import pandas as pd
#it is used for apriori algorithm 
from mlxtend.frequent_patterns import apriori,association_rules
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure



X=pd.read_csv("E:\\Data Science\\Assignments\\Python code\\Association_Rules\\book.csv")

frequent_itemsets = apriori(X, min_support=0.0035, max_len=4,use_colnames = True)
frequent_itemsets.sort_values('support',ascending = False,inplace=True)
figure(num=None, figsize=(30rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1), 10), dpi=80, facecolor='w', edgecolor='k')
plt.bar(x = list(range(1,11)),height = frequent_itemsets.support[1:11],color='rgmyk');plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item-sets',fontsize = 20);plt.ylabel('support', fontsize=20);plt.title('top 10 list sets with minsupport=0.0035 and max_length=4', fontsize=40)


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.shape

rules.sort_values('lift',ascending = False,inplace=True)
rules.head(20)

#min_support=0.0035 , max_len=3

frequent_itemsets = apriori(X, min_support=0.0035, max_len=3,use_colnames = True)

frequent_itemsets.sort_vafrequent_itemsets.sort_values('support',ascending = False,inplace=True)lues('support',ascending = False,inplace=True)

figure(num=None, figsize=(30, 10), dpi=80, facecolor='w', edgecolor='k')
plt.bar(x = list(range(1,11)),height = frequent_itemsets.support[1:11],color='rgmyk');plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item-sets',fontsize = 20);plt.ylabel('support', fontsize=20);plt.title('top 10 list sets with minsupport=0.0035 and max_length=3', fontsize=40)


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.sort_values('lift',ascending = False,inplace=True)
rules.head(20)

#min_support=0.007 , max_len=

frequent_itemsets = apriori(X, min_support=0.0035, max_len=4,use_colnames = True)
frequent_itemsets.sort_values('support',ascending = False,inplace=True)
figure(num=None, figsize=(30rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1), 10), dpi=80, facecolor='w', edgecolor='k')
plt.bar(x = list(range(1,11)),height = frequent_itemsets.support[1:11],color='rgmyk');plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item-sets',fontsize = 20);plt.ylabel('support', fontsize=20);plt.title('top 10 list sets with minsupport=0.0035 and max_length=4', fontsize=40)


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.shape

rules.sort_values('lift',ascending = False,inplace=True)
rules.head(20)
