import pandas as pd
import numpy as np
df  = pd.read_csv("C:/Users/BenjaminWinsey/Documents/GitHub/Preppin-Data-Challenges/2023 Week 5/Data Sources/PD 2023 Wk 1 Input (1).csv")
df["Bank"] = df["Transaction Code"].str.extract(r'([a-zA-Z]+)')
dates = pd.date_range(start='2023-01-01', end='2023-12-31')
df2=pd.DataFrame({"date": dates})
df2["Month"]=df2["date"].dt.month
df2["Month"] = df2["Month"].map({
    1: 'January',
    2: 'Febuary',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12:'December'
})
df["DoW"] = pd.to_datetime(df["Transaction Date"])
df3 = pd.merge (df, df2, how="inner", right_on=df2["date"], left_on=df["DoW"])
df3 = df3.drop(columns= ["date","Transaction Date", "DoW", "key_0"])
df3 = df3.drop(columns=["Online or In-Person", "Customer Code", "Transaction Code"])
df3 =df3.groupby(["Month","Bank"]).agg({"Value":"sum"}).reset_index()
df3["Rank"] = df3.groupby(["Month"])["Value"].rank(method='max', ascending=False)
df3["Rank"]=df3["Rank"].astype("int")
df4 = df3.groupby(["Bank"]).agg({"Rank":"mean"}).reset_index()
df3 = pd.merge(df3,df4, how="inner", left_on="Bank", right_on="Bank")
df3["Rank_x"]=df3["Rank_x"].astype("string")
df5 = df3.groupby(["Rank_x"]).agg({"Value":"mean"}).reset_index()
df3 = pd.merge(df3,df5, how="inner", left_on="Rank_x", right_on="Rank_x")
print(df3)