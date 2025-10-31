import random as r 
choice=["s","p","sc"]
userChoice=input("enter your chioce: like stone:-s    paper:-p   scissor:-sc:   ")
myChoice=r.choice(choice)

while True:

    if userChoice=="s":
        if myChoice=="p":
            print("i win")
            print(f"my choice is {myChoice}")
            break
        elif myChoice=="s":
            print("draw")
            print(f"my choice is {myChoice}")
            break
        else:
            print("you win")
            print(f"my choice is {myChoice}")
            break
        
    elif userChoice=="p":
        if myChoice=="s":
            print("you win")
            print(f"my choice is {myChoice}")
            break
        elif myChoice=="p":
            print("its draw ")
            print(f"my choice is {myChoice}")
            break
        else:
            print(" i win")
            print(f"my choice is {myChoice}")
            break
    elif userChoice=="sc":
        if myChoice=="sc":
            print("its draw ")
            print(f"my choice is {myChoice}")
            break     
        elif myChoice=="s":
            print(" i win 🎆")
            print(f"my choice is {myChoice}")
            break
        else:
            print("you win")
            print(f"my choice is {myChoice}")
            break
    else:
        print("invalid input")
        break
