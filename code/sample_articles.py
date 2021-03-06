import pandas as pd
from polyglot.text import Text
from statistics import mean

# Load dataset
tsv_file = '../data/nl/decoded_nl_greta_overview.tsv'
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
publishers = content['Publisher']

# Print title, URL and Polyglot sentiment of 10 articles
pub_list = []
for i in range(content.shape[0]):
for i in range(content.shape[0]):
    if len(pub_list) < 10:

        # Get components from article
        publisher = content['Publisher'][i]
        url = content['URL'][i]
        title = content['Title'][i]
        text = content['Text'][i]

        # Remove any non-ASCII characters (needed for Polyglot)
        filtered_text = ''.join(x for x in text if x.isprintable())

        # Get only 1 article per publisher
        if publisher not in pub_list:
            pub_list.append(publisher)
            print(title)
            print(url)

            # Compute Polyglot sentiment
            print("Polyglot sentiment:")
            text_sentiment = float(mean([sent.polarity for sent in Text(filtered_text, hint_language_code='nl').sentences]))
            print(text_sentiment)

tsv_file = '../data/it/decoded_it_greta_overview.tsv'
content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0, encoding = 'utf-8')
publishers = content['Publisher']

pub_list = []
for i in range(len(publishers)):
    if len(pub_list) < 10:
        publisher = content['Publisher'][i]
        url = content['URL'][i]
        title = content['Title'][i]
        text = content['Text'][i]
        filtered_text = ''.join(x for x in text if x.isprintable())
        if publisher not in pub_list:
            pub_list.append(publisher)
            print(title)
            print(url)
            print("Polyglot sentiment:")
            text_sentiment = float(mean([sent.polarity for sent in Text(filtered_text, hint_language_code='nl').sentences]))
            print(text_sentiment)