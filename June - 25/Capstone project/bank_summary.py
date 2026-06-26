from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_transactions():

    data = """Deposit,10000
Withdraw,2500
Deposit,4000
Withdraw,1500
Deposit,2000"""

    with open("/tmp/transactions.txt","w") as f:
        f.write(data)

def calculate_balance():

    deposits = 0
    withdrawals = 0

    with open("/tmp/transactions.txt","r") as f:

        for line in f:

            transaction, amount = line.strip().split(",")

            amount = int(amount)

            if transaction == "Deposit":
                deposits += amount
            else:
                withdrawals += amount

    balance = deposits - withdrawals

    with open("/tmp/account_data.txt","w") as f:
        f.write(f"{deposits},{withdrawals},{balance}")

def generate_account_report():

    with open("/tmp/account_data.txt","r") as f:

        deposits, withdrawals, balance = f.read().split(",")

    report = f"""
Account Summary

Total Deposit = {deposits}
Total Withdrawal = {withdrawals}
Final Balance = {balance}
"""

    print(report)

    with open("/tmp/account_report.txt","w") as f:
        f.write(report)

with DAG(
    dag_id="exercise12_bank_summary",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="create_transactions",
        python_callable=create_transactions
    )

    task2 = PythonOperator(
        task_id="calculate_balance",
        python_callable=calculate_balance
    )

    task3 = PythonOperator(
        task_id="generate_account_report",
        python_callable=generate_account_report
    )

    task1 >> task2 >> task3
