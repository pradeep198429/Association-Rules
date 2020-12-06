import pandas as pd

X=pd.read_csv("E:\\Data Science\\Assignments\\Python code\\Association_Rules\\my_movies.csv")

df=X.iloc[:,5:15]

from mlxtend.frequent_patterns import apriori,association_rules
frequent_items=apriori(df, min_support=0.005, max_len=3,use_colnames = True)

frequent_items.sort_values('support',ascending=False,inplace=True)

rules=association_rules(frequent_items,metric='lift', min_threshold=1)

print(rules.sort_values('lift',ascending=False).head())
