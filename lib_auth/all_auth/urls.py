from django.urls import path
from all_auth.views import login_page


urlpatterns = [
    path('', login_page),
]