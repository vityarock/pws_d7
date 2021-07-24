from django.contrib import admin
from django.urls import include, path
from all_auth import views
import all_auth
from all_auth.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('all_auth.urls')),
    path('accounts/', include('allauth.urls')),
]
