import pandas as pd

data = {
    "Name": ["A","B","C","D","E"],
    "Department": ["IT","HR","IT","HR","IT"],
    "Salary": [50000,40000,60000,45000,70000],
    "Experience": [2,5,3,4,6]
}

df = pd.DataFrame(data)

print(df)
print("------")
print(pd.pivot_table(df, values="Salary", index="Department", aggfunc="sum"))
print("------")
print(pd.pivot_table(df, values="Salary", index="Department", aggfunc="mean"))
print("------")
print(pd.pivot_table(df, values="Name", index="Department", aggfunc="count"))
print("------")
print(pd.pivot_table(df, values="Salary", index="Department", aggfunc="max"))
print("------")
print(pd.pivot_table(df, values=["Experience","Salary"], index="Department", aggfunc="mean"))