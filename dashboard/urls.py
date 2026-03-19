from django.urls import path
from .views import dashboard_page, dashboard_metrics


urlpatterns = [
    path("", dashboard_page),
    path("api/", dashboard_metrics),
]