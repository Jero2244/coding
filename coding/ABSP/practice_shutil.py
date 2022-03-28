#! /usr/bin/python3

import shutil, os, send2trash, re

destination = '/home/jero/Downloads'
# #os.walk()

def selective_copy(destination):
    for folderName, subfolders, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.endswith('.py'):#find those that end in .py
                print(os.path.join(folderName, filename))
                shutil.copy(os.path.join(folderName, filename), destination )#copy to a new folder

def del_unneed_files(destination):
    for folderName, subfolders, filenames in os.walk(destination):
        for filename in filenames:
            if os.path.getsize(os.path.join(folderName, filename)) > 100:
                os.unlink(os.path.join(folderName, filename))

def fill_the_gaps():
    file_match_list = []
    file_list = os.listdir(os.path.join(os.getcwd(), 'dummy_texts'))
    file_number = re.compile(r'\d')
    for file in file_list:
        file_match = file_number.search(file)
        if file_match == None:
            continue
        else:
            file_match_list.append(int(file_match.group()))
    file_match_list.sort()
    for i in range(len(file_match_list)):
        if file_match_list[0] == file_match_list[i]:
            continue
        elif file_match_list[i] - 1 != file_match_list[i - 1]:
            print('It is not in order')
            # print(i)
            print(file_match_list[i])
        else:
            print(f'it is in order')
           
        

# os.walk()

fill_the_gaps()