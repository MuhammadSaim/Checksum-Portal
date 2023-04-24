from django.shortcuts import (
    render,
    redirect
)
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib import messages
from forms.LoginForm import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    next_url = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Your username/password is incorrect')
    return render(request, 'authentication/login.html', context={
        'form': form
    })


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('dashboard')
    logout(request)
    return redirect('login')


def redirect_to_login(request):
    return redirect('/auth/login')

