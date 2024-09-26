# prediction/views.py

from django.shortcuts import render
import numpy as np

def predict(request):
    if request.method == 'POST':
        # Extract data from the form
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        total_bilirubin = request.POST.get('total_bilirubin')
        direct_bilirubin = request.POST.get('direct_bilirubin')
        alkaline_phosphatase = request.POST.get('alkaline_phosphatase')
        alanine_aminotransferase = request.POST.get('alanine_aminotransferase')
        aspartate_aminotransferase = request.POST.get('aspartate_aminotransferase')
        total_proteins = request.POST.get('total_proteins')
        albumin = request.POST.get('albumin')
        albumin_globulin_ratio = request.POST.get('albumin_globulin_ratio')

        # Prepare the input data for prediction
        input_data = np.array([[age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphatase,
                                alanine_aminotransferase, aspartate_aminotransferase,
                                total_proteins, albumin, albumin_globulin_ratio]])

        # Here you would call your prediction logic
        # For demonstration, let's assume the prediction is based on total_bilirubin
        prediction = "Positive" if float(total_bilirubin) > 1.2 else "Negative"

        return render(request, 'result.html', {'prediction': prediction})

    return render(request, 'index.html')