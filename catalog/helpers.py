from .models import Language


def get_procedure_content(procedure, requested_lang_code=None):
    """
    İçerik dili çözümleme mantığı (PLAN.md Bölüm 6):
    - Başvuru sayfası ilk açıldığında içerik, ülkenin resmî dilinde gösterilir.
    - Kullanıcı ?lang=xx parametresi ile içerik dilini değiştirebilir.
    - İstenen dilde çeviri yoksa ülkenin primary_language içeriği gösterilir ve
      is_fallback=True bayrağı ile bilgi etiketi çıkartılır.
    - N+1 sorgusu oluşmaması için translations prefetch edilmiş queryset ile uyumludur.
    """
    all_translations = list(procedure.translations.all())
    available_langs = [t.language for t in all_translations]
    primary_lang = procedure.country.primary_language

    selected_trans = None
    is_fallback = False

    # 1. Kullanıcı açıkça bir dil seçtiyse
    if requested_lang_code:
        for trans in all_translations:
            if trans.language.code == requested_lang_code:
                selected_trans = trans
                is_fallback = False
                break

    # 2. Seçilmediyse veya bulunamadıysa: Ülkenin birincil resmî dili
    if not selected_trans:
        for trans in all_translations:
            if trans.language.code == primary_lang.code:
                selected_trans = trans
                # Eğer kullanıcı başka dil istemiş ama bulamadığımız için primary'e düştüysek fallback'tir
                is_fallback = bool(requested_lang_code and requested_lang_code != primary_lang.code)
                break

    # 3. Ülkenin birincil dilinde de yoksa ilk bulunan çeviriye düş
    if not selected_trans and all_translations:
        selected_trans = all_translations[0]
        is_fallback = True

    return {
        'translation': selected_trans,
        'language': selected_trans.language if selected_trans else primary_lang,
        'is_fallback': is_fallback,
        'available_languages': available_langs,
        'primary_language': primary_lang,
    }


def get_country_name(country, lang_code=None):
    """Ülke adını verilen arayüz dilinde, yoksa birincil dilinde döndürür."""
    translations = list(country.translations.all())
    if lang_code:
        for t in translations:
            if t.language.code == lang_code:
                return t.name
    # Fallback to primary language
    for t in translations:
        if t.language.code == country.primary_language.code:
            return t.name
    return translations[0].name if translations else country.iso2


def get_category_name(category, lang_code=None):
    """Kategori adını verilen dilde, yoksa ilk çeviride döndürür."""
    translations = list(category.translations.all())
    if lang_code:
        for t in translations:
            if t.language.code == lang_code:
                return t.name
    return translations[0].name if translations else category.slug


def get_institution_name(institution, lang_code=None):
    """Kurum adını verilen dilde veya ülkenin birincil dilinde döndürür."""
    translations = list(institution.translations.all())
    if lang_code:
        for t in translations:
            if t.language.code == lang_code:
                return t.name
    for t in translations:
        if t.language.code == institution.country.primary_language.code:
            return t.name
    return translations[0].name if translations else institution.slug


def can_view_details(user) -> bool:
    """
    PLAN.md Bölüm 7 Erişim Kuralları:
    Kullanıcı üye ise (is_authenticated) başvuru detaylarını ve
    örnek belge indirme bağlantılarını görebilir; misafirler ise
    sadece başlık, kurum adı, kısa özet ve belge listesini görebilir.
    """
    return bool(user and user.is_authenticated)


def get_institution_details(institution, lang_code=None):
    """
    Kurumun çevrilmiş adı, adres metni ve çalışma saatlerini döndürür.
    """
    translations = list(institution.translations.all())
    selected_trans = None
    if lang_code:
        for t in translations:
            if t.language.code == lang_code:
                selected_trans = t
                break
    if not selected_trans:
        for t in translations:
            if t.language.code == institution.country.primary_language.code:
                selected_trans = t
                break
    if not selected_trans and translations:
        selected_trans = translations[0]

    return {
        'name': selected_trans.name if selected_trans else institution.slug,
        'address_text': selected_trans.address_text if (selected_trans and selected_trans.address_text) else institution.address,
        'working_hours': selected_trans.working_hours if selected_trans else '',
        'phone': institution.phone,
        'email': institution.email,
        'website': institution.website,
        'map_url': institution.map_url,
    }
