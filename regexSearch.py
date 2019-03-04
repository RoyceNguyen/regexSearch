#Search for a regex pattern in all txt files in a directory.

import os, re

# List all files in directory and filter those that aren't txt files
files = os.listdir(os.getcwd())
txtFiles = []

txtRegex = re.compile(r'.txt')

for doc in files:
    if txtRegex.search(doc) is not None:
        txtFiles.append(doc)

#Write regex to match
searchRegex = re.compile(r'\s?\w*\!') #match all words ending in !

#open each txt file and if regex triggers print to console