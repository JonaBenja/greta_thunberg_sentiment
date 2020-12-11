import pandas as pd
import stanza
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import nltk
from gensim.models import KeyedVectors
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# This is very simplistic pre-processing. You might want to modify it

"""
https://github.com/coosto/dutch-word-embeddings
"""

def preprocess(article):
    processed_article = nlp.process(article)
    all_lemmas = []
    for s in processed_article.sentences:
        stopwords = ['de', 'en', 'van', 'ik', 'te', 'dat', 'die', 'in', 'een', 'hij', 'het', 'niet', 'zijn', 'is', 'was', 'op', 'aan', 'met', 'als', 'voor', 'had', 'er', 'maar', 'om', 'hem', 'dan', 'zou', 'of', 'wat', 'mijn', 'men', 'dit', 'zo', 'door', 'over', 'ze', 'zich', 'bij', 'ook', 'tot', 'je', 'mij', 'uit', 'der', 'daar', 'haar', 'naar', 'heb', 'hoe', 'heeft', 'hebben', 'deze', 'u', 'want', 'nog', 'zal', 'me', 'zij', 'nu', 'ge', 'geen', 'omdat', 'iets', 'worden', 'toch', 'al', 'waren', 'veel', 'meer', 'doen', 'toen', 'moet', 'ben', 'zonder', 'kan', 'hun', 'dus', 'alles', 'onder', 'ja', 'eens', 'hier', 'wie', 'werd', 'altijd', 'doch', 'wordt', 'wezen', 'kunnen', 'ons', 'zelf', 'tegen', 'na', 'reeds', 'wil', 'kon', 'niets', 'uw', 'iemand', 'geweest', 'andere']
        lemmas = [word.lemma.lower() for word in s.words if not word.text.lower in stopwords]
        clean_lemmas = [lemma for lemma in lemmas if not lemma in string.punctuation]
        all_lemmas.extend(clean_lemmas)
    return all_lemmas

# Read in TSV
#tsv_file = "nl/nl_greta_overview.tsv"
tsv_file = "it/it_greta_overview.tsv"
news_content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0)
nlp = stanza.Pipeline('it', processors='tokenize,pos,lemma')

# We filter out empty articles
news_content = news_content[news_content["Text"].str.len() >0 ]
articles = news_content["Text"]

# You can play around with the ngram range
vectorizer = TfidfVectorizer(use_idf=True, tokenizer=preprocess)
tf_idf = vectorizer.fit_transform(articles)
all_terms = vectorizer.get_feature_names()
#print(all_terms[0:30])

# We extract the keywords
num_keywords = 10

def get_top_tfidf_features(row, terms, top_n=25):
    top_ids = np.argsort(row)[::-1][:top_n]
    top_features = [terms[i] for i in top_ids]
    return top_features

keywords = []
for i in range(0, tf_idf.shape[0]):
    row = np.squeeze(tf_idf[i].toarray())
    top_terms_for_article= get_top_tfidf_features(row, all_terms, top_n=num_keywords)
    #print("Keywords for article " + str(i))
    #print(top_terms_for_article)
    keywords.append(top_terms_for_article)

"""
#WORD EMBEDDINGS FOR CLUSTERING
"""

print("loading")
fasttext_model  = KeyedVectors.load_word2vec_format("embeddings/ita_newscrawl_2019_1M.bin", binary=True)
print("done loading")

all_doc_representations = []
not_in_embeddings = 0
n_keywords = 0
no_embedding = []
for doc_keywords in keywords:
    doc_representation = []
    for keyword in doc_keywords:
        n_keywords += 1
        try:
            word_representation = fasttext_model[keyword]
            doc_representation.append(word_representation)
        except KeyError as e:
            # We simply ignore unknown words
            not_in_embeddings += 1
            no_embedding.append(keyword)


    # Take the mean over the keywords
    mean_keywords = np.mean(doc_representation, axis=0)
    all_doc_representations.append(mean_keywords)

print(not_in_embeddings,"/",n_keywords)

# How many clusters do you expect?
from sklearn.cluster import KMeans
num_clusters = 4
km = KMeans(n_clusters=num_clusters)
km.fit(all_doc_representations)

clusters = km.labels_.tolist()
clustered_articles ={'Title': news_content["Title"],'Author': news_content["Author"],'Publisher': news_content["Publisher"], 'Cluster': clusters}
overview = pd.DataFrame(clustered_articles, columns = ['Author', 'Title', 'Publisher', 'Cluster'])

overview.to_tsv ('clusters/it_4_topic_clusters.tsv', index = False, header=True)