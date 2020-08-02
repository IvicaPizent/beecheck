from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beecheck/', include('beecheck.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
