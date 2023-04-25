from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .helpers import get_filename, hash_file
import os
from config.settings import BASE_DIR
from django.contrib import messages


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
