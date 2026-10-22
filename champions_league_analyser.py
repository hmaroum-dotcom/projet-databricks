from pyspark.sql import functions as F

def calculer_points(df_matches):
    """Calcule les points à domicile et à l'extérieur selon les scores."""
    return df_matches.withColumn(
        "home_points", 
        F.when(F.col("home_goals") > F.col("away_goals"), 3)
         .when(F.col("home_goals") == F.col("away_goals"), 1)
         .otherwise(0)
    ).withColumn(
        "away_points",
        F.when(F.col("away_goals") > F.col("home_goals"), 3)
         .when(F.col("away_goals") == F.col("home_goals"), 1)
         .otherwise(0)
    )
