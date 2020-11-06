# utils
from collections import Counter

def calculate_ngram_frequencies(n, nlp_output):

    ngram_frequencies = Counter()

    for data in nlp_output:
        for sentence in data.sentences:
            tokens = [token.text for token in sentence.tokens]
            ngrams = [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
            ngram_frequencies.update(ngrams)
    return ngram_frequencies
