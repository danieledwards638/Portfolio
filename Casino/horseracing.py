import random
import time

def race(Money):
    Money=int(Money)
    horses=[0,0,0,0,0]
    choice=int(input("Choose horse 1-5\n"))
    if choice<1 or choice>5:
        print(f"You cannot choose horse {choice}")
        race(Money)
        return str(Money)
    bet=int(input(f"Enter your bet on horse {choice}\n"))
    if bet<1 or bet>Money:
        print(f"You cannot bet £{bet}")
        race(Money)
        return str(Money)
    Money-=bet
    
    complete=False
    while not complete:
        print("\n"*40)
        for i in range(5):
            horses[i]+=random.random()*3
            print(str(round(horses[i], 1))+" | HORSE "+str(i+1)+":|"+("-"*int(round(horses[i]*3,0)))+"HORSE"+str(i+1))
        for i in range(5):
            if horses[i]>40:
                temp = []
                for i in range(len(horses)):
                    temp.append(horses[i])
                temp.sort(reverse=True)
                winner=horses.index(temp[0])+1
                complete=True
        time.sleep(0.15)
    
    print(f"The winner was horse {winner}")
    if choice==winner:
        Money+=bet*2
        print(f"You have won £{bet}, you now have £{Money}")
   
    else:
        print(f"You have lost £{bet}, you now have £{Money}")
    return str(Money)