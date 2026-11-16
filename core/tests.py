# -*- coding: utf-8 -*-
from django.test import TestCase, RequestFactory, override_settings
from django.urls import reverse
from core.views import custom_404_view, custom_500_view, robots_txt


class RobotsTxtTest(TestCase):
    def test_robots_txt_returned_successfully(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/plain', response['Content-Type'])
        content = response.content.decode('utf-8')
        self.assertIn('User-agent: *', content)
        self.assertIn('Disallow: /admin/', content)
        self.assertIn('Disallow: /accounts/', content)
        self.assertIn('Sitemap:', content)


class SitemapXmlTest(TestCase):
    def test_sitemap_xml_returned_successfully(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertIn('xml', response['Content-Type'])
        content = response.content.decode('utf-8')
        self.assertIn('<urlset', content)
        self.assertIn('/tr/', content)


class CustomErrorPagesTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_custom_404_view(self):
        request = self.factory.get('/non-existent-url-testing-404/')
        response = custom_404_view(request)
        self.assertEqual(response.status_code, 404)
        content = response.content.decode('utf-8')
        self.assertIn('Aradığınız Sayfayı Bulamadık', content)
        self.assertIn('Ana Sayfaya Dön', content)

    def test_custom_500_view(self):
        request = self.factory.get('/server-error-test/')
        response = custom_500_view(request)
        self.assertEqual(response.status_code, 500)
        content = response.content.decode('utf-8')
        self.assertIn('Beklenmeyen Bir Hata Oluştu', content)
        self.assertIn('Ana Sayfaya Dön', content)


class SeoAndAccessibilityTest(TestCase):
    def test_home_page_seo_and_a11y_tags(self):
        response = self.client.get('/tr/')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')

        # Canonical & Hreflang
        self.assertIn('rel="canonical"', content)
        self.assertIn('hreflang="tr"', content)
        self.assertIn('hreflang="en"', content)
        self.assertIn('hreflang="fr"', content)

        # Open Graph
        self.assertIn('property="og:title"', content)
        self.assertIn('property="og:description"', content)
        self.assertIn('property="og:url"', content)

        # A11y skip to content & landmarks
        self.assertIn('skip-to-content', content)
        self.assertIn('id="main-content"', content)


class I18nInterfaceTest(TestCase):
    def test_interface_languages(self):
        # Türkçe
        resp_tr = self.client.get('/tr/')
        self.assertEqual(resp_tr.status_code, 200)
        content_tr = resp_tr.content.decode('utf-8')
        self.assertIn('Ülkeler', content_tr)
        self.assertIn('Sorumluluk Reddi:', content_tr)

        # İngilizce
        resp_en = self.client.get('/en/')
        self.assertEqual(resp_en.status_code, 200)
        content_en = resp_en.content.decode('utf-8')
        self.assertIn('Countries', content_en)
        self.assertIn('Disclaimer:', content_en)

        # Fransızca
        resp_fr = self.client.get('/fr/')
        self.assertEqual(resp_fr.status_code, 200)
        content_fr = resp_fr.content.decode('utf-8')
        self.assertIn('Pays', content_fr)
        self.assertIn('Clause de non-responsabilit', content_fr)
