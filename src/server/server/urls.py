from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include('stravauser.urls')),
]
