# Databricks notebook source
analytics_df = spark.read.format("delta").load(
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/final_airline_analytics"
)

analytics_df.show()

# COMMAND ----------

analytics_df.write \
.mode("overwrite") \
.format("delta") \
.save("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/delta_airline")

# COMMAND ----------

delta_df = spark.read.format("delta").load(
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/delta_airline"
)

delta_df.show()

# COMMAND ----------

from delta.tables import DeltaTable

delta_table = DeltaTable.forPath(
    spark,
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/delta_airline"
)

delta_table.history().show(truncate=False)

# COMMAND ----------

from delta.tables import DeltaTable

delta_table = DeltaTable.forPath(
    spark,
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/delta_airline"
)

delta_table.update(
    condition="price_band = 'Budget'",
    set={"price_band":"'Economy'"}
)

# COMMAND ----------

spark.read.format("delta") \
.load("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/delta_airline") \
.show()

# COMMAND ----------

version0 = spark.read \
.format("delta") \
.option("versionAsOf",0) \
.load("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/delta_airline")

version0.show()

# COMMAND ----------

version0 = spark.read \
.format("delta") \
.option("versionAsOf",0) \
.load("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/delta_airline")

version0.show()

# COMMAND ----------

spark.sql("""
OPTIMIZE delta.`/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/delta_airline`
""")