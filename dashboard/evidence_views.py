from django.shortcuts import render, get_object_or_404, redirect

import config.settings
from .models import Case, Evidence
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import os
from .helpers import hash_file, get_filename
from config.settings import BASE_DIR
from django.contrib import messages
from django.http import FileResponse


@login_required
def evidence_all(request, case):
    case = get_object_or_404(Case, id=case)
    evidences = Evidence.objects.all().order_by('-created_at')
    paginator = Paginator(evidences, per_page=10)
    page_number = request.GET.get('page')
    evidences = paginator.get_page(page_number)
    context = {
        'case': case,
        'evidences': evidences
    }
    return render(request, 'dashboard/evidences/all.html', context)


@login_required
def evidence_download(request, case, evidence):
    case = get_object_or_404(Case, id=case)
    evidence = get_object_or_404(Evidence, id=evidence)
    return FileResponse(
        open(os.path.join(config.settings.BASE_DIR, evidence.file_url.strip('/')), 'rb'),
        as_attachment=True,
        filename=evidence.file_name
    )


@login_required
def evidence_delete(request, case, evidence):
    case = get_object_or_404(Case, id=case)
    evidence = get_object_or_404(Evidence, id=evidence)
    evidence.delete()
    return redirect('evidence.all', case=case.id, evidence=evidence.id)


@login_required
def evidence_store(request, case):
    case = get_object_or_404(Case, id=case)
    if request.method == 'POST' and request.FILES['evidence']:
        evidence = request.FILES['evidence']
        name, extension = get_filename(evidence.name)
        fs = FileSystemStorage()
        filename = fs.save(name, evidence)
        file_url = fs.url(name)
        evidence_modal = Evidence()
        evidence_modal.file_name = evidence.name
        evidence_modal.file_url = file_url
        evidence_modal.file_extension = extension
        evidence_modal.file_hash = hash_file(os.path.join(BASE_DIR, 'uploads/'+filename))
        evidence_modal.case = case
        evidence_modal.save()
        messages.add_message(request, messages.SUCCESS, 'Your evidence is submitted successfully.')
        return redirect('evidence.all', case=case.id)

