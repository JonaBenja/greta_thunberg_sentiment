import pandas as pd


tsv_file = '../data/clusters/it_4_topic_clusters.tsv'
news_content = pd.read_csv(tsv_file, sep="\t", keep_default_na=False, header=0)
