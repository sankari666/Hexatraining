# Databricks notebook source
bookings_df = spark.read \
.option("header","true") \
.option("inferSchema","true") \
.option("delimiter",",") \
.csv("/Workspace/Users/azuser7228_mml.local@karthikirisoutlook.onmicrosoft.com/bookings.csv - Sheet1.csv")

bookings_df.show()
bookings_df.printSchema()

# COMMAND ----------

bookings_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import split

bookings_fixed = bookings_df.select(
    split(bookings_df.columns[0], ",").alias("data")
)

bookings_fixed = bookings_fixed.select(
    bookings_fixed.data[0].alias("booking_id"),
    bookings_fixed.data[1].alias("flight_id"),
    bookings_fixed.data[2].alias("passenger_name"),
    bookings_fixed.data[3].alias("travel_class"),
    bookings_fixed.data[4].alias("ticket_price"),
    bookings_fixed.data[5].alias("booking_date")
)

bookings_fixed.show(truncate=False)
bookings_fixed.printSchema()

# COMMAND ----------

bookings_fixed.write \
.mode("overwrite") \
.format("delta") \
.save("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/bookings")

# COMMAND ----------

spark.read.format("delta") \
.load("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/bookings") \
.show()

# COMMAND ----------

bookings_df.printSchema()