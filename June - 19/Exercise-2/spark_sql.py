# Databricks notebook source
flights_df = spark.read.format("delta").load(
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/silver_flights"
)

bookings_df = spark.read.format("delta").load(
    "/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/silver_bookings"
)

# COMMAND ----------

flights_df.createOrReplaceTempView("flights")

bookings_df.createOrReplaceTempView("bookings")

# COMMAND ----------

spark.sql("""
SELECT *
FROM flights
""").show()

# COMMAND ----------

spark.sql("""
SELECT *
FROM bookings
""").show()

# COMMAND ----------

spark.sql("""
SELECT
SUM(revenue) AS total_revenue
FROM bookings
""").show()

# COMMAND ----------

spark.sql("""
SELECT
travel_class,
SUM(revenue) AS total_revenue
FROM bookings
GROUP BY travel_class
ORDER BY total_revenue DESC
""").show()

# COMMAND ----------

spark.sql("""
SELECT
flight_id,
airline,
status
FROM flights
WHERE delay_flag='Yes'
""").show()

# COMMAND ----------

spark.sql("""
SELECT
b.passenger_name,
f.airline,
b.travel_class,
b.revenue
FROM bookings b
INNER JOIN flights f
ON b.flight_id=f.flight_id
""").show()

# COMMAND ----------

spark.sql("""
SELECT
f.airline,
SUM(b.revenue) AS total_revenue
FROM bookings b
INNER JOIN flights f
ON b.flight_id=f.flight_id
GROUP BY f.airline
ORDER BY total_revenue DESC
""").show()

# COMMAND ----------

spark.sql("""
SELECT
AVG(ticket_price) AS average_ticket_price
FROM bookings
""").show()