from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Case
from django.core.paginator import Paginator
from forms.CaseForm import CaseForm
from django.contrib import messages


@login_required
def case_all(request):
    cases = Case.objects.all().order_by('-created_at')
    paginator = Paginator(cases, per_page=10)
    page_number = request.GET.get('page')
    cases = paginator.get_page(page_number)
    return render(request, 'dashboard/cases/all.html', {'cases': cases})


@login_required
def case_create(request):
    form = CaseForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        messages.add_message(request, messages.SUCCESS, 'Your case is created successfully.')
    return render(request, 'dashboard/cases/add.html', {'form': form})


@login_required
def case_edit(request, _id):
    case = get_object_or_404(Case, id=_id)
    form = CaseForm(request.POST or None, instance=case)
    if form.is_valid():
        form.save(commit=True)
        messages.add_message(request, messages.SUCCESS, 'Your case is updated successfully.')
    return render(request, 'dashboard/cases/edit.html', {
        'form': form,
        'case': case
    })


@login_required
def case_delete(request, _id):
    case = get_object_or_404(Case, id=_id)
    case.delete()
    return redirect('cases.all')
