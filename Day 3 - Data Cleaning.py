# --------------------- DAY 3 -----------------------------------------------
# Learned how to clean datasets in Pandas by identifying and handling missing 
# values using isna(), notna(), fillna(), and dropna(). 
# Practiced replacing missing values with fixed values or column means, removing duplicate rows using duplicated() 
# and drop_duplicates(), and applying basic 
# data-cleaning techniques to prepare datasets for analysis.

import pandas as pd

data = {
    "Name": ["Aisha", "Rahul", "Meera", "Arjun", "Zoya", "Kabir", "Rahul"],
    "Age": [19, None, 20, 22, None, 21, None],
    "City": ["Bengaluru", "Mumbai", None, "Bengaluru", "Chennai", "Mumbai", "Mumbai"],
    "Score": [85, 92, None, 95, 88, None, 92]
}

df = pd.DataFrame(data)

print(df)
print(df.isna())
print(df.isna().sum())
print(df[df["Age"].isna()])
print(df[df["Score"].notna()])

df["Age"] =df["Age"].fillna(20)
print(df)
df["City"] = df["City"].fillna("Unknown")
print(df)
df["Score"] = df["Score"].fillna(df["Score"].mean())
print(df)
print(df.dropna())
print(df.dropna(subset = "Age"))

print(df.duplicated())
print(df.duplicated().sum())
print(df.drop_duplicates())
# yes


df["Age"] = df["Age"].fillna(df["Age"].mean())
# print(df)
df["City"] = df["City"].fillna(df ["City"]=="Unknown")
# print(df)
df["Score"] = df["Score"].fillna("Unknown")
df.drop_duplicates()
print(df)
