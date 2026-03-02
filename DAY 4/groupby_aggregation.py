# import pandas as pd

# data = {
#     "Name": ["A","B","C","D","E"],
#     "Department": ["IT","HR","IT","HR","IT"],
#     "Salary": [50000,40000,60000,45000,70000]
# }

# df = pd.DataFrame(data)
# print(df)
# print("------")

# grouped = df.groupby("Department")
# for dept,group in grouped:
#     print("Department:",dept)
#     print(group)
#     print("------")

# print(df.groupby("Department")["Salary"].mean())
# print("------")
# print(df.groupby("Department")["Salary"].sum())
# print("------")
# print(df.groupby("Department")["Salary"].max())
# print("------")
# print(df.groupby("Department")["Salary"].count())
# print("------")

import pandas as pd

data = {
    "City" : ["Delhi", "Delhi", "Mumbai", "Mumbai"],
    "Product" : ["A", "B", "C", "D"],
    "Sales" : [100, 200, 150, 250]
}

df = pd.DataFrame(data)
print(df)
print("------")
print(df.groupby("City")["Sales"].sum())