from django.urls import (
    path,
    include
)
from .views import dashboard_view


urlpatterns = [
    path('', dashboard_view, name="dashboard"),
    path('cases/', include('dashboard.case_urls')),
]