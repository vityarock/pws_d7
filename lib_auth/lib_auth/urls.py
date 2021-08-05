from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
# from all_auth import views
# import all_auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)