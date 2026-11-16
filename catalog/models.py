from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.Model):
    code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name=_('Dil Kodu (ISO)'),
        help_text=_('Örn: tr, en, fr, ar')
    )
    name_native = models.CharField(
        max_length=100,
        verbose_name=_('Yerel Dil Adı'),
        help_text=_('Örn: Türkçe, English, Français')
    )
    is_rtl = models.BooleanField(
        default=False,
        verbose_name=_('Sağdan Sola (RTL) mı?')
    )

    class Meta:
        verbose_name = _('Dil')
        verbose_name_plural = _('Diller')
        ordering = ['code']

    def __str__(self):
        return f"{self.name_native} ({self.code})"


class Country(models.Model):
    iso2 = models.CharField(
        max_length=2,
        unique=True,
        verbose_name=_('ISO2 Ülke Kodu'),
        help_text=_('Örn: SN, TR, GB')
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name=_('URL Slug')
    )
    flag_emoji = models.CharField(
        max_length=10,
        blank=True,
        verbose_name=_('Bayrak Emojisi')
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name=_('Yayınlandı mı?')
    )
    official_languages = models.ManyToManyField(
        Language,
        related_name='countries_official',
        verbose_name=_('Resmî Diller')
    )
    primary_language = models.ForeignKey(
        Language,
        on_delete=models.PROTECT,
        related_name='countries_primary',
        verbose_name=_('Birincil Dil')
    )

    class Meta:
        verbose_name = _('Ülke')
        verbose_name_plural = _('Ülkeler')
        ordering = ['iso2']

    def __str__(self):
        return f"{self.flag_emoji} {self.iso2}"

    def get_name(self, lang_code=None):
        if lang_code:
            trans = self.translations.filter(language__code=lang_code).first()
            if trans and trans.name:
                return trans.name
        primary_trans = self.translations.filter(language=self.primary_language).first()
        if primary_trans and primary_trans.name:
            return primary_trans.name
        first_trans = self.translations.first()
        return first_trans.name if first_trans else self.iso2


class CountryTranslation(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='translations',
        verbose_name=_('Ülke')
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='country_translations',
        verbose_name=_('Dil')
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_('Ülke Adı')
    )

    class Meta:
        verbose_name = _('Ülke Çevirisi')
        verbose_name_plural = _('Ülke Çevirileri')
        unique_together = ('country', 'language')

    def __str__(self):
        return f"{self.name} ({self.language.code})"


class Institution(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='institutions',
        verbose_name=_('Ülke')
    )
    slug = models.SlugField(
        max_length=150,
        blank=True,
        verbose_name=_('URL Slug')
    )
    website = models.URLField(
        blank=True,
        verbose_name=_('Resmî Web Sitesi')
    )
    phone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Telefon')
    )
    email = models.EmailField(
        blank=True,
        verbose_name=_('E-posta')
    )
    address = models.TextField(
        blank=True,
        verbose_name=_('Adres (Varsayılan)')
    )
    map_url = models.URLField(
        blank=True,
        verbose_name=_('Harita Konum Linki')
    )

    class Meta:
        verbose_name = _('Resmî Kurum')
        verbose_name_plural = _('Resmî Kurumlar')
        ordering = ['country', 'id']

    def __str__(self):
        trans = self.translations.first()
        name = trans.name if trans else f"Institution #{self.id}"
        return f"{name} ({self.country.iso2})"

    def get_name(self, lang_code=None):
        if lang_code:
            trans = self.translations.filter(language__code=lang_code).first()
            if trans and trans.name:
                return trans.name
        primary_trans = self.translations.filter(language=self.country.primary_language).first()
        if primary_trans and primary_trans.name:
            return primary_trans.name
        first_trans = self.translations.first()
        return first_trans.name if first_trans else f"Institution #{self.id}"


class InstitutionTranslation(models.Model):
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name='translations',
        verbose_name=_('Kurum')
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='institution_translations',
        verbose_name=_('Dil')
    )
    name = models.CharField(
        max_length=200,
        verbose_name=_('Kurum Adı')
    )
    address_text = models.TextField(
        blank=True,
        verbose_name=_('Adres Metni')
    )
    working_hours = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_('Çalışma Saatleri')
    )

    class Meta:
        verbose_name = _('Kurum Çevirisi')
        verbose_name_plural = _('Kurum Çevirileri')
        unique_together = ('institution', 'language')

    def __str__(self):
        return f"{self.name} ({self.language.code})"


class Category(models.Model):
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name=_('URL Slug')
    )
    icon = models.CharField(
        max_length=20,
        default='📄',
        verbose_name=_('Kategori İkonu (Emoji)')
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Sıralama')
    )

    class Meta:
        verbose_name = _('Kategori')
        verbose_name_plural = _('Kategoriler')
        ordering = ['order', 'id']

    def __str__(self):
        trans = self.translations.first()
        name = trans.name if trans else self.slug
        return f"{self.icon} {name}"

    def get_name(self, lang_code=None):
        if lang_code:
            trans = self.translations.filter(language__code=lang_code).first()
            if trans and trans.name:
                return trans.name
        first_trans = self.translations.first()
        return first_trans.name if first_trans else self.slug


