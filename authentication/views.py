from django.shortcuts import (
    render,
    redirect
)

# Create your views here.


def login(request):
    return render(request, 'authentication/login.html')


def redirect_to_login(request):
    return redirect('/auth/login')

