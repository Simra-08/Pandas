import pandas as pd

print(pd.__version__)

data = [100,102,103]
series = pd.Series(data,index = ["a","b","c"])
print(series)
print(series.loc["b"])
series.loc["d"] = 150
print(series)
print(series.iloc[3])

data = [100,200,202,203,600]
series = pd.Series(data,index = ["a","b","c","d","e"])
print(series[series>200])


calories = {"day1":1750,
            "day2":2100,
            "day3":1700}
series = pd.Series(calories)
print(series)
print(series.loc["day1"])
print(series.iloc[1])
print(series[series>1700])



data = {"Name":["Spongebob","Squidward","Patrick"],
        "Age":[27,26,21]}

df = pd.DataFrame(data,index = ["emp1","emp2","emp3"])
# print(df)
# print(df.loc["emp1"])

# add column
df["Job"] = ["engineer","doctor","cook"]

# add row
new_row = pd.DataFrame({"Name":["Sandy"],"Age":[12],"Job":["analyst"]})

df = pd.concat([df,new_row])
print(df)