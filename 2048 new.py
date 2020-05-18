from random import randrange,randint
from os import system, name 
from time import sleep
import msvcrt

game_board=[]

def board():
	clear()
	for row in game_board:
		print( row )
	print(" ")	
 
def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear') 

def maker(n):
	for i in range(n):
		zero=[]
		for j in range(n):
			zero.append(0)
		game_board.append( zero )

def user_input():
	uinput = msvcrt.getch()
	return(uinput)

def randpos(n):
	gen1=randrange(n)
	gen2=randrange(n)
	if game_board[gen1][gen2]==0:
		game_board[gen1][gen2]=2

def checker(n,game_board):
	end=False
	for i in range(n):
		for j in range(n):
			if game_board[i][j]==0:
				end=True
		for j in range(n-1):
			if game_board[i][j]!=0:
				if game_board[i][j]==game_board[i][j+1]:
					end=True		
	for i in range(n-1):
			for j in range(n):
				if game_board[i][j]!=0:
					if game_board[i][j]==game_board[i+1][j]:
						end=True
	else:
		end=False		
			
	return(end)

def valid(boardcopy,game_board):
	if game_board==boardcopy:
		print("Invalid move!")
		spawn=False
	else:
		spawn=True
	return spawn

def win(game_board,n,q):
	for i in range(n):
		for j in range(n):
			if game_board[i][j]==q:
				return(False)

def reverse(game_board,n):
    new_game_board=[]
    for i in range(n):
        new_game_board.append([])
        for j in range(n):
            new_game_board[i].append(game_board[i][n-1-j])
    return new_game_board

def transp(game_board,n):
    new_game_board=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(4):
            new_game_board[i][j]=game_board[j][i]
    return new_game_board

def merge(game_board,n):
    for i in range(4):
        for j in range(3):
            if game_board[i][j]==game_board[i][j+1] and game_board[i][j]!=0:
                game_board[i][j]+=game_board[i][j]
                game_board[i][j+1]=0
    return game_board

def compress(game_board,n):
    new_game_board=[[0 for i in range(4)] for i in range(4)]
    for i in range(4):
        pos=0
        for j in range(4):
            if game_board[i][j]!=0:
                new_game_board[i][pos]=game_board[i][j]
                pos+=1
    return new_game_board

def leftshift(game_board,n):
    temp1=compress(game_board,n)
    temp2=merge(temp1,n)
    temp3=compress(temp2,n)
    return temp3
    
def rightshift(game_board,n):
    temp=reverse(game_board,n)
    temp1=compress(temp,n)
    temp2=merge(temp1,n)
    temp3=compress(temp2,n)
    temp4=reverse(temp3,n)
    return temp4

def upshift(game_board,n):
    temp=transp(game_board,n)
    temp1=compress(temp,n)
    temp2=merge(temp1,n)
    temp3=compress(temp2,n)
    temp4=transp(temp3,n)    
    return temp4
    
def downshift(game_board,n):
    temp=transp(game_board,n)
    temp1=reverse(temp,n)
    temp2=compress(temp1,n)
    temp3=merge(temp2,n)
    temp4=compress(temp3,n)
    temp5=reverse(temp4,n)
    temp6=transp(temp5,n)
    return temp6

def main():
	global game_board
	boardcopy=[]
	spawn=True
	n=int(input('Input size of board: '))
	q=int(input('Input winning number in power of 2: '))
	maker(n)
	board()
	checker(n,game_board)
	end=True
	while (end) :
		if spawn == True:
			randpos(n)
		board()
		move=user_input()
		if move==b"w":
			boardcopy=game_board
			game_board=upshift(game_board,n)
			board()
			valid(boardcopy,game_board)
		elif move==b"a":
			boardcopy=game_board
			game_board=leftshift(game_board,n)
			board()
			valid(boardcopy,game_board)
		elif move==b"d":
			boardcopy=game_board
			game_board=rightshift(game_board,n)
			board()
			valid(boardcopy,game_board)
		elif move==b"s":
			boardcopy=game_board
			game_board=downshift(game_board,n)
			board()
			valid(boardcopy,game_board)
		elif move==b"x":
			break
		if (win(game_board,n,q)==False):
			print("You have won!")	
			break	

	print("Game Over!")

if __name__ == '__main__':
	main()
