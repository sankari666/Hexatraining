# Databricks notebook source
preferences_df = spark.read \
.option("multiline","true") \
.json("/Workspace/Users/azuser7228_mml.local@karthikirisoutlook.onmicrosoft.com/Drafts/passenger_preferences.json")

preferences_df.show()
preferences_df.printSchema()

# COMMAND ----------

preferences_flat_df = preferences_df.select(
    "passenger_name",
    "meal",
    "seat"
)

preferences_flat_df.show()

# COMMAND ----------

preferences_flat_df.write \
.mode("overwrite") \
.format("delta") \
.save("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/preferences")

# COMMAND ----------

spark.read.format("delta") \
.load("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/preferences") \
.show()