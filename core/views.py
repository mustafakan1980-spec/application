from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import get_language
from django.db.models import Q
from catalog.models import Country, Category, Procedure
from catalog.helpers import get_country_name, get_category_name, get_procedure_content, get_institution_name


def robots_txt(request):
    """robots.txt çıktısı: Tüm arama motorlarına izin verir ve sitemap.xml yolunu gösterir."""
    sitemap_url = request.build_absolute_uri('/sitemap.xml')
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Disallow: /documents/",
        f"Sitemap: {sitemap_url}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")


def custom_404_view(request, exception=None):
    """Marka diliyle özel 404 Sayfa Bulunamadı sayfası."""
    return render(request, '404.html', status=404)


def custom_500_view(request):
    """Marka diliyle özel 500 Sunucu Hatası sayfası."""
    return render(request, '500.html', status=500)


def home(request):
    """Ana sayfa - Arama, popüler ülkeler, kategoriler ve öne çıkan başvurular."""
    current_lang = get_language() or 'tr'

    countries = (
        Country.objects.filter(is_published=True)
        .select_related('primary_language')
        .prefetch_related('translations', 'translations__language', 'procedures')[:6]
    )
    country_cards = []
    for c in countries:
        country_cards.append({
            'country': c,
            'name': get_country_name(c, current_lang),
            'procedures_count': c.procedures.filter(is_published=True).count(),
        })

    categories = (
        Category.objects.all()
        .prefetch_related('translations', 'translations__language', 'procedures')
        .order_by('order')
    )
    category_cards = []
    for cat in categories:
        category_cards.append({
            'category': cat,
            'name': get_category_name(cat, current_lang),
            'procedures_count': cat.procedures.filter(is_published=True).count(),
        })

    procedures = (
        Procedure.objects.filter(is_published=True)
        .select_related('country', 'category', 'institution', 'country__primary_language')
        .prefetch_related('translations', 'translations__language')[:6]
    )
    procedure_cards = []
    for proc in procedures:
        content_info = get_procedure_content(proc, None)
        trans = content_info['translation']
        procedure_cards.append({
            'procedure': proc,
            'title': trans.title if trans else proc.slug,
            'summary': trans.summary if trans else '',
            'country_name': get_country_name(proc.country, current_lang),
            'institution_name': get_institution_name(proc.institution, current_lang),
            'category_name': get_category_name(proc.category, current_lang),
            'content_lang': content_info['language'],
        })

    return render(request, 'core/home.html', {
        'countries': country_cards,
        'categories': category_cards,
        'procedures': procedure_cards,
    })


def search(request):
    """Basit arama görünümü: Başvuru başlığı, özet, ülke adı ve kategori adı üzerinde arar."""
    query = request.GET.get('q', '').strip()
    current_lang = get_language() or 'tr'
    results = []

    if query:
        procedures = (
            Procedure.objects.filter(is_published=True)
            .filter(
                Q(translations__title__icontains=query) |
                Q(translations__summary__icontains=query) |
                Q(country__translations__name__icontains=query) |
                Q(category__translations__name__icontains=query) |
                Q(institution__translations__name__icontains=query)
            )
            .select_related('country', 'institution', 'category', 'country__primary_language')
            .prefetch_related('translations', 'translations__language', 'institution__translations')
            .distinct()
        )

        for proc in procedures:
            content_info = get_procedure_content(proc, None)
            trans = content_info['translation']
            results.append({
                'procedure': proc,
                'title': trans.title if trans else proc.slug,
                'summary': trans.summary if trans else '',
                'country_name': get_country_name(proc.country, current_lang),
                'institution_name': get_institution_name(proc.institution, current_lang),
                'category_name': get_category_name(proc.category, current_lang),
                'content_lang': content_info['language'],
            })

    return render(request, 'core/search.html', {
        'query': query,
        'results': results,
        'results_count': len(results),
    })
