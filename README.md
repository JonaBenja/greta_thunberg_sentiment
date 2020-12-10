# lad-assignment1

#README.txt

### INTRODUCTION
This repository contains the code, data and analysis of assignment 1 for the course Language as Data. This students that contributed to this assignment are Gabriele Catanese and Jona Bosman.

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

### WINDOWS
1) Follow the instructions given in these links:
- https://github.com/Jcharis/Natural-Language-Processing-Tutorials/blob/master/NLP_with_Polyglot/NLP%20with%20Polyglot%20.ipynb
- https://www.alirookie.com/post/install-polyglot-on-windows

2) As general instructions the following should work:

You will have to download the PyCLD2 and PyICU from here:
- https://www.lfd.uci.edu/~gohlke/pythonlibs/

*ATTENTION*: make sure you download the file with the right python version and check if you need 32 or 64 bits version.* 
The python version is the number that follows 'cp' in the name of the file(in our case in was cp38 for python 3.8)
The files that we used on Windows: 
- pycld2‑0.41‑cp38‑cp38‑win_amd64.whl
- PyICU‑2.6‑cp38‑cp38‑win_amd64.whl

Then run these in the command line to install the files
(make sure you activate the LaD environment and that you are in the right directory (ex. C:\Users\YourName)):

- pip install pycld2‑0.41‑cp38‑cp38‑win_amd64.whl
- pip install PyICU‑2.6‑cp38‑cp38‑win_amd64.whl
- git clone https://github.com/aboSamoor/polyglot.git
When you clone the file from git, extract the content in the same directory that you were using for PyCDL and PyICU.
 
3) Explore the content of the downloaded git folder that should be named 'polyglot':
- find the child folder named with the same name 'polyglot' inside it (ex. C:>Users>YourName>polyglot>polyglot (like a matryoshka :D ))
- take the 'polyglot' folder out of the parent folder
- put it in the same directory (do not substitute the original file! To avoid that, you can rename the parent folder)

4) FINALLY run on the command line:
- python setup.py install
or 
- pip install polyglot

If you run into errors, even though you carefully followed the steps above, check the following link:
- https://www.alirookie.com/post/install-polyglot-on-windows
or
- google the errors
- check if you installed everything in the same directory 
- check if you are in the right evironment
- check if you have numpy installed (polyglot is based on numpy)
- check if you are using the right versions of the files above

If nothing compleately works after 1h of attempts, reach out to: gabrielecatanese@gmail.com
