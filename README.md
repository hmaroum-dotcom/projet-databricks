# 🇪🇺 UEFA Champions League 2026/2027 Analysis & Simulation

### 👨‍💻 AUTHOR / AUTEUR
**Moussa H. (@hmaroum-dotcom)**

---

### 🎯 PROJECT OVERVIEW / PRÉSENTATION DU PROJET
* **EN:** This Data Analysis project, built entirely on **Databricks**, delivers an end-to-end data pipeline for ingestion, processing, and visualization tailored to the **new UEFA Champions League single-league format** (36-team single table).
* **FR:** Ce projet d'analyse de données, entièrement développé sur **Databricks**, propose un pipeline complet d'ingestion, de traitement et de visualisation adapté au **nouveau format de la Ligue des Champions** (Phase de Ligue unique à 36 équipes).

---

### 💡 CORE OBJECTIVES / OBJECTIFS CLÉS
* **EN:** Ingest, centralize, and dynamically compute global standings according to strict UEFA tie-breaking rules (Points, Goal Difference, Goals Scored).
* **EN:** Automatically segment teams based on tournament outcomes (Top 8, Play-offs, Eliminated) and analyze club offensive efficiency.
* **FR:** Ingérer, centraliser et calculer dynamiquement le classement global selon les critères stricts de l'UEFA (Points, Différence de buts, Buts marqués).
* **FR:** Segmenter automatiquement les équipes selon leur destin (Top 8, Barrages, Éliminés) et analyser l'efficacité offensive des clubs.

---

### 💻 TECHNOLOGIES USED / TECHNOLOGIES UTILISÉES
* **Platform / Plateforme :** Databricks (Collaborative Workspace, Lakehouse Architecture)
* **Compute Engine / Moteur :** PySpark / Apache Spark (DataFrames API, Advanced Window Functions)
* **Version Control / Gestion de versions :** Native Git Integration (Databricks GitHub App)
* **Visualization / Visualisation :** Databricks Native Visualizations (Color-coded dashboards)

---

### ⚙️ DATA PIPELINE DESIGN / ARCHITECTURE DU PIPELINE

1. **Ingestion & Data Cleansing (EN/FR):** 
   * *EN:* Loading raw scores and allocating points (3, 1, 0) accurately for both home and away fixtures.
   * *FR:* Chargement des scores bruts et attribution des points (3, 1, 0) pour les matchs à domicile et à l'extérieur.
2. **Standings Aggregation (EN/FR):** 
   * *EN:* Leveraging Spark's `union` and `groupBy` operators to compile consolidated stats for all 36 clubs.
   * *FR:* Utilisation des fonctions Spark `union` et `groupBy` pour consolider les statistiques des 36 clubs.
3. **Advanced Analytics (EN/FR):** 
   * *EN:* Implementing cluster-optimized `Window` functions to generate precise league rankings and map qualification tiers (`UEFA_Status`).
   * *FR:* Application de fonctions de fenêtrage (`Window`) optimisées pour générer le rang officiel et cartographier le statut de qualification.
4. **Efficiency Metrics (EN/FR):** 
   * *EN:* Computing goals-per-match ratios (`Offensive_Efficiency`) rounded to two decimals to isolate clinical teams.
   * *FR:* Calcul du ratio de buts par match (`Efficacité_Offensive`) arrondi à deux décimales pour identifier les attaques les plus réalistes.

---

### 📊 METRICS & VISUALIZATIONS / INDICATEURS & VISUALISATIONS
* **EN:** Interactive bar charts with specific status group coloring (`🟢 Qualified`, `🟡 Knockout Play-offs`, `🔴 Eliminated`) and integrated data value labels for clean metric scanning.
* **FR:** Graphiques en barres interactifs avec un codage couleur par statut (`🟢 Qualifié`, `🟡 Barragiste`, `🔴 Éliminé`) et étiquettes de données intégrées pour une lecture immédiate des indicateurs.

---

### 🚀 RUNNING THE CODE / EXÉCUTION DU PROJET
1. **EN:** Clone this repository into your Databricks workspace using **Git Folders**. Attach a cluster (fully compatible with Databricks Community Edition) and click **Run All**.
2. **FR:** Clonez ce dépôt dans votre espace Databricks via les **Git Folders**. Connectez un cluster (compatible avec l'édition gratuite Community) et cliquez sur **Tout exécuter**.

---

### 📬 GET IN TOUCH / CONTACT
* **GitHub:** [@hmaroum-dotcom](https://github.com)
