#! /usr/bin/python3

def printTable(table):
    colWidths = [0] * len(table)
    i = 0
    for ls in table:
        big_word = None
        for word in ls:
            if big_word == None or len(word) > len(big_word):
                big_word = word          
        colWidths[i] = len(big_word)
        i += 1

    print(colWidths)

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j]), end=" ")
        print('\n')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)