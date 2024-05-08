import pandas as pd
df=pd.read_csv('pubmid11.csv')
mylist=df["Pmid"].tolist()
with open("file11.txt", "w") as output:
    output.write(str(mylist))

