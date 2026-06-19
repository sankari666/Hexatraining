# Databricks notebook source
flights_df = spark.read.format("delta") \
.load("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/flights")

bookings_df = spark.read.format("delta") \
.load("/Volumes/hexa_databrick_7405614050819600/default/hexa-volume/bookings")

# COMMAND ----------

flights_df.show()

bookings_df.show()

# COMMAND ----------

airline_df = bookings_df.join(
    flights_df,
    on="flight_id",
    how="inner"
)

airline_df.show()

# COMMAND ----------

import matplotlib.pyplot as plt

# COMMAND ----------

from pyspark.sql.functions import col

bookings_df = bookings_df.withColumn(
    "ticket_price",
    col("ticket_price").cast("double")
)

bookings_df.printSchema()

# COMMAND ----------

revenue_airline = airline_df.groupBy("airline") \
.sum("ticket_price") \
.toPandas()

plt.figure(figsize=(8,5))

plt.bar(
    revenue_airline["airline"],
    revenue_airline["sum(ticket_price)"]
)

plt.title("Revenue by Airline")
plt.xlabel("Airline")
plt.ylabel("Revenue")

plt.show()

# COMMAND ----------

travel_class_df = bookings_df.groupBy(
    "travel_class"
).sum(
    "ticket_price"
).toPandas()

plt.figure(figsize=(6,6))

plt.pie(
    travel_class_df["sum(ticket_price)"],
    labels=travel_class_df["travel_class"],
    autopct="%1.1f%%"
)

plt.title("Revenue by Travel Class")

plt.show()

# COMMAND ----------

status_df = flights_df.groupBy(
    "status"
).count().toPandas()

plt.figure(figsize=(6,6))

plt.pie(
    status_df["count"],
    labels=status_df["status"],
    autopct="%1.1f%%"
)

plt.title("Flights by Status")

plt.show()

# COMMAND ----------

from pyspark.sql.functions import concat_ws

routes_df = flights_df.withColumn(
    "route",
    concat_ws(
        " -> ",
        flights_df.from_city,
        flights_df.to_city
    )
)

top_routes = routes_df.groupBy(
    "route"
).count().toPandas()

plt.figure(figsize=(10,6))

plt.barh(
    top_routes["route"],
    top_routes["count"]
)

plt.title("Top Routes")
plt.xlabel("Number of Flights")
plt.ylabel("Route")

plt.show()

# COMMAND ----------

ticket_df = bookings_df.toPandas()

plt.figure(figsize=(8,5))

plt.scatter(
    ticket_df.index,
    ticket_df["ticket_price"]
)

plt.title("Ticket Price Distribution")
plt.xlabel("Booking Number")
plt.ylabel("Ticket Price")

plt.show()

# COMMAND ----------

