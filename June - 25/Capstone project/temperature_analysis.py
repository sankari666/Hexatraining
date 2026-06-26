from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_temperature_file():

    data = """Monday,34
Tuesday,36
Wednesday,31
Thursday,38
Friday,35
Saturday,33
Sunday,32"""

    with open("/tmp/temperature.txt","w") as f:
        f.write(data)

def find_highest_temperature():

    temperatures = []

    with open("/tmp/temperature.txt","r") as f:

        for line in f:

            day,temp = line.strip().split(",")

            temperatures.append(int(temp))

    highest = max(temperatures)
    average = sum(temperatures) / len(temperatures)

    with open("/tmp/weather_data.txt","w") as f:
        f.write(f"{highest},{average}")

def generate_weather_report():

    with open("/tmp/weather_data.txt","r") as f:

        highest,average = f.read().split(",")

    report = f"""
Weather Report

Highest Temperature = {highest}
Average Temperature = {average}
"""

    print(report)

    with open("/tmp/weather_report.txt","w") as f:
        f.write(report)

with DAG(
    dag_id="exercise11_temperature_analysis",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_temperature_file",
        python_callable=create_temperature_file
    )

    task2 = PythonOperator(
        task_id="find_highest_temperature",
        python_callable=find_highest_temperature
    )

    task3 = PythonOperator(
        task_id="generate_weather_report",
        python_callable=generate_weather_report
    )

    task1 >> task2 >> task3
