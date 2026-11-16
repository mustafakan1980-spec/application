from unittest.mock import patch
from django.test import TestCase, Client
from django.core.management import call_command
from django.contrib.auth import get_user_model
from catalog.models import Country, Procedure, Language, SampleDocument

User = get_user_model()


class Faz3PublicPagesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('seed_demo')

    def setUp(self):
        self.client = Client()

    def test_home_page_status(self):
        """Ana sayfa 200 dönmeli ve ülkeleri listelemeli."""
        response = self.client.get('/tr/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Popüler Ülkeler')

    def test_country_list_page(self):
        """Ülke listesi sayfası açılabilmeli."""
        response = self.client.get('/tr/countries/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Senegal')
        self.assertContains(response, 'Türkiye')
        self.assertContains(response, 'Birleşik Krallık')

    def test_country_detail_page(self):
        """Ülke detay sayfası açılmalı ve o ülkenin başvurularını listelemeli."""
        response = self.client.get('/tr/countries/sn/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Senegal')
        self.assertContains(response, 'Obtention du permis de conduire')

    def test_senegal_procedure_default_french(self):
        """Senegal ehliyeti varsayılan olarak Fransızca resmî dilde açılmalı."""
        response = self.client.get('/tr/p/sn-permis-de-conduire-b/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Obtention du permis de conduire (Catégorie B)')
        self.assertContains(response, 'Direction des Transports Routiers')
        # Örnek belgeler başlık listesi görünmeli
        self.assertContains(response, 'Formulaire de demande de permis de conduire')
        # Kilitli alan kartı görünmeli
        self.assertContains(response, 'Başvuru Detayları Kilitli')

    def test_content_language_switch_and_fallback(self):
        """İçerik dili ?lang= ile değiştirilebilmeli, olmayan dil için fallback olmalı."""
        # Türkçe çeviriye geçiş
        response_tr = self.client.get('/tr/p/sn-permis-de-conduire-b/?lang=tr')
        self.assertEqual(response_tr.status_code, 200)
        self.assertContains(response_tr, 'Senegal B Sınıfı Sürücü Belgesi Başvurusu')
        self.assertFalse(response_tr.context['is_fallback'])

        # Olmayan bir dile (örn: en - Senegal ehliyetinde en çevirisi yok) istek yapıldığında primary_language (fr) fallback devreye girmeli
        response_fallback = self.client.get('/tr/p/sn-permis-de-conduire-b/?lang=en')
        self.assertEqual(response_fallback.status_code, 200)
        self.assertTrue(response_fallback.context['is_fallback'])
        self.assertContains(response_fallback, 'ülkenin resmî dilinde gösterilmektedir')

    def test_search_view(self):
        """Arama görünümü anahtar kelimelere göre sonuç döndürmeli."""
        response = self.client.get('/tr/search/?q=ehliyet')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'B Sınıfı Sürücü Belgesi')

        response_country = self.client.get('/tr/search/?q=Senegal')
        self.assertEqual(response_country.status_code, 200)
        self.assertContains(response_country, 'sn-permis-de-conduire-b')


