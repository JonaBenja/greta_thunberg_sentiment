# extract_statistics.py
import pandas as pd
import stanza
import nltk
from collections import defaultdict, Counter
from datetime import datetime
import pickle
from utils import calculate_ngram_frequencies, filter_stopwords
import json

# Read in the Dutch data and Stanza pipeline
nl_nlp = stanza.Pipeline('nl')

nl_content = pd.read_csv('../data/nl/nl_greta_overview.tsv', sep="\t", header = 0, keep_default_na=False, encoding = 'utf-8', error_bad_lines=False)

#nl_content.fillna('Unknown')

nl_statistics = defaultdict(dict)

# Read in the Italian data and Stanza pipeline
it_nlp = stanza.Pipeline('it')

it_content = pd.read_csv('../data/it/it_greta_overview.tsv', sep="\t", header = 0, keep_default_na=False, encoding = 'utf-8', error_bad_lines=False)

#it_content.fillna('Unknown')

it_statistics = defaultdict(dict)

"""
METADATA
"""
# Count number of authors
authors = Counter(nl_content['Author'].str.casefold())
nl_statistics['metadata']['n_authors'] = len(authors)

authors = Counter(it_content['Author'].str.casefold())
it_statistics['metadata']['n_authors'] = len(authors)

# Count number of publishers and the number of their articles
publishers = Counter(nl_content['Publisher'].str.casefold())
max_publishers = publishers.most_common(5)
nl_statistics['metadata']['n_publishers'] = len(publishers)
nl_statistics['metadata']['max_publishers'] = max_publishers

publishers = Counter(it_content['Publisher'].str.casefold())
max_publishers = publishers.most_common(5)
it_statistics['metadata']['n_publishers'] = len(publishers)
it_statistics['metadata']['max_publishers'] = max_publishers

# Extract time span
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

# Extract mean character title length
title_lengths = []
for title in nl_content["Title"]:
    title_lengths.append(len(title))

nl_statistics['content']['mean_title_length'] = sum(title_lengths)/len(title_lengths)

title_lengths = []
for title in it_content["Title"]:
    title_lengths.append(len(title))

it_statistics['content']['mean_title_length'] = sum(title_lengths)/len(title_lengths)

"""
CONTENT
"""
# Get stopwords of languages from NLTK
nl_stopwords = nltk.corpus.stopwords.words('dutch')
it_stopwords = nltk.corpus.stopwords.words('italian')

# Extract length of texts in tokens
text_lengths = []
for text in nl_content["Text"]:
    if text:
        text_lengths.append(len(text))

nl_n_texts = len(text_lengths)
nl_statistics['content']['texts_present'] = nl_n_texts
nl_statistics['content']['mean_text_length'] = sum(text_lengths)/nl_n_texts

text_lengths = []
for text in it_content["Text"]:
    if text:
        text_lengths.append(len(text))

it_n_texts = len(text_lengths)
it_statistics['content']['texts_present'] = it_n_texts
it_statistics['content']['mean_text_length'] = sum(text_lengths)/it_n_texts

"""
#This was the code that was used to create the processed Stanza files.
print("Loading Stanza NL")
nl_texts = []
i = 0
for article in nl_content['Text']:
    if article:
        i += 1
        processed_text = nl_nlp(article)
        nl_texts.append(processed_text)
        print(i)
pickle.dump(nl_texts, open('processed_articles/nl_articles_stanza', "wb"))

print("Loading Stanza IT")
it_texts = []
i = 0
for article in it_content['Text']:
    if article:
        i += 1
        processed_text = it_nlp(article)
        it_texts.append(processed_text)
        print(i)
pickle.dump(it_texts, open('processed_articles/it_articles_stanza', "wb"))

"""
# Load Stanza files of data
nl_nlp_output = pickle.load(open('../data/processed_articles/nl_articles_stanza',"rb"))
it_nlp_output = pickle.load(open('../data/processed_articles/it_articles_stanza',"rb"))

"""
#DUTCH TOKENS
"""
# Initialize counters for token and token-pos frequencies
token_pos_frequencies = Counter()
token_frequencies = Counter()

# Initialize tokens per sentence counter
n_sentences = []

