# import pandas as pd
# import numpy as np

# data = {
#     "Name":["A","B","C","D"],
#     "Age":[22,np.nan,25,np.nan],
#     "Marks":[80,90,np.nan,70]
# }

# df = pd.DataFrame(data)

# print(df.isnull().sum())
# df["Age"]=df["Age"].fillna(df["Age"].mean())
# df["Marks"]=df["Marks"].fillna(0)
# print(df)

# import pandas as pd
# import numpy as np

# data = {
#     "Age":[20,22,np.nan,25,np.nan,30],
#     "Salary":[30000,32000,35000,np.nan,40000,42000],
#     "Experience":[1,2,3,np.nan,np.nan,50]
# }

# df = pd.DataFrame(data)

# # print(df.isnull().sum())
# # print([df.isnull().sum()/len(df)*100])

# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["Salary"] = df["Salary"].fillna(df["Salary"].median())
# df["Experience"] = df["Experience"].fillna(df["Experience"].mean())
# print(df)

# import pandas as pd
# import numpy as np

# data = {
#     "Gender": ["M","F",np.nan,"F","M",np.nan],
#     "Age": [25,30,22,np.nan,28,np.nan],
#     "Income": [50000,np.nan,45000,60000,np.nan,52000]
# }

# df = pd.DataFrame(data)

# #print(df.isnull().sum())
# df["Gender"]=df["Gender"].fillna(df["Gender"].mode()[0],inplace=True)
# df["Age"]=df["Age"].fillna(df["Age"].mean())
# df["Income"]=df["Income"].fillna(df["Income"].median())
# print(df)

# import pandas as pd
# import numpy as np

# data = {
#     "CustomerID" : [1,2,3,4,5],
#     "Age" : [23,np.nan,35,np.nan,29],
#     "Income" : [50000,60000,np.nan,80000,np.nan],
#     "SpendingScore" : [np.nan,50,60,70,np.nan]
# }

# df = pd.DataFrame(data)
# print(df.isnull())
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["Income"] = df["Income"].fillna(df["Income"].median())
# df["SpendingScore"] = df["SpendingScore"].fillna(df["SpendingScore"].mean())
# print(df)
