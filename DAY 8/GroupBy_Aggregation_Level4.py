import pandas as pd
import numpy as np

data = {
    "UserID" : [1,2,3,4,5,6,7,8],
    "City" : ["Delhi","Delhi","Mumbai","Mumbai","Delhi","Mumbai","Delhi","Mumbai"],
    "Product" : ["Phone","Laptop","Phone","Laptop","Tablet","Phone","Laptop","Tablet"],
    "PurchaseAmount" : [20000,50000,22000,48000,15000,21000,52000,18000]
}

df = pd.DataFrame(data)

print(df)
print("------")
print(df.groupby("City")["PurchaseAmount"].sum())
print("------")
print(df.groupby("Product")["PurchaseAmount"].mean())
print("------")
print(df.groupby("Product")["PurchaseAmount"].max())
