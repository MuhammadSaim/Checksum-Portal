from django.urls import (
    path,
    include
)
from .views import (
    dashboard_view,
    validate_evidence,
    users_view,
    user_add,
    user_delete
)


urlpatterns = [
    path('', dashboard_view, name="dashboard"),
    path('validate', validate_evidence, name='validate'),
    path('users', users_view, name='users.all'),
    path('users/add', user_add, name='users.add'),
    path('users/<int:user>/delete', user_delete, name='users.delete'),
    path('cases/', include('dashboard.case_urls')),
]