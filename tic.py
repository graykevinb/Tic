#!/usr/bin/env python3
#To play type in the coordinates for your move. 0:0 would be the top left.
#0:2 would be the top right. 2:1 would be the bottom row in the middle.

def get_cor(inp):
    """Gets the coordinates from the player"""
    while True:
        try:
            inp = int(input('Coordinate: '))
            if inp < 3:
                return  inp
            else:
                print ('type in a valid coordinate')
                #because the input, inp,
                #is invalid the loop will continue until the input is valid.
        except ValueError:
            print ('ValueError')
            #Same as above. The loop will continue because of a value error.


class Rules(object):

    def legal(self, board, move0, move1):
        """This function will determine if the players move is on a empty square
    and return True for legal and False for illegal."""
        try:
            #checks if the coordinates are on a empty square.
            if board[move0][move1] == 0:
                return True
            else:
                print ('Illegal move')
                return False
        except IndexError:
            print('IndexError')
            return False

    def win_check(self, board, player):
        """Checks if the current player has won."""
        #Top Row Horizontal
        if board[0][0] == player and board[0][1] == player and board[0][2] == player:
            print('1')
            return True
        #Middle Row Horizontal
        elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
            print('2')
            return True
        #Bottom Row Horizontal
        elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
            print('3')
            return True
        #Left Vertical Row
        elif board[0][0] == player and board [1][0] == player and board[2][0] == player:
            print('4')
            return True
        #Middle Vertical Row
        elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
            print('5')
            return True
        #Right Vertical Row
        elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
            print('6')
            return True
        #Diagonal Row starting from top left and going down to the bottom right corner.
        elif board[0][0] == player and board [1][1] == player and board[2][2] == player:
            print('7')
            return True
        #Diagonal Row starting from bottom left and going up to the top right corner.
        elif board[0][2] == player and board [1][1] == player and board[2][0] == player:
            print('8')
            return True
        #Returns false if the player hasn't won.
        else:
            return False

class board():

    def __init__(self):
        board = [[0, 0, 0],
        	[0, 0, 0],
         	[0, 0, 0]]

    def print_board(self):
        """Prints the board"""
        #This is why you need comments.
        for row in self.board:
            print(row)
        return

def main():
    player = 1
    turn = 0
    move0 = None
    move1 = None
    move_check = Rules()
    count = 0
    print ('Welcome to tic! Tic is a tic tac toe game written entirely in python3!')
    print ('To play type in the coordinate of where you want to go.')
    tutorial = str(input('Would you like to do the tutorial? y or n.'))
    if tutorial == 'y':
        print (''' Let's get started!''')
        print_board(board)
        print ('''So there is the board and your probobly wondering how you move.\n
        Am I correct? Anyways you move by typing in the cordinates of where\n
        you want to go. So lets try it!
        To move first type a number from 0 to 2 and press enter. Repeat.
        Notice where it showed up. The system goes like this:
        0:0 top right corner, 0:2 top left corner.
        2:0 bottom left corner and so on.''')
        while True:
            if count != 5:
                print_board(board)
                move0 = get_cor(None)
                move1 = get_cor(None)
                if board[move0][move1] == 0:
                    board[move0][move1] = 1
                    count += 1
                else:
                    pass
            else:
                break
        print ('Tutorial Complete!')
        board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    else:
        pass


    while True:
        if turn != 9:
            if player == 1:
                player = 2
            else:
                player = 1
            print_board(board)
            #gets the coordinates
            print(player, 'turn.')
            move0 = get_cor(None)
            move1 = get_cor(None)
            print_board(board)
            print ('------------------------')
            move_check.legal(board, move0, move1)
            if move_check.legal(board, move0, move1) == True:
                board[move0][move1] = player
                turn += 1
            else:
                continue
            if move_check.win_check(board, player):
                print_board(board)
                print ('Congratulations! You won player: ')
                print(player)
                break
            else:
                continue
        else:
            print ('Game ends in a draw')
            break
main() 
