import pandas as pd 
import numpy as np 
df = pd.read_csv("C:/Users/BenjaminWinsey/Documents/GitHub/Preppin-Data-Challenges/2023 Week 3/Data Sources/PD 2023 Wk 1 Input.csv")
# print(df)
df=df[df["Transaction Code"].str.contains("DSB")]
df["Online or In-Person"]= np.where(df["Online or In-Person"]==1, "Online", "In-Person")
df["Transaction Date"]= pd.to_datetime(df["Transaction Date"])
df["Quarter"] = pd.PeriodIndex(df["Transaction Date"], freq='Q')
df["Quarter"]= df["Quarter"].astype("string")
df["Quarter"]= df["Quarter"].str.replace('2023', '', regex=True)
df = df.groupby(["Quarter", "Online or In-Person"])["Value"].sum().reset_index()
# print(df)
df2 = pd.read_csv("C:/Users/BenjaminWinsey/Documents/GitHub/Preppin-Data-Challenges/2023 Week 3/Data Sources/Targets.csv")
# df3= pd.merge(df,df2, how="inner", left_on=df['Quarter'], right_on=df2['Quarter'])
# df2.pivot(
    # df2, values='Q1', index=["Online or In-Person"], columns=["Q1"]
    
df2= pd.melt(df2,id_vars=["Online or In-Person"], value_vars=["Q1", "Q2", "Q3", "Q4"])
df2.rename(columns={'variable': 'Quarter', 'value': 'Quarterly Targets'}, inplace=True)
df2["Quarter"]=df2["Quarter"].str.replace('Q', '')
# print(df)
df["Quarter"]= df["Quarter"].str.replace('Q', '')
df3= pd.merge(df, df2, how='inner', left_on=["Quarter", "Online or In-Person"], right_on=["Quarter", "Online or In-Person"])
df3.groupby(["Online or In-Person",  "Quarter"])["Value"].sum()
df3["Value"]=df3["Value"].astype("int")
df3["Quarterly Targets"]=df3["Quarterly Targets"].astype("int")
df3["Variable Diff"] = df3["Value"].sub(df3["Quarterly Targets"])
print(df3)