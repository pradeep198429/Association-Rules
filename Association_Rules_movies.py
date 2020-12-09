import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from mlxtend.frequent_patterns import apriori, association_rules 


X=pd.read_csv("E:\\Data Science\\Assignments\\Python code\\Association_Rules\\my_movies.csv")

X.drop(['V1', 'V2', 'V3', 'V4', 'V5'], axis = 1, inplace = True)
X.head()

frequent_itemsets = apriori(X, min_support=0.66, max_len=3,use_colnames = True)

frequent_itemsets

frequent_itemsets.shape

frequent_itemsets.sort_values('support',ascending = False,inplace=True)

figure(num=None, figsize=(30, 10), dpi=80, facecolor='w', edgecolor='k')
plt.bar(x = list(range(1,11)),height = frequent_itemsets.support[1:11],color='rgmyk');plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item-sets',fontsize = 20);plt.ylabel('support', fontsize=20);plt.title('top 10 list sets with minsupport=0.0035 and max_length=4', fontsize=40)


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.shape

rules.sort_values('lift',ascending = False,inplace=True)
rules.head(20)

frequent_itemsets = apriori(X, min_support=0.66, max_len=3,use_colnames = True)

frequent_itemsets = apriori(X, min_support=0.66, max_len=2,use_colnames = True)


frequent_itemsets = apriori(X, min_support=0.22, max_len=3,use_colnames = True)


figure(num=None, figsize=(30, 10), dpi=80, facecolor='w', edgecolor='k')
plt.bar(x = list(range(0,7)),height = frequent_itemsets.support[0:7],color='rgmyk');plt.xticks(list(range(0,7)),frequent_itemsets.itemsets[0:7])
plt.xlabel('item-sets',fontsize = 20);plt.ylabel('support', fontsize=20);plt.title('top 7 list sets with minsupport=0.22 and max_length=3', fontsize=40)




rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.shape

rules.sort_values('lift',ascending = False,inplace=True)
rules.head(20)






