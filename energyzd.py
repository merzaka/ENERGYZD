import streamlit as st
import pandas as pd

st.title("⚡ Plateforme d'Optimisation Énergétique - Algérie (V1)")
st.sidebar.header("Paramètres de la Maison")

# Étape 1 : Localisation simple
wilaya = st.sidebar.selectbox("Wilaya", ["Batna", "Alger", "Oran", "Constantine"])
commune = st.sidebar.text_input("Commune", "Batna")

# Étape 2 : Saisie des équipements
st.header("Gestion des Équipements")
category = st.selectbox("Catégorie d'équipement", ["Climatisation", "Eau chaude", "Cuisine", "Linge", "Électronique", "Éclairage", "Pompes", "Autres"])
equipment_name = st.text_input("Nom de l'équipement", "Climatiseur Split")
brand = st.selectbox("Marque", ["Condor", "Samsung", "LG", "Starlight", "Brandt", "Autre"])

col1, col2 = st.columns(2)
with col1:
    nombre = st.number_input("Nombre", min_value=1, value=1)
with col2:
    heures = st.number_input("Heures d'utilisation / jour", min_value=0.0, max_value=24.0, value=5.0)

# Gestion de la puissance par défaut ou personnalisée
connu = st.radio("Connaissez-vous la puissance exacte de l'appareil ?", ["Oui", "Non (utiliser la valeur par défaut)"])

# Valeur par défaut simplifiée par catégorie pour la V1 (1 seule valeur par catégorie comme demandé)
default_powers = {
    "Climatisation": 1200, "Eau chaude": 2000, "Cuisine": 150, 
    "Linge": 500, "Électronique": 100, "Éclairage": 10, "Pompes": 750, "Autres": 100
}

if connu == "Oui":
    puissance = st.number_input("Puissance (Watts)", min_value=1.0, value=float(default_powers.get(category, 100)))
else:
    puissance = default_powers.get(category, 100)
    st.info(f"Puissance par défaut appliquée pour la catégorie {category} : {puissance} W")

# Bouton de calcul
if st.button("Calculer la consommation"):
    e_jour = (nombre * puissance * heures) / 1000.0  # kWh / jour
    e_mois = e_jour * 30
    e_an = e_jour * 365
    
    st.success("Résultat du calcul énergétique :")
    st.metric("Consommation Journalière", f"{e_jour:.2f} kWh/jour")
    st.metric("Consommation Mensuelle estimée", f"{e_mois:.2f} kWh/mois")
    st.metric("Consommation Annuelle estimée", f"{e_an:.2f} kWh/an")