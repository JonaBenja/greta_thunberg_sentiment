# utils
from collections import Counter
from string import punctuation

def calculate_ngram_frequencies(n, nlp_output):
    ngram_frequencies = Counter()

    for data in nlp_output:
        for sentence in data.sentences:
            tokens = [token.text.casefold() for token in sentence.tokens]
            ngrams = [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
            ngram_frequencies.update(ngrams)
    return ngram_frequencies

def filter_stopwords(data, stopwords):
    for tokens in list(data):
        if type(tokens) == tuple:
            token = tokens[0]
            token = token.casefold()
            if token in stopwords or token in punctuation or token == '”':
                del data[tokens]

        elif len(tokens) == 1:
            token = tokens
            token = token.casefold()
            if token in stopwords or token in punctuation or token == '”':
                del data[tokens]
        elif len(tokens) > 1:
            for token in tokens.split():
                token = token.casefold()
                if token in stopwords or token in punctuation or token == '”':
                    del data[tokens]

    return data