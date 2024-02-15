# app_admin/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import dashboard, add_expense

urlpatterns = [
    path('admin/', admin.site.urls), #admin
    path("", include("pages.urls")), #homepage
    path("projects/", include("projects.urls")), #projects
    path("dashboard/", include("dashboard.urls")), #dashboard
    path("login/", include("login.urls")), #login
    path('', dashboard, name='dashboard'),
    path('add_expense/', add_expense, name='add_expense'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)