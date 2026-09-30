# ------------------- DAY 2 --------------------------------------------
# Learned how to select single and multiple columns, access rows using loc and iloc, 
# filter rows using 
# comparison operators, combine conditions with & and |, 
# and use isin() for filtering multiple values. 
# Practiced combining row filtering with column selection on a sample dataset.

import pandas as pd

data = {
    "Name": ["Aisha", "Rahul", "Meera", "Arjun", "Zoya", "Kabir"],
    "Age": [19, 21, 20, 22, 19, 23],
    "City": ["Bengaluru", "Mumbai", "Delhi", "Bengaluru", "Chennai", "Mumbai"],
    "Score": [85, 92, 78, 95, 88, 91]
}

df = pd.DataFrame(data)

print(df["Name"])
print(df[["Name","Score"]])
print(df.iloc[2])
print(df["Score"].iloc[3])
print(df.iloc[0:4,0:3])
print(df[df["Score"]>90])
print(df[df["Age"]<=20])
print(df[df["City"]=="Mumbai"])
print(df[(df["Age"]>20) & (df["Score"]>90)])
print(df[(df["City"]=="Bengaluru") | (df["City"]=="Delhi")])
print(df[df["City"].isin(["Bengaluru","Delhi","Mumbai"])])

print(df[df["Score"]>=85][["Name","City","Score"]] )


data = {
    "Name": ["Aisha", "Rahul", "Meera", "Arjun", "Zoya", "Kabir"],
    "Age": [19, 21, 20, 22, 19, 23],
    "City": ["Bengaluru", "Mumbai", "Delhi", "Bengaluru", "Chennai", "Mumbai"],
    "Score": [85, 92, 78, 95, 88, 91]
}

df = pd.DataFrame(data)

print(df[df["Score"]>90][["Name","Age"]])
print(df[df["Age"]==19])
print(df[df["City"]=="Mumbai"][["Name","Score"]])
print(df.iloc[0:3,0:3:2])
print(df[df["City"]!="Delhi"])
print(df[(df["Score"] >=80) & (df["Score"]<=90)])

print(df[(df["City"]=="Mumbai") | (df["City"]=="Chennai")[["Name","Score"]]])
print([df.iloc[4][["Name","City"]]])
print(df[(df["Age"]>= 21)  | (df["Score"]==95)])
print(df[((df["City"]=="Bengaluru")  | (df["City"]=="Mumbai")) & (df["Score"]>85)])