import csv, pandas as pd
from pymed import PubMed
pubmed = PubMed(tool="Food Synergy", email="shahid.21csz0029@iitrpr.ac.in","nivedita.21csz0019@iitrpr.ac.in")
query = 
num_max = pubmed.getTotalResultsCount(query)
print("Number of records to be returned: {}.".format(num_max))
results = pubmed.query(query, max_results=num_max)
pubmed = [paper.toDict() for paper in results]
pd.DataFrame(pubmed).to_csv("file.csv", index=False, quoting=csv.QUOTE_ALL)
