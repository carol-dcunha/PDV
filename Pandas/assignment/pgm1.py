import pandas as pd
print "Pandas version: ",pd.__version__

print "\nVersion information of the libraries required by pandas library:"
pd.show_versions(as_json=False)
