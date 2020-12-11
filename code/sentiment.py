from polyglot.text import Text
from statistics import mean
import pandas as pd
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import numpy as np

"""
DUTCH
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

publishers = top10_publishers
sentiment = [art_pub_sent[publisher] for publisher in top10_publishers]

x = np.arange(len(publishers))  # the label locations
width = 0.50  # the width of the bars

fig, ax = plt.subplots(1, 1, figsize = (16, 6))
rects1 = ax.bar(x - width/2, sentiment, width, label='Men')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('SENTIMENT')
ax.set_xlabel('PUBLISHER')
ax.set_title('MEAN ARTICLE SENTIMENT OF DUTCH PUBLISHERS')
ax.set_xticks(x)
ax.set_xticklabels(publishers)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect, publisher in zip(rects, top10_publishers):
        label = len(sents_sentiment[publisher])
        height = rect.get_height()
        ax.annotate('{}'.format(label),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
fig.tight_layout()
plt.show()
fig.savefig("../data/plots/nl_publisher_sentiment.png")

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

publishers = top10_publishers
sentiment = [art_pub_sent[publisher] for publisher in top10_publishers]

x = np.arange(len(publishers))  # the label locations
width = 0.50  # the width of the bars

fig, ax = plt.subplots(1, 1, figsize = (16, 6))
rects1 = ax.bar(x - width/2, sentiment, width, label='Men')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('SENTIMENT')
ax.set_xlabel('PUBLISHER')
ax.set_title('MEAN ARTICLE SENTIMENT OF ITALIAN PUBLISHERS')
ax.set_xticks(x)
ax.set_xticklabels(publishers)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect, publisher in zip(rects, top10_publishers):
        label = len(sents_sentiment[publisher])
        height = rect.get_height()
        ax.annotate('{}'.format(label),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
fig.tight_layout()
plt.show()
fig.savefig("../data/plots/it_publisher_sentiment.png")