import pandas as pd

df = pd.read_excel("students.xlsx")
data = {}

for i in range(len(df)):
    r = df.loc[i, "rollno"]
    n = df.loc[i, "name"]
    s1 = df.loc[i, "sub1"]
    s2 = df.loc[i, "sub2"]
    s3 = df.loc[i, "sub3"]
    t = s1 + s2 + s3
    data[r] = {"name": n, "sub1": s1, "sub2": s2, "sub3": s3, "total": t}

for k in data:
    print(k, data[k])
