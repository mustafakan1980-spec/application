from django.contrib import admin
from .models import (
    Language,
    Country, CountryTranslation,
    Institution, InstitutionTranslation,
    Category, CategoryTranslation,
    Procedure, ProcedureTranslation,
    SampleDocument, SampleDocumentTranslation,
)


class CountryTranslationInline(admin.TabularInline):
    model = CountryTranslation
    extra = 1
    fields = ('language', 'name')


class InstitutionTranslationInline(admin.StackedInline):
    model = InstitutionTranslation
    extra = 1
    fields = ('language', 'name', 'address_text', 'working_hours')


class CategoryTranslationInline(admin.TabularInline):
    model = CategoryTranslation
    extra = 1
    fields = ('language', 'name')


class ProcedureTranslationInline(admin.StackedInline):
    model = ProcedureTranslation
    extra = 1
    fields = (
        'language', 'title', 'summary',
        'eligibility', 'required_documents',
        'steps', 'fees_and_duration', 'validity', 'notes'
    )


class SampleDocumentTranslationInline(admin.TabularInline):
    model = SampleDocumentTranslation
    extra = 1
    fields = ('language', 'title', 'description')


class SampleDocumentInline(admin.TabularInline):
    model = SampleDocument
    extra = 0
    fields = ('storage_path', 'file_type', 'order')
    show_change_link = True


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name_native', 'is_rtl')
    search_fields = ('code', 'name_native')
    list_filter = ('is_rtl',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('iso2', 'flag_emoji', 'get_default_name', 'primary_language', 'is_published')
    list_filter = ('is_published', 'primary_language')
    search_fields = ('iso2', 'slug', 'translations__name')
    filter_horizontal = ('official_languages',)
    prepopulated_fields = {'slug': ('iso2',)}
    inlines = [CountryTranslationInline]

    @admin.display(description='Ülke Adı')
    def get_default_name(self, obj):
        return obj.get_name()


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('get_default_name', 'country', 'phone', 'email', 'website')
    list_filter = ('country',)
    search_fields = ('translations__name', 'phone', 'email')
    inlines = [InstitutionTranslationInline]

    @admin.display(description='Kurum Adı')
    def get_default_name(self, obj):
        return obj.get_name()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('icon', 'get_default_name', 'slug', 'order')
    ordering = ('order', 'id')
    search_fields = ('slug', 'translations__name')
    prepopulated_fields = {'slug': ('icon',)}
    inlines = [CategoryTranslationInline]

    @admin.display(description='Kategori Adı')
    def get_default_name(self, obj):
        return obj.get_name()


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = (
        'get_default_title',
        'country',
        'category',
        'institution',
        'is_published',
        'last_verified_at',
        'updated_at'
    )
    list_filter = ('country', 'category', 'is_published')
    search_fields = ('slug', 'translations__title', 'translations__summary')
    inlines = [ProcedureTranslationInline, SampleDocumentInline]

    @admin.display(description='Başvuru Başlığı')
    def get_default_title(self, obj):
        trans = obj.translations.first()
        return trans.title if trans else obj.slug


@admin.register(SampleDocument)
class SampleDocumentAdmin(admin.ModelAdmin):
    list_display = ('get_default_title', 'procedure', 'file_type', 'storage_path', 'order')
    list_filter = ('file_type', 'procedure__country')
    search_fields = ('storage_path', 'translations__title')
    inlines = [SampleDocumentTranslationInline]

    @admin.display(description='Belge Başlığı')
    def get_default_title(self, obj):
        return obj.get_title()
