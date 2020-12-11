from polyglot.text import Text
from statistics import mean
import pandas as pd
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import numpy as np

"""
DUTCH
"""
"""
# Prepare dictionaries
sents_sentiment = defaultdict(list)

# Read in data
tsv_file = "../data/nl/decoded_nl_greta_overview.tsv"
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
articles = content['Text']
publishers = content['Publisher']

# Save mean sentiment of sentences per article
for text, publisher in zip(articles, publishers):
    text = ''.join(x for x in text if x.isprintable())
    sentences = Text(text, hint_language_code = 'nl').sentences
    sent_senti = float(mean([sent.polarity for sent in sentences]))
    sents_sentiment[publisher].append(sent_senti)

art_pub_sent = defaultdict(dict)
for publisher in sents_sentiment:
    art_pub_sent[publisher] = mean(sents_sentiment[publisher])

d = sents_sentiment
top10_publishers = sorted(d, key=lambda k: len(d[k]), reverse=True)[:10]

fig, ax = plt.subplots(1, 1, figsize = (11, 6))
x = top10_publishers
y = [art_pub_sent[publisher] for publisher in top10_publishers]
plt.xlabel('PUBLISHER')
plt.ylabel('SENTIMENT"')
plt.title('MEAN ARTICLE SENTIMENT OF DUTCH PUBLISHERS')
plt.bar(x, y)
fig.tight_layout()
fig.savefig("../data/plots/nl_publisher_sentiment.png")
plt.show()

"""

"""
ITALIAN
"""

sents_sentiment = defaultdict(list)

tsv_file = "../data/it/it_greta_overview.tsv"
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
articles = content['Text']
publishers = content['Publisher']

# Save mean sentiment of sentences per article
for text, publisher in zip(articles, publishers):
    if publisher == 'la Repubblica':
        publisher = 'La Repubblica'
    text = ''.join(x for x in text if x.isprintable())
    sentences = Text(text, hint_language_code = 'it').sentences
    sent_senti = float(mean([sent.polarity for sent in sentences]))
    sents_sentiment[publisher].append(sent_senti)

art_pub_sent = defaultdict(dict)
for publisher in sents_sentiment:
    art_pub_sent[publisher] = mean(sents_sentiment[publisher])

d = sents_sentiment
top10_publishers = sorted(d, key=lambda k: len(d[k]), reverse=True)[:10]

"""
SENTIMENT PLOT
"""

fig, ax = plt.subplots(1, 1, figsize = (12, 6))
x = top10_publishers
y = [art_pub_sent[publisher] for publisher in top10_publishers]
plt.xlabel('PUBLISHER')
plt.ylabel('SENTIMENT"')
plt.title('MEAN ARTICLE SENTIMENT OF ITALIAN PUBLISHERS')
plt.bar(x, y)
fig.tight_layout()
fig.savefig("../data/plots/it_publisher_sentiment.png")
plt.show()