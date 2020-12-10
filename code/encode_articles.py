from polyglot.text import Text
from statistics import mean

outfile = open('../data/nl/decoded_nl_greta_overview.tsv', 'w', encoding='utf-8')
outfile.write('Publication Date\tTime\tPublisher\tAuthor\tTitle\tURL\tText\n')

with open('../data/nl/nl_greta_overview.tsv', 'r', encoding = 'utf-8') as infile:
    for article in infile:
        if 'Publisher' in article:
            continue
        components = article.strip().split('\t')
        text = components[-1]
        filtered_text = ''.join(x for x in text if x.isprintable())
        article = article.replace(text, filtered_text)
        outfile.write(article)
outfile.close()

outfile = open('../data/it/decoded_it_greta_overview.tsv', 'w', encoding='utf-8')
outfile.write('Publication Date\tTime\tPublisher\tAuthor\tTitle\tURL\tText\n')

with open('../data/it/it_greta_overview.tsv', 'r', encoding = 'utf-8') as infile:
    for article in infile:
        if 'Publisher' in article:
            continue
        components = article.strip().split('\t')
        text = components[-1]
        filtered_text = ''.join(x for x in text if x.isprintable())
        article = article.replace(text, filtered_text)
        outfile.write(article)
outfile.close()