class CategoryTranslation(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='translations',
        verbose_name=_('Kategori')
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='category_translations',
        verbose_name=_('Dil')
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_('Kategori Adı')
    )

    class Meta:
        verbose_name = _('Kategori Çevirisi')
        verbose_name_plural = _('Kategori Çevirileri')
        unique_together = ('category', 'language')

    def __str__(self):
        return f"{self.name} ({self.language.code})"


class Procedure(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='procedures',
        verbose_name=_('Ülke')
    )
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name='procedures',
        verbose_name=_('Başvurulacak Kurum')
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='procedures',
        verbose_name=_('Kategori')
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name=_('URL Slug')
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name=_('Yayınlandı mı?')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Oluşturulma Tarihi')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Güncellenme Tarihi')
    )
    last_verified_at = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Son Doğrulama Tarihi')
    )
    official_source_url = models.URLField(
        blank=True,
        verbose_name=_('Resmî Bilgi Kaynağı Linki')
    )

    class Meta:
        verbose_name = _('Başvuru (Prosedür)')
        verbose_name_plural = _('Başvurular (Prosedürler)')
        ordering = ['country', 'category', 'slug']

    def __str__(self):
        trans = self.translations.first()
        title = trans.title if trans else self.slug
        return f"[{self.country.iso2}] {title}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('procedure_detail', kwargs={'slug': self.slug})

    def get_translation(self, lang_code=None):
        """İçerik dili arama: istenen dil -> ülkenin birincil dili -> ilk bulunan çeviri"""
        if lang_code:
            trans = self.translations.filter(language__code=lang_code).first()
            if trans:
                return trans, False
        primary_trans = self.translations.filter(language=self.country.primary_language).first()
        if primary_trans:
            return primary_trans, True
        first_trans = self.translations.first()
        return first_trans, True


class ProcedureTranslation(models.Model):
    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE,
        related_name='translations',
        verbose_name=_('Başvuru')
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='procedure_translations',
        verbose_name=_('Dil')
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('Başvuru Başlığı')
    )
    summary = models.TextField(
        verbose_name=_('Kısa Özet'),
        help_text=_('Kısa özet - Herkese açık görüntülenir')
    )
    eligibility = models.TextField(
        blank=True,
        verbose_name=_('Kimler Başvurabilir / Geçerlilik Şartları')
    )
    required_documents = models.TextField(
        blank=True,
        verbose_name=_('Gerekli Belgeler')
    )
    steps = models.TextField(
        blank=True,
        verbose_name=_('Başvuru Adımları')
    )
    fees_and_duration = models.TextField(
        blank=True,
        verbose_name=_('Ücret ve Süre')
    )
    validity = models.TextField(
        blank=True,
        verbose_name=_('Geçerlilik Koşulları')
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_('Ek Notlar')
    )

    class Meta:
        verbose_name = _('Başvuru Çevirisi')
        verbose_name_plural = _('Başvuru Çevirileri')
        unique_together = ('procedure', 'language')

    def __str__(self):
        return f"{self.title} ({self.language.code})"


class SampleDocument(models.Model):
    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE,
        related_name='sample_documents',
        verbose_name=_('Başvuru')
    )
    storage_path = models.CharField(
        max_length=500,
        verbose_name=_('Supabase Storage Dosya Yolu'),
        help_text=_('Örn: samples/sn_permis_form.pdf')
    )
    file_type = models.CharField(
        max_length=50,
        default='PDF',
        verbose_name=_('Dosya Türü')
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Görüntüleme Sırası')
    )

    class Meta:
        verbose_name = _('Örnek Belge')
        verbose_name_plural = _('Örnek Belgeler')
        ordering = ['procedure', 'order', 'id']

    def __str__(self):
        trans = self.translations.first()
        title = trans.title if trans else self.storage_path
        return f"{title} ({self.file_type})"

    def get_download_url(self):
        from django.urls import reverse
        return reverse('sample_document_download', kwargs={'document_id': self.id})

    def get_title(self, lang_code=None):
        if lang_code:
            trans = self.translations.filter(language__code=lang_code).first()
            if trans and trans.title:
                return trans.title
        primary_trans = self.translations.filter(language=self.procedure.country.primary_language).first()
        if primary_trans and primary_trans.title:
            return primary_trans.title
        first_trans = self.translations.first()
        return first_trans.title if first_trans else self.storage_path


class SampleDocumentTranslation(models.Model):
    document = models.ForeignKey(
        SampleDocument,
        on_delete=models.CASCADE,
        related_name='translations',
        verbose_name=_('Örnek Belge')
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='document_translations',
        verbose_name=_('Dil')
    )
    title = models.CharField(
        max_length=200,
        verbose_name=_('Belge Başlığı')
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('Belge Açıklaması')
    )

    class Meta:
        verbose_name = _('Örnek Belge Çevirisi')
        verbose_name_plural = _('Örnek Belge Çevirileri')
        unique_together = ('document', 'language')

    def __str__(self):
        return f"{self.title} ({self.language.code})"
