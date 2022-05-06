import time
import horseracing 
import bingo
import code
import Blackjack
import roulette

Money=int(input("Input how much money you want to play with.\n"))




def main():
    global Money
    if Money<1:
        print("You do not have enough money.\nYou are now being kicked out of the casino for being poor lol.")
        return
    print(
        """
        For Horse Racing, Press 1
        For Blackjack, Press 2
        For Bingo, Press 3
        For Slot Machine, Press 4
        For Roulette, Press 5
        """
    )
    choice6969=input()
    if choice6969=="1":
        print("£"+str(Money))
        Money = int(horseracing.race(Money))
    if choice6969=="2":
        Money = int(Blackjack.BlackJack(Money))
    if choice6969=="3":
        Money = int(bingo.Bingo(Money))
    if choice6969=="4":
        Money= int(code.play(Money))
    if choice6969=="5":
        Money=int(roulette.roulette(Money))
    print(Money)



    time.sleep(5)
    main()
main()