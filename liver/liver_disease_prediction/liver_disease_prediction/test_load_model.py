# test_load_model.py
from prediction.ml_model import load_model

model = load_model()
if model:
    print("Model loaded successfully.")
else:
    print("Failed to load the model.")
