from django.urls import path
from .evidence_views import (
    evidence_all,
    evidence_store,
    evidence_download,
    evidence_delete
)


urlpatterns = [
    path('all', evidence_all, name='evidence.all'),
    path('upload', evidence_store, name='evidence.store'),
    path('<int:evidence>/download', evidence_download, name='evidence.download'),
    path('<int:evidence>/delete', evidence_delete, name='evidence.delete'),
]