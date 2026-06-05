#pandas
import pandas as pd

data={
    "employee_id":[101,102,103],
    "name":["Rahul","Amit","Priya"],
    "salary":[75000,70000,65000]
}
df=pd.DataFrame(data)
print(df)

#reading csv
df=pd.read_csv("employees.csv")
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df["name"])
print(df["name","salary"])
