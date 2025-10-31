print("SNAKE GAME.WHO WILL REACH 100 FIRST WINS")


import random as r 
pick=[1,2,3,4,5,6]
computerStart=0
userStart=0
while True:
    yourTurn=input("press 't' for your turn")
    userChoice=r.choice(pick)
    computer=r.choice(pick)
    print(f"your number is{userChoice}")
    computerStart+=computer

    print()
    print("its my turn ")
    print(f"my number is {computer}")
    userStart+=userChoice
    print()
    print(f"my score is {computerStart}   and  your score is {userStart}")
    print()
    if userStart>=100 or computerStart>100:
        break
        


if (computerStart>=100):
    print("wohoo i won this match ✌️✌️🎆🎇")
else:
    print("congratulation, you won 😏😏")
    


print("GAME FINISHED")







    

