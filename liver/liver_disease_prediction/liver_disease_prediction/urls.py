


# liver_disease_prediction/urls.py
from django.contrib import admin
from django.urls import path, include
from prediction.views import predict  # Import the predict view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', predict, name='home'),  # Set the root URL to point to the predict view
    path('predict/', include('prediction.urls')),  # Keep the existing URL pattern
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]


# liver_disease_prediction/urls.py

from django.contrib import admin
from django.urls import path, include  # Include the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prediction.urls')),  # Include the URLs from the prediction app
]