### INTRODUCTION
This repository contains the code, data and analysis of assignment 1 for the course Language as Data. The students that contributed to this assignment are Gabriele Catanese and Jona Bosman. A blogpost with the results can be viewed here: [link]

### CORPUS RETRIEVAL
The corpus contains 101 recent articles in Dutch and and 103 recent articles in Italian about Greta Thunberg, that were retrieved from the Google News corpus.

ISO-639-3 code for Dutch: 'nl'.

ISO-639-3 code for Italian: 'it'.

### REPOSITORY STRUCTURE

`code` contains all code that was used for the analysis that is described in the blogpost

`data` contains all data needed for the analysis: the articles, annotations and results. A more detailed description can be found in the README.md in the data folder.

### LINKS TO SOURCES AND LICENCES
Dutch queries: http://news.google.com/?q=greta+thunberg+opwarming&gl=nl and http://news.google.com/?q=greta+thunberg+klimaat&gl=nl

Italian query: http://news.google.com/?q=greta+thunberg+riscaldamento&gl=it and http://news.google.com/?q=greta+thunberg+climatico&gl=it

Stanza license: http://www.apache.org/licenses/LICENSE-2.0

### INSTALLING POLYGLOT ON MAC OS

1) Clone the GitHub repository of polyglot: `git clone https://github.com/aboSamoor/polyglot`

2) Inside the main folder 'polyglot' there is another folder called 'polyglot'. Rename the main polyglot folder to 'main_polyglot', take the second 'polyglot' folder and move it outside of 'main_polyglot'.

3) Install the Polyglot library with this command: `pip install polyglot`

4) Run this command: `pip install -U git+https://github.com/aboSamoor/polyglot.git@master`

5) Make sure you have Anaconda installed, and run this command: `conda install -c conda-forge pyicu morfessor icu -y && pip install pycld2 polyglot`

6) Run the file `polyglot_test.py` to make sure polyglot is correctly installed. If there are no errors, the installation was succesfull!

### INSTALLING POLYGLOT ON WINDOWS
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

- `pip install pycld2‑0.41‑cp38‑cp38‑win_amd64.whl`
- `pip install PyICU‑2.6‑cp38‑cp38‑win_amd64.whl`
- `git clone https://github.com/aboSamoor/polyglot.git`
When you clone the file from git, extract the content in the same directory that you were using for PyCDL and PyICU.
 
3) Explore the content of the downloaded git folder that should be named 'polyglot':
- find the child folder named with the same name 'polyglot' inside it (ex. C:>Users>YourName>polyglot>polyglot (like a matryoshka :D ))
- take the 'polyglot' folder out of the parent folder
- put it in the same directory (do not substitute the original file! To avoid that, you can rename the parent folder) 

4) FINALLY run on the command line:
- `python setup.py install`
or 
- `pip install polyglot`

If you run into errors, even though you carefully followed the steps above, check the following link:
- https://www.alirookie.com/post/install-polyglot-on-windows
or
- google the errors
- check if you installed everything in the same directory 
- check if you are in the right evironment
- check if you have numpy installed (polyglot is based on numpy)
- check if you are using the right versions of the files above

If nothing completely works after 1h of attempts, reach out to: gabrielecatanese@gmail.com
