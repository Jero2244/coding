#! /usr/bin/python3

import re

#text without the words
text = '''The ADJECTIVE panda walked to the NOUN and 
then VERB. A nearby NOUN was
unaffected by these events.'''

#a loop that finds ADjective, noun, etc words in the text
word_class = re.compile(r'[A-Z][A-Z]+')
word_list = word_class.findall(text)
#input from the user and create new text
for word in word_list:
    replacement = input(f'Enter an {word.lower()}: \n')
    text = text.replace(word, replacement, 1)

#print it and save it to textfile(madlibs.txt)
print(text)
fhan = open('madlibs.txt', 'w')
fhan.write(text)
fhan.close()