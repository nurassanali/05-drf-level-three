from django.contrib import admin
from django.urls import include, path
from rest_auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("profiles.api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/rest-auth/", include("rest_auth.urls")),   
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
