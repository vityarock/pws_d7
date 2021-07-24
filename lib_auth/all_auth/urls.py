from django.urls import path
from all_auth.views import index

urlpatterns = [
    path('', index),
]