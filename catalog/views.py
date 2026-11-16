from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import get_language, gettext as _
from .models import Country, Procedure, Category, SampleDocument
from .helpers import (
    get_procedure_content,
    get_country_name,
    get_category_name,
    get_institution_name,
    get_institution_details,
    can_view_details,
)
from .services.storage import create_sample_document_signed_url


def country_list(request):
    """Tüm aktif ülkeleri listeler."""
    current_lang = get_language() or 'tr'
    countries = (
        Country.objects.filter(is_published=True)
        .select_related('primary_language')
        .prefetch_related('translations', 'translations__language', 'procedures')
        .order_by('iso2')
    )

    country_items = []
    for c in countries:
        country_items.append({
            'country': c,
            'name': get_country_name(c, current_lang),
            'procedures_count': c.procedures.filter(is_published=True).count(),
        })

    return render(request, 'catalog/country_list.html', {
        'countries': country_items,
    })


def country_detail(request, iso2):
    """Bir ülkenin sayfasını ve kategorilere göre başvurularını gösterir."""
    current_lang = get_language() or 'tr'
    country = get_object_or_404(
        Country.objects.select_related('primary_language')
        .prefetch_related('translations', 'translations__language', 'official_languages'),
        iso2__iexact=iso2,
        is_published=True
    )

    procedures = (
        Procedure.objects.filter(country=country, is_published=True)
        .select_related('institution', 'category')
        .prefetch_related('translations', 'translations__language', 'institution__translations')
    )

    # Kategori filtresi varsa
    category_slug = request.GET.get('category')
    active_category = None
    if category_slug:
        procedures = procedures.filter(category__slug=category_slug)
        active_category = Category.objects.filter(slug=category_slug).first()

    # Ülkedeki mevcut kategoriler
    country_categories = (
        Category.objects.filter(procedures__country=country, procedures__is_published=True)
        .distinct()
        .prefetch_related('translations')
    )

    category_items = []
    for cat in country_categories:
        category_items.append({
            'category': cat,
            'name': get_category_name(cat, current_lang),
            'is_active': (category_slug == cat.slug),
        })

    # Başvuru kartları için içerik dili
    procedure_items = []
    for proc in procedures:
        content_info = get_procedure_content(proc, None)  # varsayılan olarak ülkenin resmî dili
        trans = content_info['translation']
        procedure_items.append({
            'procedure': proc,
            'title': trans.title if trans else proc.slug,
            'summary': trans.summary if trans else '',
            'content_lang': content_info['language'],
            'institution_name': get_institution_name(proc.institution, current_lang),
            'category_name': get_category_name(proc.category, current_lang),
        })

    return render(request, 'catalog/country_detail.html', {
        'country': country,
        'country_name': get_country_name(country, current_lang),
        'categories': category_items,
        'active_category': active_category,
        'procedures': procedure_items,
    })


def procedure_detail(request, slug):
    """
    Başvuru detay sayfası (FAZ 5: Erişim Kapısı).
    - Üye ise: Tüm detay bölümleri, kurum iletişim bilgileri ve örnek belge indirme butonları görünür.
    - Misafir ise: Detay bölümleri sunucu çıktısına HİÇ eklenmez; kilitli kart ve önizleme yer tutucusu görünür.
    """
    current_lang = get_language() or 'tr'
    requested_content_lang = request.GET.get('lang')

    procedure = get_object_or_404(
        Procedure.objects.select_related(
            'country',
            'country__primary_language',
            'institution',
            'category'
        ).prefetch_related(
            'translations',
            'translations__language',
            'institution__translations',
            'category__translations',
            'country__translations',
            'sample_documents',
            'sample_documents__translations',
            'sample_documents__translations__language'
        ),
        slug=slug,
        is_published=True
    )

    content_info = get_procedure_content(procedure, requested_content_lang)
    translation = content_info['translation']
    user_can_view = can_view_details(request.user)

    # Kurum bilgileri
    institution_info = get_institution_details(procedure.institution, content_info['language'].code)

    # Örnek belgeleri hazırla
    sample_docs = []
    for doc in procedure.sample_documents.all():
        doc_trans = None
        for dt in doc.translations.all():
            if dt.language.code == content_info['language'].code:
                doc_trans = dt
                break
        if not doc_trans and doc.translations.exists():
            doc_trans = doc.translations.first()

        sample_docs.append({
            'document': doc,
            'title': doc_trans.title if doc_trans else doc.storage_path,
            'description': doc_trans.description if doc_trans else '',
            'file_type': doc.file_type,
            'download_url': doc.get_download_url(),
        })

    context = {
        'procedure': procedure,
        'translation': translation,
        'content_language': content_info['language'],
        'is_fallback': content_info['is_fallback'],
        'available_languages': content_info['available_languages'],
        'primary_language': content_info['primary_language'],
        'country_name': get_country_name(procedure.country, current_lang),
        'institution_name': institution_info['name'],
        'institution_details': institution_info if user_can_view else None,
        'category_name': get_category_name(procedure.category, current_lang),
        'sample_documents': sample_docs,
        'can_view_details': user_can_view,
    }
    return render(request, 'catalog/procedure_detail.html', context)


@login_required
def sample_document_download(request, document_id):
    """
    Kayıtlı/giriş yapmış kullanıcılar için Supabase Storage'daki private bucket'tan
    kısa ömürlü (60 sn) signed URL üretir ve kullanıcıyı bu adrese yönlendirir.
    Misafir kullanıcılar @login_required ile ?next=... parametresiyle giriş sayfasına yönlendirilir.
    """
    document = get_object_or_404(
        SampleDocument.objects.select_related('procedure', 'procedure__country'),
        id=document_id
    )

    signed_url = create_sample_document_signed_url(document.storage_path, expires_in=60)
    if signed_url:
        return HttpResponseRedirect(signed_url)

    # Dosya depoya henüz yüklenmemişse veya Storage hatası varsa kullanıcıyı bilgilendir
    messages.info(
        request,
        _("Bu örnek belge henüz depoya yüklenmemiştir veya geçici olarak erişilemiyor. Lütfen daha sonra tekrar deneyiniz.")
    )
    return redirect(document.procedure.get_absolute_url())
