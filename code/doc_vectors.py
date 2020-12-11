import spacy
import pandas as pd
from scipy.spatial.distance import cosine

tsv_file = "nl/nl_greta_overview.tsv"
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
articles = content['Text']

spacy_pipeline = spacy.load("nl_core_news_sm")
doc1_vector = spacy_pipeline(articles[0]).vector
doc2_vector = spacy_pipeline(articles[1]).vector

similarity = 1 - cosine(doc1_vector, doc2_vector)
print(similarity)