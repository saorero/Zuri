

import random
print("*****ROCK PAPER SCISSOR GAME*****")

aList=['R','P','S']

cpuWin='\tCPU WON!!!'
pWin='\tPLAYER WON!!!'

print('Enter option(R,P or S):')


while True:
    
    CPU=random.choice(aList)
    while True:
            player=input("PLAYER:")
            if player in aList:
                        break
            else:
                print('Invalid Input try again')


    print("PLAYER("+player,"):CPU("+CPU,")")
    if (CPU=='R' and player=='P'):
        print(pWin)
    elif CPU=='P' and player=='R':
        print(cpuWin)
    elif CPU=='S' and player=='P':
        print(cpuWin)

    elif (CPU=='R' and player=='S'):
        print(cpuWin)
    elif (CPU=='P' and player=='S'):
        print(pWin)
    elif (CPU=='S' and player=='R'):
        print(pWin)

    elif player==CPU:
        print('Its a tie!')
    else:
        print('Invalid Results')
    if player!=CPU:
            break