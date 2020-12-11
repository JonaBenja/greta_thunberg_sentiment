import spacy
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.cm as cm
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

tsv_file = "../data/clusters/nl_4_topic_clusters.tsv"
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
articles = content['Text']
clusters = content['Cluster']

nlp = spacy.load("nl_core_news_lg")
doc_vectors = [nlp(doc).vector for doc in articles]

# Apply dimensionality reduction with PCA
reduction_technique = PCA(n_components=2)

print("Calculate dimensionality reduction")
two_dimensional = reduction_technique.fit_transform(doc_vectors)
print("Done")

fig, ax = plt.subplots(1, 1, figsize = (15, 10))

# Plot the two-dimensional vectors for the selected terms
x_values = [doc_vector[0] for doc_vector in two_dimensional]
y_values = [doc_vector[1] for doc_vector in two_dimensional]

fig, ax = plt.subplots(1, 1, figsize=(15, 10))

colors = cm.rainbow(np.linspace(0, 1, len(set(clusters))))

for x, y, cluster in zip(x_values, y_values, clusters):
    c = colors[cluster]
    ax.plot(x, y, 'o', markersize=12, color=c)

# Add title and description
ax.set_title('Dutch document vectors')
description = "Dutch document vectors reduced to two dimensions using the PCA algorithm. "
fig.text(.51, .05, description, ha="center", fontsize=12)

# Hide the ticks
ax.set_yticks([])
ax.set_xticks([])

cluster1 = mpatches.Circle((0.1, 0.1), color=colors[0], label='Cluster 1')
cluster2 = mpatches.Circle((0.1, 0.1), color=colors[1], label='Cluster 2')
cluster3 = mpatches.Circle((0.1, 0.1), color=colors[2], label='Cluster 3')
cluster4 = mpatches.Circle((0.1, 0.1), color=colors[3], label='Cluster 4')

plt.legend(handles=[cluster1, cluster2, cluster3, cluster4])
fig.savefig("../data/plots/nl_clusterplot.png")
plt.show()

"""
ITALIAN DOCUMENT VECTORS
"""

tsv_file = "../data/clusters/it_4_topic_clusters.tsv"
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
articles = content['Text']
clusters = content['Cluster']

nlp = spacy.load("it_core_news_lg")
doc_vectors = [nlp(doc).vector for doc in articles]

# Apply dimensionality reduction with PCA or T-SNE
reduction_technique = PCA(n_components=2)

print("Calculate dimensionality reduction")
two_dimensional = reduction_technique.fit_transform(doc_vectors)
print("Done")

"""
ITALIAN CLUSTERPLOT
"""

fig, ax = plt.subplots(1, 1, figsize = (15, 10))

# Plot the two-dimensional vectors for the selected terms
x_values = [doc_vector[0] for doc_vector in two_dimensional]
y_values = [doc_vector[1] for doc_vector in two_dimensional]

fig, ax = plt.subplots(1, 1, figsize=(15, 10))

colors = cm.rainbow(np.linspace(0, 1, len(set(clusters))))

for x, y, cluster in zip(x_values, y_values, clusters):
    c = colors[cluster]
    ax.plot(x, y, 'o', markersize=12, color=c)

# Add title and description
ax.set_title('Italian document vectors')
description = "Italian document vectors reduced to two dimensions using the PCA algorithm. "
fig.text(.51, .05, description, ha="center", fontsize=12)

# Hide the ticks
ax.set_yticks([])
ax.set_xticks([])

cluster1 = mpatches.Circle((0.1, 0.1), color=colors[0], label='Cluster 1')
cluster2 = mpatches.Circle((0.1, 0.1), color=colors[1], label='Cluster 2')
cluster3 = mpatches.Circle((0.1, 0.1), color=colors[2], label='Cluster 3')
cluster4 = mpatches.Circle((0.1, 0.1), color=colors[3], label='Cluster 4')

plt.legend(handles=[cluster1, cluster2, cluster3, cluster4])
fig.savefig("../data/plots/it_clusterplot.png")
plt.show()