# Loop through Stanza data and update counters
for data in nl_nlp_output:
    sentences = data.sentences
    n_sentences.append(len(sentences))
    for sentence in sentences:
        token_pos = [(word.lemma.casefold(), word.pos) for word in sentence.words]
        token_pos_frequencies.update(token_pos)
        words = [word.lemma.casefold() for word in sentence.words]
        token_frequencies.update(words)

# Save tokens, types and token/type frequencies
n_types = len(token_frequencies.keys())
n_tokens = sum(token_frequencies.values())
tt_ratio = n_types/n_tokens
num_sentences = sum(n_sentences)
nl_statistics['content']['n_tokens'] = n_tokens
nl_statistics['content']['n_types'] = n_types
nl_statistics['content']['tt_ratio'] = tt_ratio

# Save sentence information
nl_statistics['content']['mean_n_sentences'] = sum(n_sentences)/nl_n_texts
nl_statistics['content']['mean_sentence_length'] = n_tokens / num_sentences

# Save tokens frequencies and token-pos frequencies
nl_statistics['content']['freq_tokens'] = token_frequencies.most_common(10)
nl_statistics['content']['freq_token_pos'] = token_pos_frequencies.most_common(10)

# Save tokens frequencies and token-pos frequencies without stopwords
token_stopwords = filter_stopwords(token_frequencies, nl_stopwords)

nl_statistics['content']['freq_token_excl_stopwords'] = token_stopwords.most_common(10)
token_pos_stopwords = filter_stopwords(token_pos_frequencies, nl_stopwords)

nl_statistics['content']['freq_token_pos_excl_stopwords'] = token_pos_stopwords.most_common(10)

"""
#ITALIAN TOKENS
"""

token_pos_frequencies = Counter()
token_frequencies = Counter()

n_sentences = []

for data in it_nlp_output:
    sentences = data.sentences
    n_sentences.append(len(sentences))
    for sentence in sentences:
        token_pos = [(word.lemma.casefold(), word.pos) for word in sentence.words]
        token_pos_frequencies.update(token_pos)
        words = [word.lemma.casefold() for word in sentence.words]
        token_frequencies.update(words)

n_types = len(token_frequencies.keys())
n_tokens = sum(token_frequencies.values())
tt_ratio = n_types/n_tokens
num_sentences = sum(n_sentences)
it_statistics['content']['n_tokens'] = n_tokens
it_statistics['content']['n_types'] = n_types
it_statistics['content']['tt_ratio'] = tt_ratio

it_statistics['content']['mean_n_sentences'] = sum(n_sentences)/it_n_texts

it_statistics['content']['mean_sentence_length'] = n_tokens / num_sentences

it_statistics['content']['freq_tokens'] = token_frequencies.most_common(5)
it_statistics['content']['freq_token_pos'] = token_pos_frequencies.most_common(5)

token_stopwords = filter_stopwords(token_frequencies, it_stopwords)

it_statistics['content']['freq_token_excl_stopwords'] = token_stopwords.most_common(5)

token_pos_stopwords = filter_stopwords(token_pos_frequencies, it_stopwords)

it_statistics['content']['freq_token_pos_excl_stopwords'] = token_pos_stopwords.most_common(5)

"""
#N-GRAMS
"""
# Extract bigram frequencies
ngram_frequencies = calculate_ngram_frequencies(2, nl_nlp_output)
nl_statistics['content']['freq_n-gram'] = ngram_frequencies.most_common(5)

# Extract bigram frequencies without stopwords
ngram_stopwords = filter_stopwords(ngram_frequencies, nl_stopwords)
nl_statistics['content']['n-gram_excl_stopwords'] = ngram_stopwords.most_common(5)

ngram_frequencies = calculate_ngram_frequencies(2, it_nlp_output)
it_statistics['content']['freq_n-gram'] = ngram_frequencies.most_common(5)

ngram_stopwords = filter_stopwords(ngram_frequencies, it_stopwords)
it_statistics['content']['n-gram_excl_stopwords'] = ngram_stopwords.most_common(5)

"""
#SAVE BASIC STATISTICS
"""

with open('../data/statistics/nl_statistics.json', 'w') as outfile:
    json.dump(nl_statistics, outfile)

with open('../data/statistics/it_statistics.json', 'w') as outfile:
    json.dump(it_statistics, outfile)