import liver_disease_prediction
from liver_disease_prediction import views

print("Import successful")
# Example content of views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")
