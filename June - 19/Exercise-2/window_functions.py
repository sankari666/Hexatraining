# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.window import Window

flights_df = spark.read.format("delta").load(
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/silver_flights"
)

bookings_df = spark.read.format("delta").load(
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/silver_bookings"
)

# COMMAND ----------

airline_df = bookings_df.join(
    flights_df,
    on="flight_id",
    how="inner"
)

airline_df.show()

# COMMAND ----------

price_window = Window.orderBy(
    col("ticket_price").desc()
)

rank_df = airline_df.withColumn(
    "rank",
    rank().over(price_window)
)

rank_df.select(
    "passenger_name",
    "ticket_price",
    "rank"
).show()

# COMMAND ----------

dense_rank_df = airline_df.withColumn(
    "dense_rank",
    dense_rank().over(price_window)
)

dense_rank_df.select(
    "passenger_name",
    "ticket_price",
    "dense_rank"
).show()

# COMMAND ----------

row_df = airline_df.withColumn(
    "row_num",
    row_number().over(price_window)
)

row_df.select(
    "passenger_name",
    "ticket_price",
    "row_num"
).show()

# COMMAND ----------

revenue_window = Window.orderBy(
    "booking_date"
)

running_total_df = airline_df.withColumn(
    "running_revenue",
    sum("revenue").over(revenue_window)
)

running_total_df.select(
    "booking_date",
    "revenue",
    "running_revenue"
).show()

# COMMAND ----------

class_window = Window.partitionBy(
    "travel_class"
).orderBy(
    col("ticket_price").desc()
)

top_passengers = airline_df.withColumn(
    "row_num",
    row_number().over(class_window)
)

top_passengers.filter(
    col("row_num") <= 3
).select(
    "travel_class",
    "passenger_name",
    "ticket_price",
    "row_num"
).show()

# COMMAND ----------

airline_revenue = airline_df.groupBy(
    "airline"
).agg(
    sum("revenue").alias("total_revenue")
)

airline_window = Window.orderBy(
    col("total_revenue").desc()
)

airline_rank = airline_revenue.withColumn(
    "rank",
    rank().over(airline_window)
)

airline_rank.show()

# COMMAND ----------

airline_price_window = Window.partitionBy(
    "airline"
).orderBy(
    col("ticket_price").desc()
)

highest_ticket = airline_df.withColumn(
    "row_num",
    row_number().over(airline_price_window)
)

highest_ticket.filter(
    col("row_num") == 1
).show()

# COMMAND ----------

airline_price_window = Window.partitionBy(
    "airline"
).orderBy(
    col("ticket_price").desc()
)

highest_ticket = airline_df.withColumn(
    "row_num",
    row_number().over(airline_price_window)
)

highest_ticket.filter(
    col("row_num") == 1
).show()

# COMMAND ----------

airline_df.write \
.mode("overwrite") \
.format("delta") \
.save("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/final_airline_analytics")

# COMMAND ----------

spark.read.format("delta").load(
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/final_airline_analytics"
).show()