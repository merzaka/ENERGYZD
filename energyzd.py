import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Plateforme Énergétique Algérie", page_icon="🇩🇿", layout="centered")

# --- STYLE / DÉCORATION THÉMATIQUE (Algérie & EnR) ---
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #006233 0%, #FFFFFF 50%, #D21034 100%);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        color: black;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    <div class="main-header">
        <h2>🇩🇿 Plateforme Intelligente - Efficacité Énergétique & Solaire ☀️</h2>
    </div>
""", unsafe_allow_html=True)

# Initialisation de la mémoire de l'application (Session State)
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'equipments_list' not in st.session_state:
    st.session_state.equipments_list = []

# ==========================================
# ÉTAPE 1 : LOCALISATION & ACCUEIL
# ==========================================
if st.session_state.step == 1:
    st.subheader("📍 Étape 1 : Localisation du Logement")
    
    # Liste des Wilayas principales d'Algérie (exemple)
    wilayas_algerie = [
        "Adrar", "Chlef", "Laghouat", "Oum El Bouaghi", "Batna", "Béjaïa", "Biskra", 
        "Blida", "Bordj Badji Mokhtar", "Bouira", "Tamanrasset", "Tébessa", "Tlemcen", 
        "Tiaret", "Tizi Ouzou", "Alger", "Djelfa", "Jijel", "Sétif", "Saïda", "Skikda", 
        "Sidi Bel Abbès", "Annaba", "Guelma", "Constantine", "Médéa", "Mostaganem", 
        "M'Sila", "Mascara", "Ouargla", "Oran", "El Bayadh", "Illizi", "Bordj Bou Arreridj", 
        "Boumerdès", "El Tarf", "Tindouf", "Tissemsilt", "El Oued", "Khenchela", 
        "Souk Ahras", "Tipaza", "Mila", "Aïn Defla", "Naâma", "Aïn Témouchent", 
        "Ghardaïa", "Relizane", "Timimoun", "Bordj Badji Mokhtar", "Ouled Djellal", 
        "Béni Abbès", "In Salah", "In Guezzam", "Touggourt", "Djanet", "El M'Ghair", "El Meniaa"
    ]
    
    wilaya = st.selectbox("Sélectionnez votre Wilaya", sorted(wilayas_algerie))
    commune = st.text_input("Entrez votre Commune", "Mohammadia")
    
    if st.button("Suivant ➡️"):
        st.session_state.wilaya = wilaya
        st.session_state.commune = commune
        st.session_state.step = 2
        st.rerun()

# ==========================================
# ÉTAPE 2 : CARACTÉRISTIQUES DU LOGEMENT
# ==========================================
elif st.session_state.step == 2:
    st.subheader("🏠 Étape 2 : Caractéristiques Thermiques du Logement")
    
    type_logement = st.selectbox("Type de logement", ["Villa", "Appartement", "Maison traditionnelle"])
    
    col1, col2 = st.columns(2)
    with col1:
        nb_etages = st.number_input("Nombre d'étages", min_value=1, value=1)
    with col2:
        nb_fenetres = st.number_input("Nombre de fenêtres", min_value=1, value=4)
        
    type_vitrage = st.selectbox("Type de vitrage", ["Simple vitrage", "Double vitrage", "Triple vitrage"])
    
    type_toiture = st.selectbox("Type de toiture", ["Terrasse", "Inclinée", "Kermoud (Tuiles rouges)"])
    
    isolation_toiture = st.selectbox("Isolation de la toiture", ["Pas d'isolation", "Isolation standard", "Isolation renforcée"])
    
    col_prev, col_next = st.columns(2)
    with col_prev:
        if st.button("⬅️ Retour"):
            st.session_state.step = 1
            st.rerun()
    with col_next:
        if st.button("Suivant ➡️"):
            st.session_state.step = 3
            st.rerun()

# ==========================================
# ÉTAPE 3 : SAISIE DES ÉQUIPEMENTS (Marché Algérien)
# ==========================================
elif st.session_state.step == 3:
    st.subheader("⚡ Étape 3 : Inventaire des Équipements Électriques")
    
    # Dictionnaire des puissances par défaut par catégorie (en Watts)
    default_powers = {
        "Climatisation": 1200, "Eau chaude": 2000, "Cuisine": 150, 
        "Linge": 500, "Électronique": 100, "Éclairage": 10, "Pompes": 750, "Autres": 100
    }
    
    # Marques courantes sur le marché algérien
    marques_marche = ["Condor", "Iris", "Samsung", "LG", "Brandt", "Beko", "Midea", "TCL", "Stream", "Autre"]
    
    col_cat, col_brand = st.columns(2)
    with col_cat:
        category = st.selectbox("Catégorie", list(default_powers.keys()))
    with col_brand:
        brand = st.selectbox("Marque (Marché Algérien)", marques_marche)
        
    equipment_name = st.text_input("Nom précis de l'équipement", "Climatiseur Split 12000 BTU")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        nombre = st.number_input("Quantité", min_value=1, value=1)
    with col2:
        puissance = st.number_input("Puissance (Watts)", min_value=1.0, value=float(default_powers.get(category, 100)))
    with col3:
        heures = st.number_input("Utilisation (heures/jour)", min_value=0.1, max_value=24.0, value=4.0)
        
    if st.button("➕ Ajouter cet équipement"):
        st.session_state.equipments_list.append({
            "Catégorie": category,
            "Nom": equipment_name,
            "Marque": brand,
            "Quantité": nombre,
            "Puissance (W)": puissance,
            "Heures/jour": heures
        })
        st.success(f"Équipement '{equipment_name}' ajouté avec succès !")
        
    # Affichage du tableau récapitulatif des équipements ajoutés
    if st.session_state.equipments_list:
        st.write("### Équipements déjà enregistrés :")
        df_eq = pd.DataFrame(st.session_state.equipments_list)
        st.dataframe(df_eq, use_container_width=True)
        
    col_prev, col_next = st.columns(2)
    with col_prev:
        if st.button("⬅️ Retour aux caractéristiques"):
            st.session_state.step = 2
            st.rerun()
    with col_next:
        if st.button("Suivant vers l'Objectif ➡️"):
            if not st.session_state.equipments_list:
                st.warning("Veuillez ajouter au moins un équipement avant de continuer.")
            else:
                st.session_state.step = 4
                st.rerun()

# ==========================================
# ÉTAPE 4 : CHOIX FINAL (Estimation / Solaire)
# ==========================================
elif st.session_state.step == 4:
    st.subheader("🎯 Étape 4 : Choisissez votre Objectif")
    
    option = st.radio(
        "Que souhaitez-vous faire ?",
        [
            "1. Estimer et optimiser la consommation énergétique de la maison",
            "2. Dimensionner une installation photovoltaïque (Solaire)"
        ]
    )
    
    if st.button("Lancer l'analyse 🚀"):
        st.success("Analyse en cours de traitement pour votre foyer...")
        
        # Calcul global rapide de la consommation journalière
        total_kwh_jour = sum(
            (eq["Quantité"] * eq["Puissance (W)"] * eq["Heures/jour"]) / 1000.0 
            for eq in st.session_state.equipments_list
        )
        total_kwh_mois = total_kwh_jour * 30
        
        st.metric("Consommation Journalière Totale", f"{total_kwh_jour:.2f} kWh/jour")
        st.metric("Consommation Mensuelle Estimée", f"{total_kwh_mois:.2f} kWh/mois")
        
        if "photovoltaïque" in option:
            st.info("☀️ Recommandation Solaire : Basé sur votre consommation, un système photovoltaïque adapté à votre région en Algérie sera dimensionné lors de la prochaine mise à jour.")
        else:
            st.info("💡 Recommandation d'Optimisation : Des conseils ciblés pour réduire votre facture d'électricité (Sonelgaz) vous seront proposés.")
            
    if st.button("⬅️ Modifier les équipements"):
        st.session_state.step = 3
        st.rerun()
