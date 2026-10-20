# 🇪🇺 Analyse et Simulation de la UEFA Champions League 2026/2027

### 👨‍💻 Développé par : **Moussa H. (@hmaroum-dotcom)**

Ce projet de Data Analysis, développé intégralement sur **Databricks**, propose un pipeline complet d'ingestion, de traitement et de visualisation des données pour le **nouveau format de la Ligue des Champions** (Phase de Ligue unique à 36 équipes).

---

## 🚀 Objectifs du Projet
* **Ingérer et centraliser** les résultats de matchs au format de données distribuées.
* **Calculer dynamiquement le classement** global selon les critères stcrits de l'UEFA (Points, Différence de buts, Meilleure attaque).
* **Segmenter automatiquement les équipes** selon leur destin dans la compétition (Top 8 Qualifiés, Barragistes, Éliminés).
* **Visualiser la hiérarchie** des clubs via des tableaux de bord interactifs.

---

## 🛠️ Stack Technique
* **Plateforme :** Databricks (Espace de travail collaboratif, Lakehouse architecture)
* **Moteur de calcul :** PySpark / Apache Spark (DataFrames API, Fonctions de fenêtrage avancées)
* **Gestion de versions :** Intégration Git native avec l'application GitHub Databricks
* **Visualisation :** Databricks Native Visualizations (Graphiques en barres dynamiques avec groupements logiques)

---

## 📂 Structure du Pipeline (Notebook)

Le projet s'articule autour de 3 étapes clés au sein du même pipeline de données :

1. **Ingestion & Data Cleansing :** Chargement des scores bruts, calcul des résultats (Victoire/Nul/Défaite) et attribution des points (3, 1, 0) distinctement pour les équipes à domicile et à l'extérieur.
2. **Agrégation du Classement :** Utilisation des fonctions Spark `union` et `groupBy` pour consolider les performances globales des 36 clubs européens.
3. **Analyse de Performance (Window Functions) :** Application de `Window.partitionBy().orderBy()` pour privilégier l'exécution optimisée du cluster, suivi d'un enrichissement de données (`uefa_status`) pour cartographier la qualification.

---

## 📊 Aperçu des Résultats Visuels

L'analyse permet de générer des graphiques en barres épurés où :
* Les clubs sont triés de manière rigoureuse selon les règles de l'UEFA.
* Les barres disposent d'un codage couleur selon leur statut (`🟢 Qualifié`, `🟡 Barragiste`, `🔴 Éliminé`).
* Le volume de buts et de points est directement inspectable via des étiquettes de données intégrées.

---

## ⚙️ Comment exécuter ce projet ?
1. Clonez ce dépôt dans votre espace de travail Databricks via les **Git Folders**.
2. Créez ou connectez un cluster d'exécution (compatible avec l'offre gratuite Databricks Community Edition).
3. Ouvrez le notebook et cliquez sur **Run All** (Tout exécuter).

---

## 📬 Contact
* **GitHub :** [@hmaroum-dotcom](https://github.com)
