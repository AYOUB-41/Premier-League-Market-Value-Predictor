import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. CHARGEMENT (D'abord charger les fichiers !)
model_rl = joblib.load('models/modele_rl.pkl')
model_rf = joblib.load('models/modele_rf.pkl')
scaler = joblib.load('models/scaler_stats.pkl')

# 2. RÉCUPÉRATION DES COLONNES (Indispensable pour éviter l'erreur "Feature names")
features_entrainement = scaler.feature_names_in_

# 3. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Predicteur de Prix PL", page_icon="⚽")
st.title("⚽ Estimation de Valeur Marchande - Premier League")

# 4. BARRE LATÉRALE
st.sidebar.header("Configuration")
modele_choisi = st.sidebar.radio("Choisir le modèle d'IA", ("Régression Linéaire", "Random Forest"))

st.sidebar.divider()
st.sidebar.header("Statistiques du Joueur")
nom = st.sidebar.text_input("Nom du joueur", "Joueur X")

# IMPORTANT : Ajoutez le choix du Club car votre modèle a été entraîné avec !
club_choisi = st.sidebar.selectbox("Club", [
    "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", 
    "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich Town",
    "Leicester City", "Liverpool", "Manchester City", "Manchester Utd", 
    "Newcastle Utd", "Nott'm Forest", "Southampton", "Tottenham", "West Ham", "Wolves"
])

poste_choisi = st.sidebar.selectbox("Poste", ["Attaquand", "Milieu", "Défenseur"]) # Vérifiez l'orthographe exacte dans votre dataset
buts = st.sidebar.slider("Buts", 0, 40, 5)
assists = st.sidebar.slider("Passes décisives", 0, 30, 3)
mins = st.sidebar.slider("Minutes jouées", 0, 3420, 1200)
tacles = st.sidebar.slider("Tacles", 0, 100, 10)

# 5. PRÉPARATION DES DONNÉES (Le "Fix" pour l'erreur de colonnes)
if st.button("Calculer la Valeur"):
    # On crée un tableau vide avec TOUTES les colonnes que le scaler attend
    input_df = pd.DataFrame(0, index=[0], columns=features_entrainement)
    
    # On remplit les colonnes numériques
    input_df['Goals'] = buts
    input_df['Assists'] = assists
    input_df['Minutes'] = mins
    input_df['Tackles'] = tacles
    
    # On active la colonne du club et du poste (One-Hot Encoding)
    col_club = f"Club_{club_choisi}"
    col_pos = f"Position_{poste_choisi}"
    
    if col_club in input_df.columns:
        input_df[col_club] = 1
    if col_pos in input_df.columns:
        input_df[col_pos] = 1

    # 6. PRÉDICTION
    input_scaled = scaler.transform(input_df)
    
    if modele_choisi == "Régression Linéaire":
        prediction = model_rl.predict(input_scaled)
    else:
        prediction = model_rf.predict(input_scaled)
    
    # Affichage
    resultat = max(0, prediction[0])
    st.success(f"💰 Valeur estimée pour {nom} : {resultat:.2f} M€")