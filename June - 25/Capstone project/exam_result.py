from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_result_file():

    data = """Rahul,Pass
Priya,Fail
Amit,Pass
Sneha,Pass
Kiran,Fail
Megha,Pass"""

    with open("/tmp/results.txt","w") as f:
        f.write(data)

def count_pass_fail():

    passed = 0
    failed = 0

    with open("/tmp/results.txt","r") as f:

        for line in f:

            name,result = line.strip().split(",")

            if result == "Pass":
                passed += 1
            else:
                failed += 1

    with open("/tmp/result_count.txt","w") as f:
        f.write(f"{passed},{failed}")

def generate_result_summary():

    with open("/tmp/result_count.txt","r") as f:

        passed,failed = f.read().split(",")

    report = f"""
Exam Result Summary

Total Pass = {passed}
Total Fail = {failed}
"""

    print(report)

    with open("/tmp/result_summary.txt","w") as f:
        f.write(report)

with DAG(
    dag_id="exercise9_exam_result",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_result_file",
        python_callable=create_result_file
    )

    task2 = PythonOperator(
        task_id="count_pass_fail",
        python_callable=count_pass_fail
    )

    task3 = PythonOperator(
        task_id="generate_result_summary",
        python_callable=generate_result_summary
    )

    task1 >> task2 >> task3
