from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsAuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = '/tr/accounts/register/'
        self.login_url = '/tr/accounts/login/'
        self.logout_url = '/tr/accounts/logout/'

    def test_registration_success(self):
        """Yeni bir kullanıcı başarıyla kaydolmalı ve otomatik giriş yapmalıdır."""
        response = self.client.post(self.register_url, {
            'email': 'ahmet@example.com',
            'username': 'ahmet_sn',
            'password': 'SecurePassword123!',
            'password_confirm': 'SecurePassword123!',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='ahmet_sn').exists())
        user = User.objects.get(username='ahmet_sn')
        self.assertEqual(user.email, 'ahmet@example.com')
        # Header'da kullanıcı adı görünmeli
        self.assertContains(response, 'ahmet_sn')

    def test_duplicate_email_rejection(self):
        """Aynı e-posta adresi (büyük/küçük harf farkı olsa dahi) tekrar kaydedilememelidir."""
        User.objects.create_user(
            username='user_one',
            email='test@example.com',
            password='Password123!'
        )

        response = self.client.post(self.register_url, {
            'email': 'TEST@EXAMPLE.COM',  # Büyük harfle
            'username': 'user_two',
            'password': 'Password123!',
            'password_confirm': 'Password123!',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bu e-posta adresi ile zaten bir hesap kayıtlı')
        self.assertFalse(User.objects.filter(username='user_two').exists())

    def test_duplicate_username_rejection(self):
        """Aynı kullanıcı adı (büyük/küçük harf farkı olsa dahi) tekrar kaydedilememelidir."""
        User.objects.create_user(
            username='unique_user',
            email='first@example.com',
            password='Password123!'
        )

        response = self.client.post(self.register_url, {
            'email': 'second@example.com',
            'username': 'UNIQUE_USER',  # Büyük harfle
            'password': 'Password123!',
            'password_confirm': 'Password123!',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bu kullanıcı adı zaten kullanılıyor')
        self.assertFalse(User.objects.filter(email='second@example.com').exists())

    def test_password_mismatch_and_short_password(self):
        """Parola uyuşmazlığı ve kısa parola engellenmelidir."""
        # 1. Parola uyuşmazlığı
        r1 = self.client.post(self.register_url, {
            'email': 'mismatch@example.com',
            'username': 'mismatch_user',
            'password': 'Password123!',
            'password_confirm': 'Different123!',
        })
        self.assertContains(r1, 'Girdiğiniz parolalar birbiriyle eşleşmiyor')

        # 2. Kısa parola
        r2 = self.client.post(self.register_url, {
            'email': 'short@example.com',
            'username': 'short_user',
            'password': '123',
            'password_confirm': '123',
        })
        self.assertContains(r2, 'kısa')

    def test_login_with_username(self):
        """Kullanıcı adı ile giriş yapılabilmelidir."""
        User.objects.create_user(
            username='deneme_user',
            email='deneme@example.com',
            password='MyPassword2026!'
        )

        response = self.client.post(self.login_url, {
            'login_id': 'DENEME_USER',  # Büyük harf desteği
            'password': 'MyPassword2026!',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'deneme_user')
        self.assertContains(response, 'Çıkış')

    def test_login_with_email(self):
        """E-posta adresi ile giriş yapılabilmelidir."""
        User.objects.create_user(
            username='email_user',
            email='loginme@example.com',
            password='MyPassword2026!'
        )

        response = self.client.post(self.login_url, {
            'login_id': 'LOGINME@EXAMPLE.COM',  # Büyük harf e-posta
            'password': 'MyPassword2026!',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'email_user')
        self.assertContains(response, 'Çıkış')

    def test_logout_post(self):
        """POST ile çıkış yapılmalı ve oturum sonlandırılmalıdır."""
        user = User.objects.create_user(
            username='logout_test_user',
            email='logout@example.com',
            password='MyPassword2026!'
        )
        self.client.force_login(user)

        # GET çıkış yapmamalı
        r_get = self.client.get(self.logout_url, follow=True)
        # Hâlâ oturum açık olmalı
        self.assertContains(r_get, 'logout_test_user')

        # POST çıkış yapmalı
        r_post = self.client.post(self.logout_url, follow=True)
        self.assertEqual(r_post.status_code, 200)
        self.assertNotContains(r_post, 'logout_test_user')
        self.assertContains(r_post, 'Giriş')

    def test_open_redirect_prevention(self):
        """Kötü niyetli harici next URL yönlendirmeleri engellenmelidir."""
        User.objects.create_user(
            username='redirect_user',
            email='redirect@example.com',
            password='MyPassword2026!'
        )

        # Harici siteye yönlendirme girişimi
        response = self.client.post(self.login_url, {
            'login_id': 'redirect_user',
            'password': 'MyPassword2026!',
            'next': 'https://evil-site.com/steal-data'
        })

        # Harici siteye gitmemeli, home/default'a yönlenmeli
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('evil-site.com', response.headers.get('Location', ''))
