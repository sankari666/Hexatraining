from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv

def create_orders():

    with open("/tmp/orders.csv","w",newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["product","quantity","price"])

        writer.writerow(["Laptop",1,70000])
        writer.writerow(["Mouse",4,500])
        writer.writerow(["Monitor",2,12000])
        writer.writerow(["Keyboard",3,1500])

def calculate_order_value():

    total_revenue = 0
    highest_product = ""
    highest_revenue = 0

    report_lines = []

    with open("/tmp/orders.csv","r") as f:

        reader = csv.DictReader(f)

        for row in reader:

            revenue = (
                int(row["quantity"])
                *
                int(row["price"])
            )

            report_lines.append(
                f'{row["product"]} = {revenue}'
            )

            total_revenue += revenue

            if revenue > highest_revenue:
                highest_revenue = revenue
                highest_product = row["product"]

    with open("/tmp/sales_data.txt","w") as f:

        f.write("\n".join(report_lines))
        f.write(f"\nTOTAL={total_revenue}")
        f.write(f"\nTOP={highest_product}")

def generate_sales_report():

    with open("/tmp/sales_data.txt","r") as f:

        data = f.readlines()

    print("Sales Report")
    print("")

    for line in data:
        print(line.strip())

with DAG(
    dag_id="exercise10_online_orders",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_orders",
        python_callable=create_orders
    )

    task2 = PythonOperator(
        task_id="calculate_order_value",
        python_callable=calculate_order_value
    )

    task3 = PythonOperator(
        task_id="generate_sales_report",
        python_callable=generate_sales_report
    )

    task1 >> task2 >> task3
