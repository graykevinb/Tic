#!/usr/bin/env python3
#To play type in the coordinates for your move. 0:0 would be the top left.
#0:2 would be the top right. 2:1 would be the bottom row in the middle.

def get_cor():
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
        """Returns True if the player has won, and False if the player hasn't won."""
        #This loop checks for horizontal wins.
        for x in range (0, 2):
            if board[x][0] == player and board[x][1] == player and board[x][2] == player:
                return True
            else:
                pass
        #This loop checks for vertical wins.
        for y in range(0, 2):
            if board[0][y] == player and board[1][y] == player and board[2][y] == player:
                return True
            else:
                pass
        #This part checks for diagonal wins.
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        else:
            pass
        return False

def print_board(board):
    """Prints the board"""
    #This is why you need comments.
    for row in board:
        print(row)
    return

def main():
    board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    player = 1
    turn = 0
    move0 = None
    move1 = None
    move_check = Rules()
    count = 0
    
    while True:
        if turn != 9:
            if player == 1:
                player = 2
            else:
                player = 1
            print_board(board)
            #gets the coordinates
            print(player, 'turn.')
            move0 = get_cor()
            move1 = get_cor()
            print_board(board)
            print ('------------------------')
            move_check.legal(board, move0, move1)
            if move_check.legal(board, move0, move1) == True:
                board[move0][move1] = player
                turn += 1
            else:
                continue
            if move_check.win_check(board, player) == True:
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
