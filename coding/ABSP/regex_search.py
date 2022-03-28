#! /usr/bin/python3

import re, os

#get the files 
files = os.listdir('/home/jero/Desktop/coding/dummy_texts')

#get the regex
regex = input('Please enter a valid regular expression: ')
find_words = re.compile(regex)
words_found = []
#go through each file 
for file in files:
    os.chdir('/home/jero/Desktop/coding/dummy_texts')
    current_file = open(file)
    file_string = current_file.read()
    matches = find_words.findall(file_string) #check if the regex exists and add them to a list     
    if len(matches) == 0:
        print(f'No matches found in {file}')
        current_file.close()
        continue
    words_found.append(matches)
    current_file.close()

#print the list of founds
print(words_found)