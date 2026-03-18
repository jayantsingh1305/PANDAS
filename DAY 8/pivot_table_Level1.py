import pandas as pd

data = {
    "Department": ["IT","HR","IT","HR","IT"],
    "Salary": [50000,40000,60000,45000,70000],
}

df = pd.DataFrame(data)

print(df)
print("------")
print(pd.pivot_table(df, values="Salary",index="Department",aggfunc="sum"))
print("------")
print(pd.pivot_table(df, values="Salary", index="Department",aggfunc="mean"))
print("------")
print(pd.pivot_table(df, values="Salary", index="Department", aggfunc="count"))