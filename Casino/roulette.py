import random
def roulette(Mone):
    global bet
    global Money
    Money=Mone
    global RorB
    print ("how to play roulette: first you will bet on the colour of what you want then you will bet on the number you want to bet on the numbers for black are:")
    print("2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35")
    print("the numbers for red are")
    print("1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36")
    bet = int(input("how much would you like to bet "))

    numr = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    redcard = random.choice(numr)

    numb = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    blackcard = random.choice(numb)
        
    RorB = random.randint(1,2)
    
    if bet > Money:
        print("not enough funds")
    else:
        Money = Money-bet
        decision = input("would you like to bet on a solid colour or a specific number and colour ")
        if decision == "solid colour":
            colour = int(input("what colour would you like to bet on 1 = black 2 = red "))
            if RorB == colour:
                print ("you win")
                if RorB == 1:
                    print ("black")
                elif RorB == 2:
                    print("red")
                print ("your money has been multiplied by 1.5")
                Money = (bet*1.5)+Money
                print(Money)
                again = input("would you like to play again ")
                if again == "yes":
                    roulette()
                elif again == "no":
                    return Money
            elif RorB != colour:
                print ("you lose")
                if RorB == 1:
                    print ("black")
                elif RorB == 2:
                    print("red")
                print (Money)
                again = input("would you like to play again ")
                if again == "yes":
                    roulette()
                elif again == "no":
                    return Money
        else:  
            cchoice = input("what colour would you like to bet on: 1 = black 2 = red ")
            nchoice = int(input("what number would you like to bet on "))
            if RorB == 2:
                print("red",redcard)
            elif RorB == 1:
                print("black",blackcard)
            if RorB == cchoice and nchoice == redcard:
                print ("you have won your chips have been multiplied by 10X ") 
                bet = (bet*10)+Money
                print (Money)
                again = input("would you like to play again ")
                if again == "yes":
                    roulette()
                elif again == "no":
                    return Money
            else:
                print("you lose")
                print (Money)
                again = input("would you like to play again ")
                if again == "yes":
                    roulette()
                elif again == "no":
                    return Money

