from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .helpers import get_filename, hash_file
import os
from config.settings import BASE_DIR
from django.contrib import messages
from authentication.models import User
from django.core.paginator import Paginator
from forms.UserForm import UserForm


# Create your views here.
@login_required
def dashboard_view(request):
    return render(request, 'dashboard/home.html')


@login_required
def validate_evidence(request):
    if request.method == 'POST' and request.FILES['file']:
        evidence = request.FILES['file']
        name, extension = get_filename(evidence.name)
        fs = FileSystemStorage()
        filename = fs.save(name, evidence)
        file_url = fs.url(name)
        checksum = request.POST['checksum']
        if checksum == hash_file(os.path.join(BASE_DIR, 'uploads/'+filename)):
            messages.add_message(request, messages.SUCCESS, 'Your file is valid')
        else:
            messages.add_message(request, messages.ERROR, 'Your file is not valid')
        os.remove(os.path.join(BASE_DIR, file_url.strip('/')))
    return render(request, 'dashboard/validate.html')


@login_required
def users_view(request):
    users = User.objects.all().order_by('-id')
    paginator = Paginator(users, per_page=10)
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    context = {
        'users': users
    }
    return render(request, 'dashboard/users/all.html', context)


@login_required
def user_add(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get('password'))
        user.save()
        messages.add_message(request, messages.SUCCESS, 'User is created successfully.')
    context = {
        'form': form
    }
    return render(request, 'dashboard/users/add.html', context)


@login_required
def user_delete(request, user):
    user = get_object_or_404(User, id=user)
    user.delete()
    return redirect('users.all')
