from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_bill_file():

    data = """Rahul,210
Priya,180
Amit,300
Sneha,150
Kiran,260"""

    with open("/tmp/electricity.txt","w") as f:
        f.write(data)

def calculate_total_units():

    total = 0
    count = 0

    with open("/tmp/electricity.txt","r") as f:

        for line in f:

            name, units = line.strip().split(",")

            total += int(units)
            count += 1

    average = total / count

    with open("/tmp/bill_data.txt","w") as f:
        f.write(f"{count},{total},{average}")

def generate_bill_summary():

    with open("/tmp/bill_data.txt","r") as f:

        count,total,average = f.read().split(",")

    report = f"""
Electricity Bill Summary

Customers = {count}
Total Units = {total}
Average Units = {average}
"""

    print(report)

    with open("/tmp/bill_summary.txt","w") as f:
        f.write(report)

with DAG(
    dag_id="exercise8_electricity_bill",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_bill_file",
        python_callable=create_bill_file
    )

    task2 = PythonOperator(
        task_id="calculate_total_units",
        python_callable=calculate_total_units
    )

    task3 = PythonOperator(
        task_id="generate_bill_summary",
        python_callable=generate_bill_summary
    )

    task1 >> task2 >> task3
