# prediction/urls.py

from django.urls import path
from .views import predict  # Ensure this matches the function name in views.py

urlpatterns = [
    path('', predict, name='predict'),  # Use predict as the view function
]