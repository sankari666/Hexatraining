from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_employee_file():

    data = """Rahul,28
Priya,31
Amit,42
Sneha,26
Kiran,38"""

    with open("/tmp/employees.txt","w") as f:
        f.write(data)

def calculate_average_age():

    ages = []

    with open("/tmp/employees.txt","r") as f:

        for line in f:

            name, age = line.strip().split(",")

            ages.append(int(age))

    youngest = min(ages)
    oldest = max(ages)
    average = sum(ages) / len(ages)

    with open("/tmp/age_data.txt","w") as f:
        f.write(f"{youngest},{oldest},{average}")

def generate_age_report():

    with open("/tmp/age_data.txt","r") as f:

        youngest, oldest, average = f.read().split(",")

    report = f"""
Employee Age Report

Youngest Employee = {youngest}
Oldest Employee = {oldest}
Average Age = {average}
"""

    print(report)

with DAG(
    dag_id="exercise13_employee_age",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_employee_file",
        python_callable=create_employee_file
    )

    task2 = PythonOperator(
        task_id="calculate_average_age",
        python_callable=calculate_average_age
    )

    task3 = PythonOperator(
        task_id="generate_age_report",
        python_callable=generate_age_report
    )

    task1 >> task2 >> task3
