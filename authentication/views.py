from django.shortcuts import (
    render,
    redirect
)
from django.contrib.auth import (
    authenticate,
    login
)
from forms.LoginForm import LoginForm
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
    return render(request, 'authentication/login.html', context={
        'form': form
    })


def redirect_to_login(request):
    return redirect('/auth/login')

