# get_all_documents.py
from util_html import *

"""
EXTRACT DUTCH DATASET
"""

# Specify query
base_url = "http://news.google.com/"
query='greta+thunberg+opwarming'
query_2='greta+thunberg+klimaat'
language='nl'

full_query = "?q={0}&hl={1}".format(query.lower(), language)
query_url = (base_url + full_query)
query_content = url_to_html(query_url)
articles = query_content.find_all('article')

outfile = "nl/nl_greta_overview.tsv"

# Extract metadata and write
with open(outfile, "a") as f:
    f.write("Publication Date\tTime\tPublisher\tAuthor\tTitle\tURL\tText\n")
    try:
        for article in articles:

            # Extract metadata
            date, time, publisher, title, article_url = extract_metadata_googlenews(article)

            # Extract content
            article_content = url_to_html(article_url)
            author = parse_author(article_content)
            content = parse_news_text(article_content)

            # We remove the newlines from the content, so that we can easily store it in a single line.
            # Keep in mind, that newlines can also carry meaning.
            # For example, they separate paragraphs and this information is lost in the analysis, if we remove them.
            content = content.replace("\n", "")

            # We want the fields to be separated by tabulators (\t)
            output = "\t".join([date, time, publisher, author, title, article_url, content])
            f.write(output +"\n")
    except:
        pass


"""
EXTRACT ITALIAN DATASET
"""

# Specify query
base_url = "http://news.google.com/"
query='greta+thunberg+surriscaldamento'
query_2='greta+thunberg+climatio'
language='it'


full_query = "?q={0}&hl={1}".format(query.lower(), language)
query_url = (base_url + full_query)
query_content = url_to_html(query_url)
articles = query_content.find_all('article')

outfile = "it/it_greta_overview.tsv"

# Extract metadata and write
with open(outfile, "a") as f:
    f.write("Publication Date\tTime\tPublisher\tAuthor\tTitle\tURL\tText\n")
    try:
        for article in articles:

            # Extract metadata
            date, time, publisher, title, article_url = extract_metadata_googlenews(article)

            # Extract content
            article_content = url_to_html(article_url)
            author = parse_author(article_content)
            content = parse_news_text(article_content)

            # We remove the newlines from the content, so that we can easily store it in a single line.
            # Keep in mind, that newlines can also carry meaning.
            # For example, they separate paragraphs and this information is lost in the analysis, if we remove them.
            content = content.replace("\n", "")

            # We want the fields to be separated by tabulators (\t)
            output = "\t".join([date, time, publisher, author, title, article_url, content])
            f.write(output +"\n")
    except:
        pass
