# 🏆 Databricks Pipeline : Analyse de Performance 360° (UEFA Champions League)

[![Databricks](https://shields.io)](https://databricks.com)
[![Apache Spark](https://shields.io)](https://apache.org)
[![Delta Lake](https://shields.io)](https://delta.io)
[![Python](https://shields.io)](https://python.org)

## 📝 Présentation du Projet
Ce projet consiste en la conception et le déploiement d'un **pipeline de données End-to-End** sur l'architecture Cloud **Databricks**, analysant les performances de la phase de ligue de la Ligue des Champions (UEFA). 

L'objectif est d'extraire des données de matchs brutes, d'appliquer des règles de nettoyage rigoureuses (*Data Quality*), de calculer des indicateurs de performance clés (KPIs) complexes et de générer une cartographie analytique prête pour des présentations exécutives ou des outils de Business Intelligence (Power BI / Tableau).

---

## 📐 Architecture Technique

Le projet respecte l'**Architecture Medallion (Bronze ➜ Silver ➜ Gold)**, standard de l'industrie pour garantir la traçabilité et la qualité de la donnée au sein d'un **Data Lakehouse** :

```text
[Données Brutes] ➜  🟫 COUCHE BRONZE : Ingestion & Stockage brut
                 ➜  ⬜ COUCHE SILVER : Nettoyage (F.trim), Harmonisation & Règles métiers
                 ➜  🟨 COUCHE GOLD   : Agrégation, Feature Engineering (Ratios) & Classement
                 ➜  💾 STOCKAGE      : Table Delta Lake (Unity Catalog Compliant)
                 ➜  📊 COMPORTEMENT  : Visualisation de production (Seaborn PNG local embedded)
```

### ⚙️ Choix d'ingénierie et Optimisations (Production-Ready)
* **Compatibilité Databricks Serverless (Spark Connect) :** L'usage classique des fenêtres globales distribuées (`Window.orderBy`) sur des clusters Serverless déclenche de lourdes alertes d'exécution et dégrade la mémoire. Ce pipeline résout cette contrainte en utilisant l'API **`mapInPandas`** pour déléguer l'indexation du classement de manière fluide et parallélisée.
* **Zéro Dépendance RDD :** Le code exclut totalement les RDDs bas niveau (interdits sur les architectures Serverless modernes), s'assurant ainsi d'être exécutable sur n'importe quel espace de travail Cloud récent.
* **Gouvernance de Données (Unity Catalog) :** L'écriture finale est configurée pour utiliser les catalogues dynamiques de sessions, évitant l'ancien méta-store Hive obsolète (`hive_metastore`).
* **Intégration Continue GitHub :** La couche visuelle est développée avec **Seaborn/Matplotlib** et nettoyée des glyphes/emojis complexes. Le rendu graphique s'inscrit nativement au format PNG au cœur du Notebook `.ipynb`, garantissant un affichage instantané et parfait lors de la navigation sur GitHub.

---

## 📊 Indicateurs Analytiques Calculés (Couche Gold)

Le modèle de données final expose un audit de performance complet à travers les métriques suivantes :
* **Win_Rate_% :** Taux de victoire réel calculé selon le prorata des matchs joués.
* **Goals_Scored_Avg :** Efficacité offensive (Moyenne de buts marqués par match).
* **Goals_Conceded_Avg :** Solidité/Fragilité défensive (Moyenne de buts encaissés par match).
* **Goal_Diff :** Différence de buts brute, alignée sur les critères officiels de bris d'égalité de l'UEFA.
* **Status :** Segmentation automatique et dynamique des équipes (*Top 8 Direct, Playoffs, Eliminated*).

---

## 🛠️ Instructions d'Installation et Déploiement

### Prérequis
* Un espace de travail **Databricks** (Community ou Enterprise).
* Un cluster configuré avec **Runtime 15.4 LTS ou supérieur** (Python 3.12+).

### Déploiement du Pipeline
1. Clonez ce dépôt ou téléchargez le fichier `Notebook.ipynb`.
2. Importez le fichier au sein de votre espace de travail Databricks Workspace.
3. Attachez le notebook à votre cluster de calcul (Serverless ou Dédié).
4. Cliquez sur **Run All** (Exécuter tout).

Le script gère automatiquement l'installation de la bibliothèque graphique requise (`%pip install seaborn --quiet`) de manière isolée pour votre session.

---

## 🚀 Impact Métier / Restitution
À la fin de l'exécution, le pipeline écrit de manière permanente les résultats au format **Delta Lake** sous le nom de table `ucl_analytics_dashboard`. Cette table présente un jeu de données parfaitement consolidé à **36 lignes uniques**, prêt pour :
1. Être requêté directement par les analystes métiers via des cellules **Spark SQL**.
2. Alimenter un tableau de bord exécutif automatisé sur **Power BI** ou **Tableau Software** via le connecteur natif Databricks.
