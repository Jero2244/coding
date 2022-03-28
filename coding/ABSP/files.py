#! /usr/bin/python3
import re, os, shutil

for folderName, subfolders, filenames in os.walk('/home/jero/Desktop/coding'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')