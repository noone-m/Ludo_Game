import random
from typing import List, Dict, Optional
from copy import deepcopy
from board import Board
from ai import AI

class LudoGame:
    def __init__(self ,depth):
        self.depth =depth 
        self.players = ['Red', 'Blue']
        self.board = Board()

    def roll_dice(self) -> int:
        return random.randint(1, 6)
  
    def play_turn(self, player: str,dice_roll , playWithPlayer) -> bool:
        
        print(f"\n{player} rolled a {dice_roll}")
        
        valid_moves = self.board.get_valid_moves(player, dice_roll)
        
        if not valid_moves:
            print(f"No valid moves for {player}")
            return False
        if player == 'Red':
            
            best_move = AI.expectimax(self.board, dice_roll, self.depth, False, False,self.players) 
            _,self.board= best_move
        if player == 'Blue':
            if(playWithPlayer):
                print(f"your valid Tokens are : {valid_moves}")
                playerMove = self.playerPlay(validMoves=valid_moves , diceRoll=dice_roll)
                self.board = playerMove


                
            else:

                best_move = AI.expectimax(self.board, dice_roll, self.depth, True, False,self.players)
                _,self.board= best_move

        # boards = self.board.get_possible_boards(player,dice_roll)
        # print('---------------------\nposssible boards:')
        # for i in range(len(boards)):
        #     print (f'* possible board {i + 1} :')
        #     boards[i].display_board()
        # print ('------------------------')
        
        # move = AI.simple_ai(self,valid_moves,player,dice_roll)

        # self.board.move_token(player,move,dice_roll)
        return True

    def playerPlay(self ,validMoves ,diceRoll):
        while(True):
            tokenNum = int(input("Enter token number To Move It : "))
            if(tokenNum in  validMoves):
                board = deepcopy(self.board)
                board.move_token(player='Blue', token_index=tokenNum,steps=diceRoll)
                return board


    def play_game(self,playWithPlayer) -> None:
            playTimes =0 
            turn = 0
            while True:
                current_player = self.players[turn % 2]
                self.board.display_board()
                dice_roll = self.roll_dice()
                self.play_turn(player=current_player ,dice_roll= dice_roll,playWithPlayer=playWithPlayer)
                if (dice_roll == 6 and playTimes<4  ) :
                    playTimes +=1
                else:
                    playTimes = 0 
                    turn +=1
                winner = self.board.check_winner(self.players)
                if winner:
                    print(f"\n{winner} wins the game!")
                    break