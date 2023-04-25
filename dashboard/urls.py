from django.urls import (
    path,
    include
)
from .views import dashboard_view, validate_evidence


urlpatterns = [
    path('', dashboard_view, name="dashboard"),
    path('validate', validate_evidence, name='validate'),
    path('cases/', include('dashboard.case_urls')),
]