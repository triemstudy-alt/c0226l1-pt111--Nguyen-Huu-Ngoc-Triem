import pandas as pd
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    f.write("username,password\n")
    f.write("user1,pass1\n")
    f.write("user2,pass2\n")
df = pd.read_csv("data.csv")
for i, row in df.iterrows():
    print(row["username"], row["password"])