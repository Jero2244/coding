#! /usr/bin/python3

import re
def detect_strong_pwd(pwd):
    str = re.compile(r'[a-zA-Z0-9]{8,}')
    if str.search(pwd) != None:
        return True
    else:
        return False

def detect_punct(phrase):
    punt = re.compile(r'[~!@#$%^&*()]')
    string = punt.sub(r'', phrase)
    return string

def reg_exp_strip(phrase, regex='\s'):
    if regex != '\s':
        strip = re.compile(f'^[{regex}]+') #if user enters a \ or / I'm fucked
        phrase = strip.sub('', phrase)
        strip = re.compile(f'[{regex}]+$')
        phrase = strip.sub('', phrase)
        return phrase
    else:
        strip = re.compile(r'^\s+')
        phrase = strip.sub(r'', phrase)
        strip = re.compile(r'\s+$')
        phrase = strip.sub(r'', phrase)
        return phrase

        
phrase = '@#$hello!!!'
print(detect_punct(phrase))
