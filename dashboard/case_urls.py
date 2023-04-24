from django.urls import path
from .case_views import (
    case_all,
    case_create,
    case_delete,
    case_edit
)


urlpatterns = [
    path('all', case_all, name="cases.all"),
    path('add', case_create, name="cases.create"),
    path('delete/<int:_id>', case_delete, name="cases.delete"),
    path('edit/<int:_id>', case_edit, name="cases.edit"),
]
