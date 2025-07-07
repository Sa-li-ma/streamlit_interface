import streamlit as st
import requests

st.title("~~~~~~Docteur~~~~~~")

# Formulaire utilisateur
age = st.number_input("Âge", 1, 120, 50)
sex = st.selectbox("Sexe", [0, 1], format_func=lambda x: "Femme" if x == 0 else "Homme")
cp = st.selectbox("Type de douleur thoracique", [0, 1, 2, 3])
trestbps = st.number_input("Pression artérielle au repos", 80, 200, 120)
chol = st.number_input("Cholestérol", 100, 600, 200)
fbs = st.selectbox("Glycémie à jeun > 120 mg/dl", [0, 1])
restecg = st.selectbox("Résultats ECG au repos", [0, 1, 2])
thalach = st.number_input("Fréquence cardiaque max", 60, 220, 150)
exang = st.selectbox("Angine induite par l’exercice", [0, 1])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Pente du segment ST", [0, 1, 2])
ca = st.selectbox("Nbre de vaisseaux colorés", [0, 1, 2, 3])
thal = st.selectbox("Thalassémie", [0, 1, 2, 3])

if st.button("¨Prédire"):
    # Création du dictionnaire à envoyer
    data = {
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    # Appel à l’API FastAPI
    response = requests.post("http://localhost:8000/predict", json=data)

    if response.status_code == 200:
        result = response.json()["prediction"]
        if result == 1:
            st.error("Risque de maladie détecté !")
        else:
            st.success("Aucun risque détecté.")
    else:
        st.warning("Erreur dans la communication avec l’API.")
