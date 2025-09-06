from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),   # ← COMMA is required here
    path('dashboards/', include('core.urls')),           # keep your core app urls
]
