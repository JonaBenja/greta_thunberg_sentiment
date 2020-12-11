This folder contains the code that was used in the project. It also contains the datafiles for the module Polyglot.

**extract_statistics.py**
Run this file to read in the dataset, preprocess them, extract statistics as a dictionary
and save the statistics as a .json file in the `data/statistics` folder. When run,
the new .json files will overwrite the old ones.

**utils.py**
Functions for `extract_statistics.py`

**evaluate_annotation.py**
Evaluates the annotation performed on a selection of articles and outputs the evaluation in tables.

**sample_articles.py**
Creates a sample of 10 articles from the data, along with the sentiment from Polyglot. These were used to read manually and measure the performance of Polyglot.

**polyglot_test.py**
You can run this file to test if Polyglot is installed correctly. If there are no errors, it is installed correctly.

**clusters.py**
Clusters the data in 4 groups and saved the ouput as a .tsv file in `data/clusters`

**cluster_keywords.py**
Prints the 10 most frequent keywords for each cluster of both the datasets.

**doc_vectors.py**
Computes document vectors for the data and reduces their dimensionality to be able to plot them along with the clusters of the article. It saves the output as a plot in `data/plots`

**sentiment.py**
Computes the mean sentiment per publisher and saves the results in a plot in `data/plots`