class Faz5AccessGateTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        if not Procedure.objects.filter(slug='tr-b-sinifi-surucu-belgesi').exists():
            call_command('seed_demo')
        cls.user = User.objects.create_user(
            username='faz5member',
            email='member@example.com',
            password='Password1234'
        )
        cls.procedure = Procedure.objects.get(slug='tr-b-sinifi-surucu-belgesi')
        cls.translation = cls.procedure.translations.get(language__code='tr')
        cls.sample_doc = cls.procedure.sample_documents.first()

    def test_guest_cannot_see_detail_content_in_html(self):
        """Misafir kullanıcının aldığı HTML çıktısında detay içerikleri ASLA yer almamalıdır."""
        response = self.client.get('/tr/p/tr-b-sinifi-surucu-belgesi/')
        self.assertEqual(response.status_code, 200)

        # Başlık ve özet görünür
        self.assertContains(response, self.translation.title)
        self.assertContains(response, 'Genel Özet')
        self.assertContains(response, 'otomobil kullanmak için')

        # Kilitli çağrı kartı ve next parametresi görünür
        self.assertContains(response, 'Başvuru Detayları Kilitli')
        self.assertContains(response, 'Ücretsiz Üye Ol')
        self.assertContains(response, '?next=/tr/p/tr-b-sinifi-surucu-belgesi/')

        # DETAY İÇERİKLERİ HTML KAYNAĞINDA ASLA OLMAMALIDIR (Server-side gate)
        self.assertNotContains(response, 'Kimler Başvurabilir? (Uygunluk Şartları)')
        self.assertNotContains(response, '18 yaşını doldurmuş olmak')
        self.assertNotContains(response, 'Sürücü Sağlık Raporu')
        self.assertNotContains(response, 'randevu.nvi.gov.tr üzerinden randevu alma')
        self.assertNotContains(response, 'Kurum İletişim Detayları')
        self.assertNotContains(response, self.procedure.institution.phone)
        self.assertNotContains(response, 'İndir (60 sn İmzalı URL)')

    def test_authenticated_user_can_see_full_details(self):
        """Üye giriş yaptığında tüm detay bölümleri HTML içerisinde görünmelidir."""
        self.client.login(username='faz5member', password='Password1234')
        response = self.client.get('/tr/p/tr-b-sinifi-surucu-belgesi/')
        self.assertEqual(response.status_code, 200)

        # Kilitli kart kalkmalı, tam erişim rozeti çıkmalı
        self.assertNotContains(response, 'Başvuru Detayları Kilitli')
        self.assertContains(response, 'Tam Erişim Aktif')

        # Tüm detay metinleri görünmeli
        self.assertContains(response, 'Kimler Başvurabilir? (Uygunluk Şartları)')
        self.assertContains(response, '18 yaşını doldurmuş olmak')
        self.assertContains(response, 'Gerekli Resmî Belgeler')
        self.assertContains(response, 'Sürücü Sağlık Raporu')
        self.assertContains(response, 'Adım Adım Başvuru Süreci')
        self.assertContains(response, 'Harç ve İşlem Süresi')
        self.assertContains(response, 'Geçerlilik Süresi')
        self.assertContains(response, 'Önemli Notlar ve İpuçları')

        # Kurum detayları görünmeli
        self.assertContains(response, 'Kurum İletişim Detayları')
        self.assertContains(response, self.procedure.institution.phone)

        # Belge indirme butonu aktif olmalı
        self.assertContains(response, f'/tr/documents/{self.sample_doc.id}/download/')
        self.assertContains(response, 'İndir (60 sn İmzalı URL)')

    def test_guest_download_redirects_to_login(self):
        """Misafir indirme URL'ine gittiğinde login sayfasına yönlendirilmelidir."""
        url = f'/tr/documents/{self.sample_doc.id}/download/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # Login sayfasına ?next= ile yönlendirilmeli
        self.assertIn('/accounts/login/', response.url)
        self.assertIn(f'next={url}', response.url)

    @patch('catalog.views.create_sample_document_signed_url')
    def test_authenticated_user_download_redirects_to_signed_url(self, mock_signed_url):
        """Üye belgeyi indirmeye çalıştığında Supabase Storage'dan üretilen signed URL'e yönlendirilmeli."""
        fake_signed_url = 'https://supabase.co/storage/v1/object/sign/sample-documents/samples/test.pdf?token=dummy123'
        mock_signed_url.return_value = fake_signed_url

        self.client.login(username='faz5member', password='Password1234')
        url = f'/tr/documents/{self.sample_doc.id}/download/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, fake_signed_url)
        mock_signed_url.assert_called_once_with(self.sample_doc.storage_path, expires_in=60)

    @patch('catalog.views.create_sample_document_signed_url')
    def test_authenticated_user_download_missing_file_handles_gracefully(self, mock_signed_url):
        """Depoda henüz dosya yoksa kullanıcı bilgilendirilmeli ve başvuru sayfasına geri yönlendirilmeli."""
        mock_signed_url.return_value = None

        self.client.login(username='faz5member', password='Password1234')
        url = f'/tr/documents/{self.sample_doc.id}/download/'
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        # Başvuru sayfasına yönlenmiş olmalı
        self.assertIn('/tr/p/tr-b-sinifi-surucu-belgesi/', response.redirect_chain[0][0])
        # Kullanıcıya bilgilendirme mesajı gösterilmeli
        self.assertContains(response, 'Bu örnek belge henüz depoya yüklenmemiştir')
