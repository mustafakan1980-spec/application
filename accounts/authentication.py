from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

User = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Kullanıcının hem e-posta adresi hem de kullanıcı adı ile giriş yapabilmesini sağlar.
    Büyük/küçük harf duyarsız (case-insensitive) eşleşme yapar.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('email')

        if not username or not password:
            return None

        username = username.strip()

        try:
            # Hem username hem de email üzerinde büyük/küçük harf duyarsız arama
            user = User.objects.filter(
                Q(username__iexact=username) | Q(email__iexact=username)
            ).first()
        except Exception:
            return None

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
