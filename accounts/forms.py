from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label=_('E-posta Adresi'),
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'ornek@alanadi.com',
            'autocomplete': 'email',
        })
    )
    username = forms.CharField(
        label=_('Kullanıcı Adı'),
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'kullaniciadi',
            'autocomplete': 'username',
        })
    )
    password = forms.CharField(
        label=_('Parola'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '••••••••',
            'autocomplete': 'new-password',
        })
    )
    password_confirm = forms.CharField(
        label=_('Parola Tekrarı'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '••••••••',
            'autocomplete': 'new-password',
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError(_('Bu e-posta adresi ile zaten bir hesap kayıtlı.'))
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError(_('Bu kullanıcı adı zaten kullanılıyor.'))
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')

        if password and password_confirm:
            if password != password_confirm:
                self.add_error('password_confirm', _('Girdiğiniz parolalar birbiriyle eşleşmiyor.'))
            else:
                # Django'nun dahili parola karmaşıklık kontrollerini çalıştır
                user_instance = User(username=username, email=email)
                try:
                    validate_password(password, user=user_instance)
                except ValidationError as error:
                    self.add_error('password', error)

        return cleaned_data

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        return user


class LoginForm(forms.Form):
    login_id = forms.CharField(
        label=_('E-posta veya Kullanıcı Adı'),
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'ornek@alanadi.com veya kullaniciadi',
            'autocomplete': 'username',
        })
    )
    password = forms.CharField(
        label=_('Parola'),
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '••••••••',
            'autocomplete': 'current-password',
        })
    )
