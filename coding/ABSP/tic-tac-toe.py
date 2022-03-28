#! /usr/bin/python3

def display_board(board):
        print(board['top_l'] + '|' + board['top_m'] +  '|' + board['top_r'])
        print('-+-+-')
        print(board['mid_l'] +  '|' +  board['mid_m'] +  '|' + board['mid_r'])
        print('-+-+-')
        print(board['low_l'] + '|' + board['low_m'] + '|' +board['low_r'])

def turn(actual_turn, board):
        print(f'It is {actual_turn} turn. Where do you want to put')
        while True:
                place = input()
                if place not in board.keys():
                        print('Please enter a valid place')
                        continue
                else:
                        if board[place] == ' ':
                                board[place] = actual_turn
                                break
                        else:
                                print('This place is occupied. Try again')
                                continue
                        
                                
                

def check_winner(board):
        if board['top_l'] == board['top_m'] == board['top_r'] != ' ':
               return (board['top_l'] + ' won')
        elif board['mid_l'] == board['mid_m'] == board['mid_r'] != ' ':
               return (board['mid_l'] + ' won')
        elif board['low_l'] == board['low_m'] == board['low_r'] != ' ':
               return (board['low_l'] + ' won')
               


board = {'top_l': ' ','top_m': ' ', 'top_r': ' ',
        'mid_l': ' ', 'mid_m': ' ', 'mid_r': ' ',
        'low_l': ' ', 'low_m': ' ', 'low_r': ' '}

this_turn = 'X'
for i in range(9):
        turn(this_turn, board)
        display_board(board)
        if this_turn == 'X':
                this_turn = 'O'
        else:
                this_turn = 'X'
        winner = check_winner(board)
        if winner != None:
                print(winner)
                break
