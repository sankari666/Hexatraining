salaries = [45000, 55000, 65000, 75000, 85000]

print(salaries)

print("Maximum Salary:", max(salaries))
print("Minimum Salary:", min(salaries))

print("Total Salary Payout:", sum(salaries))

print("Average Salary:", sum(salaries) / len(salaries))

salaries.append(95000)
salaries.append(105000)
print(salaries)

salaries.remove(55000)
print(salaries)

salaries.sort()
print(salaries)

salaries.sort(reverse=True)
print(salaries)

print("Second Highest Salary:", salaries[1])

for salary in salaries:
    if salary > 70000:
        print(salary)

employee = (101,"Rahul Sharma","Data Engineering",75000)

print(employee)

print(employee[1])

print(employee[2])

emp_id, emp_name, department, salary = employee

print(emp_id)
print(emp_name)
print(department)
print(salary)

print("Length:", len(employee))
print("First Element:", employee[0])
print("Last Element:", employee[-1])

batch_a = {"Rahul","Priya","Amit","Sneha","Farhan"}

batch_b = {"Priya","Sneha","Neha","Arjun","Farhan"}

print(batch_a.intersection(batch_b))

print(batch_a.difference(batch_b))

print(batch_b.difference(batch_a))

print(batch_a.union(batch_b))

print(batch_a.symmetric_difference(batch_b))

employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "department": "Data Engineering",
    "salary": 75000,
    "city": "Hyderabad"
}

print(employee_info["name"])

print(employee_info["department"])
print(employee_info["city"])

employee_info["experience"] = 5
print(employee_info)

employee_info["salary"] = 85000
print(employee_info)

employee_info.pop("city")
print(employee_info)

print(employee_info.keys())

print(employee_info.values())

print(employee_info.items())

employees = [
    {
        "id": 101,
        "name": "Rahul",
        "department": "IT",
        "salary": 50000
    },
    {
        "id": 102,
        "name": "Priya",
        "department": "HR",
        "salary": 70000
    },
    {
        "id": 103,
        "name": "Amit",
        "department": "IT",
        "salary": 60000
    },
    {
        "id": 104,
        "name": "Sneha",
        "department": "Finance",
        "salary": 80000
    },
    {
        "id": 105,
        "name": "Farhan",
        "department": "IT",
        "salary": 90000
    }
]

for employee in employees:
    print(employee["name"])

for employee in employees:
    if employee["department"] == "IT":
        print(employee)

print(max(employees, key=lambda x: x["salary"]))

print(min(employees, key=lambda x: x["salary"]))

total = sum(employee["salary"] for employee in employees)
print(total / len(employees))

print(sum(employee["salary"] for employee in employees))

for employee in employees:
    if employee["salary"] > 70000:
        print(employee)

count = 0
for employee in employees:
    if employee["department"] == "IT":
        count += 1
print(count)

sorted_employees = sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)

for employee in sorted_employees:
    print(employee["name"])

sorted_employees = sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)

print(sorted_employees[1])

departments = set()

for employee in employees:
    departments.add(employee["department"])

print(departments)
