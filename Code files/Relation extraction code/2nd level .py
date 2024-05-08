import pandas as pd
import os

os.chdir(r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet")

data= pd.read_csv("Level1_data.csv")
data.columns
data= data[(data.Keep=='Yes') & (data.Foods_count>1)]
data.to_csv("Level1_Keep.csv")
#data.Id