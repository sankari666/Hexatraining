#List
cities=["Hyderabad","Mumbai","Delhi"]

print(cities[0])
print(cities[1])
print(cities[2])

# Negative Indexing
print(cities[-1])
print(cities[-2])

#update an element
cities[1]="Bangalore"
print(cities)

#Append
cities.append("Chennai")
print(cities)

#insert
cities.insert(1,"Pune")
print(cities)

cities.extend(["Kochin","Pondi"])
print(cities)

#remove
cities.remove("Pune")
print(cities)

#pop
cities.pop()
print(cities)

cities.pop(1)
print(cities)

#del --->deleting the elements
del cities[0]
print(cities)

#clear--> deletes the entier list data
#cities.clear()
#print(cities)

#To find length of the list
print(len(cities))

# Check Membership
print("Mumbai" in cities)
print("Chennai" in cities)

print(cities.index("Kochin"))

#To sort the List
cities.sort()
print(cities)

#Tuple-->act as read only records

cities=("Hyderabad","Mumbai","Delhi","Chennai","Pune")
print(cities)

print(cities[0])
print(cities[1])

print(cities[-1])
print(cities[-2])

print(len(cities))

print(cities[1:4])

#Packing and Unpacking
#1
employee=(101,"Rahul",25000)
print(employee)
#2
emp_id,emp_name,emp_salary=employee
print(emp_id)
print(emp_name)
print(emp_salary)

#return multiple values
def get_employee():
    return 101,"Rahul",25000
result=get_employee()
print(result)

#Each row is represented as Tuple
record=(
    101,
    "Ravi",
    "Chennai",
    35000
)
print(record)
#sets-->not allow duplicates

cities={"Hyderabad","Mumbai","Delhi","Pune"}
print(cities)

cities={"Hyderabad","Mumbai","Delhi","Pune","Mumbai"}
print(cities)

#Remove duplicates fro list
citi=["Hyderabad","Mumbai","Delhi","Pune","Mumbai"]
unique_cities=set(citi)
print(unique_cities)

cities.add("Chennai")
print(cities)

cities.update(["Chennai","Kochin"])
print(cities)

cities.remove("Delhi") # shows error when the data is not present in the set
print(cities)

cities.discard("Delhi") # No error when data is not present
print(cities)

#Union, Intersection
set1={"Python","SQL"}
set2={"MongoDB","Python"}
result1=set1.union(set2) # combine both sets and return without duplicates
print(result1)

result2=set1.intersection(set2) # common data between 2 sets
print(result2)

result3=set1.difference(set2) # difference between set 1 and set2 and returns set1 data only
print(result3)

result4=set1.symmetric_difference(set2) # difference between set1 and 2 and returns both sets data
print(result4)
#Dictionary
customer={
    "customer_id":101,
    "name":"Rahul",
    "city":"Mumbai"
}
print(customer)

print(customer["name"])
print(customer["city"])

#safest way
print(customer.get("name"))
print(customer.get("city"))

#Add new key value pair
customer["Salary"]=75000
print(customer)

#update
customer["name"]="Rahul Sharma"
print(customer)

customer.pop("Salary")
print(customer)

del customer["city"]
print(customer)
