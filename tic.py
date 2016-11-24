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


class Rules(object):

    def legal(self, move0, move1):
        """This function will determine if the players move is on a empty square
    and return True for legal and False for illegal."""
        try:
            #checks if the coordinates are on a empty square.
            if b.board[move0][move1] == 0:
                return True
            else:
                print ('Illegal move')
                return False
        except IndexError:
            print('IndexError')
            return False

    def win_check(self, player):
        """Checks if the current player has won."""
        for x in range (0, 2):
            if b.board[x][y] == player and b.board[x][y+1] == player and b.board[x][y+1] == player:
                return
            else:
                return false
        
class matrix():

    def __init__(self):
        board = [[0, 0, 0],
        	[0, 0, 0],
         	[0, 0, 0]]

    def print_b(self):
        """Prints the b"""
        #This is why you need comments.
        for row in self.b:
            print(row)
        return

def main():
    b = matrix
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
            b.board()
            #gets the coordinates
            print(player, 'turn.')
            move0 = get_cor()
            move1 = get_cor()
            b.board()
            print ('------------------------')
            move_check.legal(move0, move1)
            if move_check.legal(move0, move1) == True:
                b.board[move0][move1] = player
                turn += 1
            else:
                continue
            if move_check.win_check(player):
                b.board()
                print ('Congratulations! You won player: ')
                print(player)
                break
            else:
                continue
        else:
            print ('Game ends in a draw')
            break
main() 
