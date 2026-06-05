#general exceptional handling
try:
    a=10
    b=0
    result=a/b
    print(result)
except:
    print("error occured")
print("Program completed")

#specific exceptional handling
try:
    a=10
    b=0
    result=a/b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by 0")

try:
    age=int(input("Enter age: "))
    print(age)
except ValueError:
    print("Please enter a numeric value")

try:
    age=int(input("Enter age: "))
    print(100/age)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Age cannot be zero")

#Exception Object
try:
    num=int("abc")
except Exception as e:
    print(e)

try:
    print(10/0)
except:
    print("Error")
finally:
    print("Connection Closed")

#raise error
salary=-1000
if salary<0:
    raise ValueError('Salary cannot be negative')
