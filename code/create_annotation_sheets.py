import pandas as pd
import stanza

# Read in the data
language = "nl"
article_file = "nl/nl_greta.tsv"
content = pd.read_csv(article_file, sep="\t", header=0, keep_default_na=False, encoding = 'utf-8', error_bad_lines=False)

# Make sure to be very clear on how you determined the annotation terms.
# You can also use ngrams, e.g. "vegan diet" instead of "diet"
terms = ["opwarming", "politici", "regering"]


# Prepare the nlp pipeline
#stanza.download(language)
nlp = stanza.Pipeline(language,  processors='tokenize,pos,lemma')

# Get all instances.
# Here, we do a simple string comparison.
# You might want to check for the lemma instead (depending on your research question)

annotation_instances = {}
for article in content["Text"]:
    # Filter out empty articles
    if len(article.strip()) > 0:
        processed_article = nlp(article)
        for sentence in processed_article.sentences:
            if len(sentence.text) > 15:
                for term in terms:
                    if term in sentence.text.casefold():
                        # Save all instances for each term
                        # This is a condensed way of updating a dictionary. Make sure you understand what is happening
                        annotation_instances[term] = annotation_instances.get(term, []) + [sentence.text.strip()]

num_annotators = 2
for i in range(1, num_annotators + 1):
    for term in terms:
        with open("annotations/nl/annotationsheet_" + term +"_a" + str(i) + ".tsv", "w") as outfile:
            outfile.write("Term\tInstance\tAnnotation\n")
            for j in range(15):
                outfile.write(term +"\t" + annotation_instances[term][j] + "\t\n")
