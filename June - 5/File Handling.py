#file handling
file=open('employees.txt','r')
data=file.read()
print(data)
file.close()

#read file lines
lines=file.readline()
print(lines)

#automatically close the file object
with open("employees.txt","r") as file:
    data=file.read()
    print(data)

#open file for write operation
with open("employees.txt","r") as file:
    file.write("Rahul\n")
    file.write("Priya\n")

#instead of overriding append use it
with open("employees.txt","a") as file:
    file.write("Amit\n")

#write mode
with open("employees.json","w") as file:
    json.dump(employees,file,indent=4)
print("JSON file created successfully")

#read mode
with open("employees.json","r") as file:
    employees=json.load(file)
print(employees)

#printing data in file
for employee in employees:
    print(employee)

#printing only name
for employee in employees:
    print(employee["name"])

#len of file
print(len(employees))

#finding highest salary
high_salary=0
for employee in employees:
    if employee["salary"]>high_salary:
        high_salary=employee["salary"]
print(high_salary)

#file handling with csv file
import csv
with open("employees.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

    for row in reader:
        print(row[1])

count=0
with open("employees.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        count+=1
print(count)
