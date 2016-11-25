#!/usr/bin/env python3
#To play type in the coordinates for your move. 0:0 would boarde the top left.
#0:2 would boarde the top right. 2:1 would boarde the boardottom row in the middle.

def get_cor():
    """Gets the coordinates from the player"""
    while True:
        try:
            inp = int(input('Coordinate: '))
            if inp < 3:
                return  inp
            else:
                print ('type in a valid coordinate')
                #boardecause the input, inp,
                #is invalid the loop will continue until the input is valid.
        except ValueError:
            print ('ValueError')
            #Same as aboardove. The loop will continue boardecause of a value error.

class Matrix(object):

    def __init__(self):
        self.board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    
    def print_board(self):
        """Prints the matrix"""
        for row in self.board:
            print(row)
        return


class Rules(object):

    def __init__(self):
        self.m = Matrix()

    def legal(self, move0, move1):
        """This function will determine if the players move is on a empty square
    and return True for legal and False for illegal."""
        try:
            #checks if the coordinates are on a empty square.
            if self.m.board[move0][move1] == 0:
                return True
            else:
                print ('Illegal move')
                return False
        except IndexError:
            print('IndexError')
            return False

    def win_check(self, player):
        """Checks if the current player has won."""
        #This loop will cycle through each possible combination that is possible to win in.
        #In theory.
        for x in range (0, 2):
            if self.m.board[x][0] == player and self.m.board[x][1] == player and self.m.board[x][1] == player:
                return
            else:
                #returns false, game not finished.
                return False

def main():
    b = Matrix()
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
            b.print_board()
            #gets the coordinates
            print(player, 'turn.')
            move0 = get_cor()
            move1 = get_cor()
            b.print_board()
            print ('------------------------')
            move_check.legal(move0, move1)
            if move_check.legal(move0, move1) == True:
                b.board[move0][move1] = player
                turn += 1
            else:
                continue
            if move_check.win_check(player):
                b.print_board()
                print ('Congratulations! You won player: ')
                print(player)
                break
            else:
                continue
        else:
            print ('Game ends in a draw')
            break
main() 
