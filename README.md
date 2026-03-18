# ⚽ Premier League Market Value Predictor (2024/2025)

Ce projet est un **Système Intelligent** conçu pour estimer la valeur marchande des joueurs de la Premier League anglaise pour la saison 2024/2025. Il combine l'analyse de données (Data Science) et le déploiement d'une interface interactive (Streamlit).

## 📊 Aperçu du Projet
L'objectif est de fournir une estimation financière basée sur les performances réelles des joueurs. Le système traite des données brutes, les normalise et utilise des modèles de Machine Learning pour prédire le prix de marché.

### Fonctionnalités clés :
- **Prétraitement automatisé** : Encodage des clubs/postes et mise à l'échelle des données (Scaling).
- **Double Modélisation** : Comparaison entre la **Régression Linéaire** et le **Random Forest**.
- **Interface Interactive** : Ajustement en temps réel des statistiques (Buts, Passes, Minutes) pour voir l'impact sur le prix.

## 🛠️ Installation et Utilisation Locale

### 1. Prérequis
Assurez-vous d'avoir Python installé. Il est fortement recommandé d'utiliser un environnement virtuel `.venv` pour éviter les conflits de bibliothèque.

### 2. Installation
Clonez le dépôt et installez les dépendances nécessaires :
```bash
git clone [https://github.com/AYOUB-41/Premier-League-Market-Value-Predictor.git](https://github.com/AYOUB-41/Premier-League-Market-Value-Predictor.git)
cd Premier-League-Market-Value-Predictor
pip install -r requirements.txt
```
### 3. Lancement de l'application
Exécutez la commande suivante pour ouvrir l'interface dans votre navigateur :
```bash
streamlit run App.py
```
## 📂 Structure du Dépôt
- App.py : Le code source de l'interface utilisateur Streamlit.

- Mini-projet_... .ipynb : Notebook Jupyter contenant l'exploration des données (EDA) et l'entraînement des modèles.

- epl_player_stats_24_25.csv : Le dataset utilisé pour l'entraînement.

- *.pkl : Les fichiers sérialisés des modèles et du scaler pour une utilisation immédiate.

- rapport_valeur_marchande.pdf : Documentation détaillée du projet.
## 🧪 Modèles et Performances
- Régression Linéaire : A montré une excellente capacité à capturer la logique proportionnelle du dataset.

- Random Forest : Offre une approche robuste basée sur des arbres de décision pour gérer les relations non-linéaires.
## 👤 Auteur
Ayoub ZOUITINE Étudiant en Systèmes Intelligents (2025-2026)
Encadré par : M. Tarek AIT BAHA
