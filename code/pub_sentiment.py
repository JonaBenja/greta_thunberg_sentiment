from polyglot.text import Text
from statistics import mean
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
"""
text_sentiment = defaultdict(list)
article_sentiment = defaultdict(list)

tsv_file = "it/it_greta_overview.tsv"
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
articles = content['Text']
publishers = content['Publisher']

for text, publisher in zip(articles, publishers):
    try:
        text_senti = Text(text).polarity
        sent_senti = float(mean([sent.polarity for sent in Text(text, hint_language_code= 'it').sentences]))
        text_sentiment[publisher].append(sent_senti)
        article_sentiment[publisher].append(text_senti)
    except:
        error = 'pycld2.error'

mean_pub_sent = defaultdict(float)
for publisher in text_sentiment:
    if len(text_sentiment[publisher]) > 3:
        mean_pub_sent[publisher] = mean(text_sentiment[publisher])

art_pub_sent = defaultdict(float)
for publisher in article_sentiment:
    if len(article_sentiment[publisher]) > 3:
        art_pub_sent[publisher] = mean(article_sentiment[publisher])


print(mean_pub_sent)
print(art_pub_sent[publisher])

fig, ax = plt.subplots(1, 1, figsize = (10, 6))
x = mean_pub_sent.keys()
y = [mean_pub_sent[publisher] for publisher in mean_pub_sent]
plt.xlabel('PUBLISHER')
plt.ylabel('SENTIMENT"')
plt.title('SENTIMENT OF PUBLISHERS')
plt.bar(x, y)
fig.tight_layout()
fig.savefig("new_plots/it_publisher_sentiment.png")
plt.show()
"""

"""
DUTCH
"""

text_sentiment = defaultdict(dict)
sents_sentiment = defaultdict(dict)

tsv_file = "nl/nl_greta_overview.tsv"
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
titles = content['Title']
articles = content['Text']
publishers = content['Publisher']

greta_sentiment = dict()
i = 0
for title, text, publisher in zip(titles, articles, publishers):
    i += 1
    if i < 10:
        try:
            entities = []
            sentences = [sent for sent in Text(text, hint_language_code= 'nl').sentences]
            sent_senti = float(mean([sent.polarity for sent in sentences]))
            title_sent = Text(title).polarity
            sent_entities = [sent.entities for sent in sentences]
            for entities in sent_entities:
                if len(entities) != 0:
                    for entity in entities:
                        if 'Greta' in entity:
                            #greta_sent = entity.positive_sentiment
                            print(entity)

                            if publisher not in sents_sentiment:
                                greta_sentiment[publisher] = [greta_sent]
                            else:
                                greta_sentiment[publisher].append(greta_sent)

            if publisher not in sents_sentiment:
                sents_sentiment[publisher]['article'] = [sent_senti]
                sents_sentiment[publisher]['title'] = [title_sent]

            else:
                sents_sentiment[publisher]['article'].append(sent_senti)
                sents_sentiment[publisher]['title'].append(title_sent)


        except Exception as e:
            print(e)
            print(entities)

"""
art_pub_sent = defaultdict(dict)
for publisher in sents_sentiment:
    if len(sents_sentiment[publisher]['article']) > 3:
        art_pub_sent[publisher]['article'] = mean(sents_sentiment[publisher]['article'])
        art_pub_sent[publisher]['title'] = mean(sents_sentiment[publisher]['title'])
        art_pub_sent[publisher]['greta'] = mean(sents_sentiment[publisher]['greta'])

print(art_pub_sent)

fig, ax = plt.subplots(1, 1, figsize = (10, 6))
x = art_pub_sent.keys()
y = [art_pub_sent[publisher]['article'] for publisher in art_pub_sent]
plt.xlabel('PUBLISHER')
plt.ylabel('SENTIMENT"')
plt.title('ARTICLE SENTIMENT OF DUTCH PUBLISHERS')
plt.bar(x, y)
fig.tight_layout()
#fig.savefig("new_plots/nl_publisher_sentiment.png")
#plt.show()

"""
"""
publishers = [publisher for publisher in art_pub_sent]
title_sent = [art_pub_sent[publisher]['title'] for publisher in art_pub_sent]
art_sent = [art_pub_sent[publisher]['article'] for publisher in art_pub_sent]

x = np.arange(len(publishers))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, title_sent, width, label='Title')
rects2 = ax.bar(x + width/2, art_sent, width, label='Article')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Sentiment')
ax.set_title('Sentiment of titles and articles')
ax.set_xticks(x)
ax.set_xticklabels(publishers)
ax.legend()

def autolabel(rects):
    #Attach a text label above each bar in *rects*, displaying its height.
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

#autolabel(rects1)
#autolabel(rects2)

fig.tight_layout()

plt.show()
"""