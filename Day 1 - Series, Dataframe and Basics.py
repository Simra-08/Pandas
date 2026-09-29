# ------------------------- DAY 1 -----------------------------

import pandas as pd

# df = pd.read_csv("xyz.csv")

import pandas as pd

data = {
    "Name": ["Aisha", "Rahul", "Meera", "Arjun", "Zoya"],
    "Age": [19, 21, 20, 22, 19],
    "City": ["Bengaluru", "Mumbai", "Delhi", "Bengaluru", "Chennai"],
    "Score": [85, 92, 78, 95, 88]
}

df = pd.DataFrame(data)

# print(df)

# print(df.head(3))

# print(df.tail(3))

# print(df.info())

# print(df.columns)

# print(df["Score"])

# print(df.describe())

# print(df.info())

# q9
# print(df.shape)
# print(df.columns)
# print(df.head(5))
# print(df.info())
# print(df.describe())

# q10
# print(df.info())
# rangeindex 5 hence 5 students

# print(df["Score"].mean())
# print(df["Score"].max())
# print(df["Score"].min())
# print(df["Score"].sum())

# ---- WRONG

# print(df["City"].count(unique=True))
# print(df["Score">80])
# print(df["Arjun"])
# print(df["Name"["Score"].max()])
# print(df["City" == "Bengaluru"].count())
# print(df["Score"["City" == "Bengaluru"]].mean())


# ---------- RIGHT

print(df["City"].nunique())
print(df["City"].unique())


