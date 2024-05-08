import pandas as pd
source_path = "pmids.csv"
for i,chunk in enumerate(pd.read_csv(source_path, chunksize=2000)):
    chunk.to_csv('pubmid{}.csv'.format(i), index=False)

    
    
