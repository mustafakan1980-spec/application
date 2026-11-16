"""
URL configuration for Application project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from core.views import robots_txt
from catalog.sitemaps import StaticViewSitemap, CountrySitemap, ProcedureSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'countries': CountrySitemap,
    'procedures': ProcedureSitemap,
}

urlpatterns = [
    # SEO & Crawlers
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Admin root without language prefix
    path('admin/', admin.site.urls),
    # Language switch endpoint (doesn't have language prefix)
    path('i18n/', include('django.conf.urls.i18n')),
]

# Custom error handlers
handler404 = 'core.views.custom_404_view'
handler500 = 'core.views.custom_500_view'

# URLs with language prefix (/tr/, /en/, /fr/)
urlpatterns += i18n_patterns(
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),
    path('', include('catalog.urls')),
    prefix_default_language=True,
)
