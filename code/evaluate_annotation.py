import pandas as pd
import glob
import os.path
from itertools import combinations
from sklearn.metrics import cohen_kappa_score, confusion_matrix
import nltk

nl_terms = ["activist", "politici", "klimaat"]
it_terms = ["attivist", "politici", "climatico"]
categories = ["pos", "neg", "neu"]

for term in nl_terms:
    print(term)
    annotations = {}

    # Read in the data
    for sheet in glob.glob("../data/annotations/nl/annotationsheet_" + term +"*.tsv"):
        filename, extension = os.path.basename(sheet).split(".")
        prefix, term, annotator = filename.split("_")

        # Read in annotations
        annotation_data = pd.read_csv(sheet, sep="\t", header=0, keep_default_na=False)
        annotations[annotator] = annotation_data["Annotation"]

    annotators = annotations.keys()

    for annotator_a, annotator_b in combinations(annotators, 2):
        agreement = [anno1 == anno2 for anno1, anno2 in  zip(annotations[annotator_a], annotations[annotator_b])]
        percentage = sum(agreement)/len(agreement)
        print(annotator_a, annotator_b)
        print("Percentage Agreement: %.2f" %percentage)
        kappa = cohen_kappa_score(annotations[annotator_a], annotations[annotator_b], labels=categories)
        print("Cohen's Kappa: %.2f" %kappa)
        confusions = confusion_matrix(annotations[annotator_a], annotations[annotator_b], labels=categories)
        #print(confusions)
        pandas_table = pd.DataFrame(confusions, index=["positive", "negative", "neutral"])
        print('Pandas')
        print(pandas_table)
        print('Markdown')
        print(pandas_table.to_markdown())

for term in it_terms:
    print(term)
    annotations = {}

    # Read in the data
    for sheet in glob.glob("../data/annotations/nl/annotationsheet_" + term +"*.tsv"):
        filename, extension = os.path.basename(sheet).split(".")
        prefix, term, annotator = filename.split("_")

        # Read in annotations
        annotation_data = pd.read_csv(sheet, sep="\t", header=0, keep_default_na=False)
        annotations[annotator] = annotation_data["Annotation"]

    annotators = annotations.keys()


    for annotator_a, annotator_b in combinations(annotators, 2):
        agreement = [anno1 == anno2 for anno1, anno2 in  zip(annotations[annotator_a], annotations[annotator_b])]
        percentage = sum(agreement)/len(agreement)
        print(annotator_a, annotator_b)
        print("Percentage Agreement: %.2f" %percentage)
        kappa = cohen_kappa_score(annotations[annotator_a], annotations[annotator_b], labels=categories)
        print("Cohen's Kappa: %.2f" %kappa)
        confusions = confusion_matrix(annotations[annotator_a], annotations[annotator_b], labels=categories)
        pandas_table = pd.DataFrame(confusions, index=["positive", "negative", "neutral"])
        print('Pandas')
        print(pandas_table)
        print('Markdown')
        print(pandas_table.to_markdown())