# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from catalog.models import Country, Procedure


class StaticViewSitemap(Sitemap):
    """Statik temel sayfalar için sitemap (ana sayfa, ülke listesi, hesap sayfaları)."""
    priority = 0.9
    changefreq = 'daily'
    i18n = True

    def items(self):
        return ['home', 'country_list', 'register', 'login']

    def location(self, item):
        return reverse(item)


class CountrySitemap(Sitemap):
    """Yayınlanmış ülkeler için sitemap."""
    priority = 0.8
    changefreq = 'weekly'
    i18n = True

    def items(self):
        return Country.objects.filter(is_published=True).order_by('iso2')

    def location(self, obj):
        return reverse('country_detail', kwargs={'iso2': obj.iso2.lower()})

    def lastmod(self, obj):
        return None


class ProcedureSitemap(Sitemap):
    """Yayınlanmış başvuru prosedürleri için sitemap."""
    priority = 1.0
    changefreq = 'weekly'
    i18n = True

    def items(self):
        return Procedure.objects.filter(is_published=True).select_related('country').order_by('slug')

    def location(self, obj):
        return reverse('procedure_detail', kwargs={'slug': obj.slug})

    def lastmod(self, obj):
        return obj.last_verified_at
