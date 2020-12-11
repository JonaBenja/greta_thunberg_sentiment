import pandas as pd
import stanza
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from collections import defaultdict, Counter
import nltk
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def preprocess(article):
    processed_article = nlp.process(article)
    all_lemmas = []
    for s in processed_article.sentences:
        stopwords = ['de', 'en', 'van', 'ik', 'te', 'dat', 'die', 'in', 'een', 'hij', 'het', 'niet', 'zijn', 'is', 'was', 'op', 'aan', 'met', 'als', 'voor', 'had', 'er', 'maar', 'om', 'hem', 'dan', 'zou', 'of', 'wat', 'mijn', 'men', 'dit', 'zo', 'door', 'over', 'ze', 'zich', 'bij', 'ook', 'tot', 'je', 'mij', 'uit', 'der', 'daar', 'haar', 'naar', 'heb', 'hoe', 'heeft', 'hebben', 'deze', 'u', 'want', 'nog', 'zal', 'me', 'zij', 'nu', 'ge', 'geen', 'omdat', 'iets', 'worden', 'toch', 'al', 'waren', 'veel', 'meer', 'doen', 'toen', 'moet', 'ben', 'zonder', 'kan', 'hun', 'dus', 'alles', 'onder', 'ja', 'eens', 'hier', 'wie', 'werd', 'altijd', 'doch', 'wordt', 'wezen', 'kunnen', 'ons', 'zelf', 'tegen', 'na', 'reeds', 'wil', 'kon', 'niets', 'uw', 'iemand', 'geweest', 'andere']
        #stopwords = ['ad', 'al', 'allo', 'ai', 'agli', 'all', 'agl', 'alla', 'alle', 'con', 'col', 'coi', 'da', 'dal', 'dallo', 'dai', 'dagli', 'dall', 'dagl', 'dalla', 'dalle', 'di', 'del', 'dello', 'dei', 'degli', 'dell', 'degl', 'della', 'delle', 'in', 'nel', 'nello', 'nei', 'negli', 'nell', 'negl', 'nella', 'nelle', 'su', 'sul', 'sullo', 'sui', 'sugli', 'sull', 'sugl', 'sulla', 'sulle', 'per', 'tra', 'contro', 'io', 'tu', 'lui', 'lei', 'noi', 'voi', 'loro', 'mio', 'mia', 'miei', 'mie', 'tuo', 'tua', 'tuoi', 'tue', 'suo', 'sua', 'suoi', 'sue', 'nostro', 'nostra', 'nostri', 'nostre', 'vostro', 'vostra', 'vostri', 'vostre', 'mi', 'ti', 'ci', 'vi', 'lo', 'la', 'li', 'le', 'gli', 'ne', 'il', 'un', 'uno', 'una', 'ma', 'ed', 'se', 'perché', 'anche', 'come', 'dov', 'dove', 'che', 'chi', 'cui', 'non', 'più', 'quale', 'quanto', 'quanti', 'quanta', 'quante', 'quello', 'quelli', 'quella', 'quelle', 'questo', 'questi', 'questa', 'queste', 'si', 'tutto', 'tutti', 'a', 'c', 'e', 'i', 'l', 'o', 'ho', 'hai', 'ha', 'abbiamo', 'avete', 'hanno', 'abbia', 'abbiate', 'abbiano', 'avrò', 'avrai', 'avrà', 'avremo', 'avrete', 'avranno', 'avrei', 'avresti', 'avrebbe', 'avremmo', 'avreste', 'avrebbero', 'avevo', 'avevi', 'aveva', 'avevamo', 'avevate', 'avevano', 'ebbi', 'avesti', 'ebbe', 'avemmo', 'aveste', 'ebbero', 'avessi', 'avesse', 'avessimo', 'avessero', 'avendo', 'avuto', 'avuta', 'avuti', 'avute', 'sono', 'sei', 'è', 'siamo', 'siete', 'sia', 'siate', 'siano', 'sarò', 'sarai', 'sarà', 'saremo', 'sarete', 'saranno', 'sarei', 'saresti', 'sarebbe', 'saremmo', 'sareste', 'sarebbero', 'ero', 'eri', 'era', 'eravamo', 'eravate', 'erano', 'fui', 'fosti', 'fu', 'fummo', 'foste', 'furono', 'fossi', 'fosse', 'fossimo', 'fossero', 'essendo', 'faccio', 'fai', 'facciamo', 'fanno', 'faccia', 'facciate', 'facciano', 'farò', 'farai', 'farà', 'faremo', 'farete', 'faranno', 'farei', 'faresti', 'farebbe', 'faremmo', 'fareste', 'farebbero', 'facevo', 'facevi', 'faceva', 'facevamo', 'facevate', 'facevano', 'feci', 'facesti', 'fece', 'facemmo', 'faceste', 'fecero', 'facessi', 'facesse', 'facessimo', 'facessero', 'facendo', 'sto', 'stai', 'sta', 'stiamo', 'stanno', 'stia', 'stiate', 'stiano', 'starò', 'starai', 'starà', 'staremo', 'starete', 'staranno', 'starei', 'staresti', 'starebbe', 'staremmo', 'stareste', 'starebbero', 'stavo', 'stavi', 'stava', 'stavamo', 'stavate', 'stavano', 'stetti', 'stesti', 'stette', 'stemmo', 'steste', 'stettero', 'stessi', 'stesse', 'stessimo', 'stessero', 'stando', 'essere', 'avere', 'fare']
        lemmas = [word.lemma.lower() for word in s.words if not word.text.lower in stopwords]
        clean_lemmas = [lemma for lemma in lemmas if not lemma in string.punctuation]
        all_lemmas.extend(clean_lemmas)
    return all_lemmas

# Read in TSV
tsv_file = "../data/nl/nl_greta_overview.tsv"
news_content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0)
nlp = stanza.Pipeline('nl', processors='tokenize,pos,lemma')

# We filter out empty articles
articles = news_content["Text"]

# You can play around with the ngram range
vectorizer = TfidfVectorizer(use_idf=True, tokenizer=preprocess)
tf_idf = vectorizer.fit_transform(articles)
all_terms = vectorizer.get_feature_names()

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
    keywords.append(top_terms_for_article)

"""
#WORD EMBEDDINGS FOR CLUSTERING
"""

print("loading")
fasttext_model  = KeyedVectors.load_word2vec_format("../data/embedding_models/nld_newscrawl_2019_1M.bin", binary=True)
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

# How many clusters do you expect?
num_clusters = 4
km = KMeans(n_clusters=num_clusters)
km.fit(all_doc_representations)

clusters = km.labels_.tolist()
clustered_articles ={'Title': news_content["Title"],'Text': news_content["Text"],'Publisher': news_content["Publisher"], 'Cluster': clusters}
overview = pd.DataFrame(clustered_articles, columns = ['Title', 'Publisher', 'Text', 'Cluster'])

overview.to_csv ('../data/clusters/nl_4_topic_clusters.tsv', sep='\t', index = False, header=True)

keywords_clusters = defaultdict(dict)

for doc_keywords, cluster in zip(keywords, clusters):
