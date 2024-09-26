# prediction/forms.py
from django import forms

class PredictionForm(forms.Form):
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[(1, 'Male'), (0, 'Female')])
    total_bilirubin = forms.FloatField(label='Total Bilirubin')
    direct_bilirubin = forms.FloatField(label='Direct Bilirubin')
    alkaline_phosphatase = forms.FloatField(label='Alkaline Phosphatase')
    alanine_transaminase = forms.FloatField(label='Alanine Transaminase')
    aspartate_transaminase = forms.FloatField(label='Aspartate Transaminase')
    total_proteins = forms.FloatField(label='Total Proteins')
    albumin = forms.FloatField(label='Albumin')
    albumin_and_globulin_ratio = forms.FloatField(label='Albumin and Globulin Ratio')
