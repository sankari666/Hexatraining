# Databricks notebook source
from pyspark.sql.functions import *

flights_df = spark.read.format("delta").load(
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/silver_flights"
)

bookings_df = spark.read.format("delta").load(
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/silver_bookings"
)

# COMMAND ----------

airline_report_df = bookings_df.join(
    flights_df,
    on="flight_id",
    how="inner"
)

airline_report_df.show()

# COMMAND ----------

airline_revenue = airline_report_df.groupBy(
    "airline"
).agg(
    sum("revenue").alias("total_revenue")
)

airline_revenue.show()

airline_revenue.orderBy(
    col("total_revenue").desc()
).show()

# COMMAND ----------

delayed_flights = airline_report_df.filter(
    col("delay_flag") == "Yes"
)

delayed_flights.show()

# COMMAND ----------

premium_passengers = airline_report_df.filter(
    col("price_band") == "Premium"
)

premium_passengers.show()

print(
    premium_passengers.count()
)

# COMMAND ----------

travel_class_revenue = airline_report_df.groupBy(
    "travel_class"
).agg(
    sum("revenue").alias("total_revenue")
)

travel_class_revenue.show()

# COMMAND ----------

airline_passenger_count = airline_report_df.groupBy(
    "airline"
).agg(
    count("passenger_name").alias("passenger_count")
)

airline_passenger_count.show()

# COMMAND ----------

airline_revenue.write \
.mode("overwrite") \
.format("delta") \
.save("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/gold_airline_revenue")

# COMMAND ----------

delayed_flights.write \
.mode("overwrite") \
.format("delta") \
.save("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/gold_delayed_flights")

# COMMAND ----------

display(
    spark.read.format("delta").load(
        "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/gold_airline_revenue"
    )
)