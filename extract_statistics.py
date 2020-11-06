# extract_statistics.py
import pandas as pd
import stanza
import nltk
from collections import defaultdict, Counter
from datetime import datetime
import pickle
from utils import calculate_ngram_frequencies

# Read in the Dutch data
nl_nlp = stanza.Pipeline('nl')
nl_content = pd.read_csv("dutch/nl_greta.tsv", sep="\t", header = 0, keep_default_na=False, encoding = 'utf-8', error_bad_lines=False)
nl_statistics = defaultdict(dict)

# Read in the Italian data
it_nlp = stanza.Pipeline('it')
it_content = pd.read_csv("italian/it_greta.tsv", sep="\t", header = 0, keep_default_na=False, encoding = 'utf-8', error_bad_lines=False)
it_statistics = defaultdict(dict)

"""
METADATA
"""
authors = Counter(nl_content['Author'])
nl_statistics['metadata']['n_authors'] = len(authors)
freq_authors = sorted(authors.items(), key=lambda item: item[1], reverse=True)

authors = Counter(it_content['Author'])
it_statistics['metadata']['n_authors'] = len(authors)

publishers = Counter(nl_content['Publisher'])
max_publishers = publishers.most_common(3)
nl_statistics['metadata']['n_publishers'] = len(publishers)
nl_statistics['metadata']['max_publishers'] = max_publishers

publishers = Counter(it_content['Publisher'])
max_publishers = publishers.most_common(4)
it_statistics['metadata']['n_publishers'] = len(publishers)
it_statistics['metadata']['max_publishers'] = max_publishers

# Time span
dates = list(set(nl_content['Publication Date']))
dates.remove('')
dates.sort(key = lambda date: datetime.strptime(date, '%Y-%m-%d'))
timespan = (dates[0], dates[-1])
nl_statistics['metadata']['timespan'] = timespan

dates = list(set(it_content['Publication Date']))
dates.remove('')
dates.sort(key = lambda date: datetime.strptime(date, '%Y-%m-%d'))
timespan = (dates[0], dates[-1])
it_statistics['metadata']['timespan'] = timespan

"""
CONTENT
number of types and tokens, most frequent content words, average sentence length (min, max, mean)...

types
number of tokens
type-token ratio
most common POS per lemma
most common token excl stopwords
most common bigrams excl stopwords
"""

title_lengths = []
for title in nl_content["Title"]:
    title_lengths.append(len(title))

nl_statistics['content']['mean_title_length'] = sum(title_lengths)/len(title_lengths)

title_lengths = []
for title in it_content["Title"]:
    title_lengths.append(len(title))

it_statistics['content']['mean_title_length'] = sum(title_lengths)/len(title_lengths)

"""
#This was the code that was used to create the processed Stanza files.

nl_texts = []
for article in nl_content['Text']:
    if article:
        processed_text = nl_nlp(article)
        nl_texts.append(processed_text)
pickle.dump(nl_texts, open('processed_articles/nl_articles_stanza', "wb"))

it_texts = []
for article in it_content['Text']:
    if article:
        processed_text = it_nlp(article)
        it_texts.append(processed_text)
pickle.dump(it_texts, open('processed_articles/it_articles_stanza', "wb"))
"""

nl_nlp_output = pickle.load(open('processed_articles/nl_articles_stanza',"rb"))
it_nlp_output = pickle.load(open('processed_articles/it_articles_stanza',"rb"))

token_pos_frequencies = Counter()
token_frequencies = Counter()
for data in nl_nlp_output:
    sentences = data.sentences
    for sentence in sentences:
        token_pos = [(word.lemma, word.pos) for word in sentence.words]
        token_pos_frequencies.update(token_pos)
        words = [word.text for word in sentence.words]
        token_frequencies.update(words)

nl_statistics['content']['freq_tokens'] = token_frequencies.most_common(50)
nl_statistics['content']['freq_token_pos'] = token_pos_frequencies.most_common(50)

token_pos_frequencies = Counter()
token_frequencies = Counter()
for data in it_nlp_output:
    sentences = data.sentences
    for sentence in sentences:
        token_pos = [(word.lemma, word.pos) for word in sentence.words]
        token_pos_frequencies.update(token_pos)
        words = [word.text for word in sentence.words]
        token_frequencies.update(words)

it_statistics['content']['freq_tokens'] = token_frequencies.most_common(50)
it_statistics['content']['freq_token_pos'] = token_pos_frequencies.most_common(50)

ngram_frequencies = calculate_ngram_frequencies(2, nl_nlp_output)
nl_statistics['content']['freq_n-gram'] = ngram_frequencies.most_common(20)

ngram_frequencies = calculate_ngram_frequencies(2, it_nlp_output)
it_statistics['content']['freq_n-gram'] = ngram_frequencies.most_common(20)

nl_stopwords = nltk.corpus.stopwords.words('dutch')
it_stopwords = nltk.corpus.stopwords.words('italian')

# mean sentence length
# n types
# n tokens


#print(nl_statistics)
#print(it_statistics)
