# lad-assignment1

#README.txt

### INTRODUCTION
This repository contains the code, data and analysis of assignment 1 for the course Language as Data. This student contributed to this assignment are Gabriele Catanese and Jona Bosman.

### CORPUS RETRIEVAL
The corpus contains 100 recent articles in Dutch and Italian about Greta Thunberg, that were retrieved from the Google News corpus by using the query 'Greta Thunberg'.

ISO-639-3 code for Dutch: 'nl'.
ISO-639-3 code for Italian: 'it'.

### REPOSITORY STRUCTURE

`it` is a folder that contains the Italian corpus (`it_greta.tsv`).
`nl` is a folder that contains the Dutch corpus (`nl_greta.tsv`).
`processed_articles` contains the corpora after they were processed by the Stanza language package (`it_articles_stanza` and `nl_articles_stanza`)
`basic_statistics.py` contains the code for extracting basic statistics from both corpora.
`utils.py` contains helper functions for `basic_statistics.py`.
`basic_statistics.pdf` contains tables with the extracted statistics for each language.

### LINKS TO SOURCES AND LICENCES
Stanza: http://www.apache.org/licenses/LICENSE-2.0
The license for the Google News articles couldn't be retrieved in time but will be posted here later.

Dutch query: http://news.google.com/?q=greta+thunberg&gl=nl
Italian query: http://news.google.com/?q=greta+thunberg&gl=it

### INSTALLING POLYGLOT ON MAC OS

1) Clone the GitHub repository of polyglot: `git clone https://github.com/aboSamoor/polyglot`

2) Inside the main folder 'polyglot' there is another folder called 'polyglot'. Rename the main polyglot folder to 'main_polyglot', take the second 'polyglot' folder and move it outside of 'main_polyglot'.

3) Install the Polyglot library with this command: `pip install polyglot`

4) Run this command: `pip install -U git+https://github.com/aboSamoor/polyglot.git@master`

5) Make sure you have Anaconda installed, and run this command: `conda install -c conda-forge pyicu morfessor icu -y && pip install pycld2 polyglot`

6) Run the file `polyglot_test.py` to make sure polyglot is correctly installed. If there are no errors, the installation was succesfull!


