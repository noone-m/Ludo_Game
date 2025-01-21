from game import LudoGame

if __name__ == "__main__":
    while(True):
        depth =int (input("enter 1 to easy 2 to medium 3 to hard : "))
        if (depth==1 or depth==2 or depth==3 ):
            break
        else: 
            print('you must enter 1 or  2 or 3')
            print(depth)
    game = LudoGame(depth=depth)
    while(True):
    
        playWithMe = int(input("Enter 1 for play with computer , 2 for let only computer play :  "))
        if(playWithMe==1 or playWithMe==2 ):
            game.play_game(playWithPlayer=(playWithMe==1))  
            break
        else:
            print("you must enter 1 or tow")