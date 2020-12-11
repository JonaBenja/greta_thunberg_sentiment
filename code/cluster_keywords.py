import pandas as pd
import pickle
from collections import defaultdict, Counter
import json

tsv_file = "../data/clusters/nl_4_topic_clusters.tsv"
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
clusters = content['Cluster']

with open("../data/clusters/nl_keywords.json", 'r') as infile:
    keywords = json.load(infile)

keyword_clusters = {0:defaultdict(int), 1:defaultdict(int), 2:defaultdict(int), 3:defaultdict(int)}

for doc, cluster in zip(keywords, clusters):
    for word in keywords[doc]:
        if word not in keyword_clusters[cluster]:
            keyword_clusters[cluster][word] = 1
        else:
            keyword_clusters[cluster][word] += 1

sorted_cluster0 = sorted(keyword_clusters[0].items(), key=lambda item:item[1], reverse=True)
sorted_cluster1 = sorted(keyword_clusters[1].items(), key=lambda item:item[1], reverse=True)
sorted_cluster2 = sorted(keyword_clusters[2].items(), key=lambda item:item[1], reverse=True)
sorted_cluster3 = sorted(keyword_clusters[3].items(), key=lambda item:item[1], reverse=True)

print(sorted_cluster0[:20])
print(sorted_cluster1[:20])
print(sorted_cluster2[:20])
print(sorted_cluster3[:20])

"""
ITALIAN CLUSTER KEYWORDS
"""


tsv_file = "../data/clusters/it_4_topic_clusters.tsv"
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
clusters = content['Cluster']

with open("../data/clusters/it_keywords.json", 'r') as infile:
    keywords = json.load(infile)

keyword_clusters = {0:defaultdict(int), 1:defaultdict(int), 2:defaultdict(int), 3:defaultdict(int)}

for doc, cluster in zip(keywords, clusters):
    for word in keywords[doc]:
        if word not in keyword_clusters[cluster]:
            keyword_clusters[cluster][word] = 1
        else:
            keyword_clusters[cluster][word] += 1

sorted_cluster0 = sorted(keyword_clusters[0].items(), key=lambda item:item[1], reverse=True)
sorted_cluster1 = sorted(keyword_clusters[1].items(), key=lambda item:item[1], reverse=True)
sorted_cluster2 = sorted(keyword_clusters[2].items(), key=lambda item:item[1], reverse=True)
sorted_cluster3 = sorted(keyword_clusters[3].items(), key=lambda item:item[1], reverse=True)

print(sorted_cluster0[:20])
print(sorted_cluster1[:20])
print(sorted_cluster2[:20])
print(sorted_cluster3[:20])




