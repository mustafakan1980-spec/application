from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import gettext_lazy as _
from .forms import RegisterForm, LoginForm


def get_safe_redirect_url(request, default_url='home'):
    """Açık yönlendirme (open redirect) açığını önlemek için next URL doğrulaması yapar."""
    next_url = request.POST.get('next') or request.GET.get('next')
    if next_url and url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure()
    ):
        return next_url
    return default_url


def register_view(request):
    """Yeni kullanıcı kaydı görünümü."""
    if request.user.is_authenticated:
        return redirect('home')

    next_url = request.GET.get('next', '')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Başarılı kayıt sonrası doğrudan giriş yaptır
            login(request, user, backend='accounts.authentication.EmailOrUsernameModelBackend')
            redirect_to = get_safe_redirect_url(request, default_url='home')
            return redirect(redirect_to)
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'form': form,
        'next_url': next_url,
    })


def login_view(request):
    """E-posta veya kullanıcı adı ile giriş görünümü."""
    if request.user.is_authenticated:
        return redirect('home')

    next_url = request.GET.get('next', '')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_id = form.cleaned_data['login_id']
            password = form.cleaned_data['password']
            user = authenticate(request, username=login_id, password=password)

            if user is not None:
                login(request, user)
                redirect_to = get_safe_redirect_url(request, default_url='home')
                return redirect(redirect_to)
            else:
                form.add_error(None, _('Girdiğiniz bilgiler hatalı. Lütfen e-posta/kullanıcı adı ve parolanızı kontrol edin.'))
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {
        'form': form,
        'next_url': next_url,
    })


def logout_view(request):
    """Güvenli çıkış işlemi (yalnızca POST istekleri ile çalışır)."""
    if request.method == 'POST':
        logout(request)
        redirect_to = get_safe_redirect_url(request, default_url='home')
        return redirect(redirect_to)
    return redirect('home')
