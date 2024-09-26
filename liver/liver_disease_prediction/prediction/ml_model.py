# prediction/ml_model.py
import pandas as pd
import numpy as np
import pickle
from imblearn.combine import SMOTETomek
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

def train_and_save_model():
    try:
        # Reading Dataset
        dataset = pd.read_csv(r'C:\Users\DELL\Desktop\files\liver\indian_liver_patient.csv')

        # Filling NaN Values
        dataset['Albumin_and_Globulin_Ratio'] = dataset['Albumin_and_Globulin_Ratio'].fillna(dataset['Albumin_and_Globulin_Ratio'].median())

        # Label Encoding
        dataset['Gender'] = np.where(dataset['Gender'] == 'Male', 1, 0)

        # Dropping 'Direct_Bilirubin' feature
        dataset = dataset.drop('Direct_Bilirubin', axis=1)

        # Independent and Dependent Feature
        X = dataset.iloc[:, :-1]
        y = dataset.iloc[:, -1]

        # SMOTE Technique
        smote = SMOTETomek()
        X_smote, y_smote = smote.fit_resample(X, y)

        # Train Test Split
        X_train, X_test, y_train, y_test = train_test_split(X_smote, y_smote, test_size=0.3, random_state=33)

        # RandomForestClassifier
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Saving the model
        filename = os.path.join(os.path.dirname(__file__), 'Liver2.pkl')  # Ensure correct path
        with open(filename, 'wb') as file:
            pickle.dump(model, file)

        print(f"Model successfully saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

def load_model():
    try:
        filename = os.path.join(os.path.dirname(__file__), 'Liver2.pkl')  # Ensure correct path
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        print(f"Model successfully loaded from {filename}")
        return model

    except FileNotFoundError:
        print(f"Model file not found at {filename}")
        return None

    except Exception as e:
        print(f"An error occurred while loading the model: {e}")
        return None
# prediction/ml_model.py
import pickle
import os

def load_model():
    try:
        filename = os.path.join(os.path.dirname(__file__), 'Liver2.pkl')  # Ensure correct path
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        print(f"Model successfully loaded from {filename}")
        return model

    except FileNotFoundError:
        print(f"Model file not found at {filename}")
        return None

    except Exception as e:
        print(f"An error occurred while loading the model: {e}")
        return None
