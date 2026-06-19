# Databricks notebook source
flights_df = spark.read \
.option("header","true") \
.option("inferSchema","true") \
.option("delimiter",",") \
.csv("/Workspace/Users/azuser7228_mml.local@karthikirisoutlook.onmicrosoft.com/Flights.csv")

flights_df.show()
flights_df.printSchema()

flights_df.show()

# COMMAND ----------

from pyspark.sql.functions import split

flights_fixed = flights_df.select(
    split(
        flights_df.columns[0],
        ","
    ).alias("data")
)

flights_fixed = flights_fixed.select(
    flights_fixed.data[0].alias("flight_id"),
    flights_fixed.data[1].alias("airline"),
    flights_fixed.data[2].alias("from_city"),
    flights_fixed.data[3].alias("to_city"),
    flights_fixed.data[4].alias("duration"),
    flights_fixed.data[5].alias("status")
)

flights_fixed.show(truncate=False)
flights_fixed.printSchema()

# COMMAND ----------

flights_fixed.write \
.mode("overwrite") \
.format("delta") \
.save("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/flights")

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume"))

# COMMAND ----------

spark.read.format("delta") \
.load("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/flights") \
.show()

# COMMAND ----------

bookings_df.printSchema()