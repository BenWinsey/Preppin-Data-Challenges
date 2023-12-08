import pandas as pd
import numpy as np
df = pd.read_csv ("C:/Users/BenjaminWinsey/Desktop/Python/Preppin-Data-Challenges/2023 Week 1/Data Sources/PD 2023 Wk 1 Input.csv")
df["Bank"] = df["Transaction Code"].str.extract(r'([a-zA-Z]+)')
# print(df)
df["Online or In-Person"]= np.where(df["Online or In-Person"]==1, "Online", "In-Person")

# df["DoW"] = pd.to_datetime(df["Transaction Date"]).dt.day_name()
# print(df)
dates = pd.date_range(start='2023-01-01', end='2023-12-31')
df2=pd.DataFrame({"date": dates})
df2["day_of_week"]=df2["date"].dt.dayofweek
df2["day_of_week"] = df2["day_of_week"].map({
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
})
df["DoW"] = pd.to_datetime(df["Transaction Date"])
df3 = pd.merge (df, df2, how="inner", right_on=df2["date"], left_on=df["DoW"])
# print(df3)
df3 = df3.drop(columns= ["date","Transaction Date", "DoW", "key_0"])
# print(df3)
df3 = df3.rename(columns={"day_of_week": "Transaction Date"})
# print(df3)
df4 = df3.groupby("Bank")["Value"].sum()
print("Get sum of the grouped data:\n", df4)
df5 = df3.groupby(["Bank", "Online or In-Person", "Transaction Date"])["Value"].sum().reset_index()
print(df5)
df6 = df3.groupby(["Bank", "Customer Code"])["Value"].sum().reset_index()
print(df6)




