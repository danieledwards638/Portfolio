#Blackjack
import random
import time


choices = " "
CompHand = 0
CompStand = " "
PlayerHand = 0


def MainMenu():
    print("MAIN MENU")
    print()
    print("1) Blackjack ")
    print("2) Roulette")
    print("3) Bingo ") 
    print("4) Grand National ")
    print("5) Slot Machines")
    choice = input("Select Gamemode (Enter correlating number to game) ")

    if choice == "1":
        BlackJack()
    #elif choice == "2":
    #    Roulette()
    #elif choice == "3":
    #   Bingo()
    #elif choice == "4":
    #    GrandNational()
    #elif choice == "5":
    #    SlotMachines()


def BlackJack(Mone):
    Money=Mone
    AceOfHearts = ["Ace Of Hearts", 1]
    TwoOfHearts = ["Two Of Hearts", 2]
    ThreeOfHearts = ["Three Of Hearts", 3]
    FourOfHearts = ["Four Of Hearts", 4]
    FiveOfHearts = ["Five Of Hearts", 5]
    SixOfHearts = ["Six Of Hearts", 6]
    SevenOfHearts = ["Seven Of Hearts", 7]
    EightOfHearts = ["Eight Of Hearts", 8]
    NineOfHearts = ["Nine Of Hearts", 9]
    TenOfHearts = ["Ten Of Hearts", 10]
    JackOfHearts = ["Jack Of Hearts", 10]
    QueenOfHearts = ["Queen Of Hearts", 10]
    KingOfHearts = ["King Of Hearts", 10]

    AceOfDiamonds = ["Ace Of Diamonds", 1]
    TwoOfDiamonds = ["Two Of Diamonds", 2]
    ThreeOfDiamonds = ["Three Of Diamonds", 3]
    FourOfDiamonds = ["Four Of Diamonds", 4]
    FiveOfDiamonds = ["Five Of Diamonds", 5]
    SixOfDiamonds = ["Six Of Diamonds", 6]
    SevenOfDiamonds = ["Seven Of Diamonds", 7]
    EightOfDiamonds = ["Eight Of Diamonds", 8]
    NineOfDiamonds = ["Nine Of Diamonds", 9]
    TenOfDiamonds = ["Ten Of Diamonds", 10]
    JackOfDiamonds = ["Jack Of Diamonds", 10]
    QueenOfDiamonds = ["Queen Of Diamonds", 10]
    KingOfDiamonds = ["King Of Diamonds", 10]

    AceOfClubs = ["Ace Of Clubs", 1]
    TwoOfClubs = ["Two Of Clubs", 2]
    ThreeOfClubs = ["Three Of Clubs", 3]
    FourOfClubs = ["Four Of Clubs", 4]
    FiveOfClubs = ["Five Of Clubs", 5]
    SixOfClubs = ["Six Of CLubs", 6]
    SevenOfClubs = ["Seven Of Clubs", 7]
    EightOfClubs = ["Eight Of Clubs", 8]
    NineOfClubs = ["Nine Of Clubs", 9]
    TenOfClubs = ["Ten Of Clubs", 10]
    JackOfClubs = ["Jack Of Clubs", 10]
    QueenOfClubs = ["Queen Of Clubs", 10]
    KingOfClubs = ["King Of Clubs", 10]

    AceOfSpades = ["Ace Of Spades", 1]
    TwoOfSpades = ["Two Of Spades", 2]
    ThreeOfSpades = ["Three Of Spades", 3]
    FourOfSpades = ["Four Of Spades", 4]
    FiveOfSpades = ["Five Of Spades", 5]
    SixOfSpades = ["Six Of Spades", 6]
    SevenOfSpades = ["Seven Of Spades", 7]
    EightOfSpades = ["Eight Of Spades", 8]
    NineOfSpades = ["Nine Of Spades", 9]
    TenOfSpades = ["Ten Of Spades", 10]
    JackOfSpades = ["Jack Of Spades", 10]
    QueenOfSpades = ["Queen Of Spades", 10]
    KingOfSpades = ["King Of Spades", 10]


    cards = [AceOfHearts, TwoOfHearts, ThreeOfHearts, FourOfHearts, FiveOfHearts, SixOfHearts, SevenOfHearts, EightOfHearts, NineOfHearts, TenOfHearts, JackOfHearts, QueenOfHearts, KingOfHearts,
    AceOfDiamonds, TwoOfDiamonds, ThreeOfDiamonds, FourOfDiamonds, FiveOfDiamonds, SixOfDiamonds, SevenOfDiamonds, EightOfDiamonds, NineOfDiamonds, TenOfDiamonds, JackOfDiamonds, QueenOfDiamonds, KingOfDiamonds,
    AceOfClubs, TwoOfClubs, ThreeOfClubs, FourOfClubs, FiveOfClubs, SixOfClubs, SevenOfClubs, EightOfClubs, NineOfClubs, TenOfClubs, JackOfClubs, QueenOfClubs, KingOfClubs,
    AceOfSpades, TwoOfSpades, ThreeOfSpades, FourOfSpades, FiveOfSpades, SixOfSpades, SevenOfSpades, EightOfSpades, NineOfSpades, TenOfSpades, JackOfSpades, QueenOfSpades, KingOfSpades
    ]
    shuffledCards = []
    def ShuffleCards():
    
        for i in range (0, len(cards)-1):
            randIdx = random.randint(0,len(cards)-1)
            card = cards[randIdx]
            cards.pop(randIdx)
            shuffledCards.append (card)
          

    def PlayerHit(choices):
        global PlayerHand
        global PlayerCardThree       
        while choices == "hit":           
            PlayerCardThree = shuffledCards.pop ()
            PlayerHand = PlayerHand + PlayerCardThree[1]
            print(PlayerCardThree[0], PlayerCardThree[1])
            print()
            print("Your new total is")
            print(PlayerHand)
            print()
            if PlayerHand <22:    
                choice = input("Do you want to hit or stand now? ")
                if choice == "hit":
                    choices = "hit"
                else:
                    choices = "stand"
                print()
                print("The dealers total is ")
                print(CompHand)
            elif PlayerHand >= 22:
                choices = "Bust"
                print("You bust, The dealer wins")

    
    def CompChoice():
        global CompHand
        global CompStand
        while CompHand <17 :
            CompCardThree = shuffledCards.pop ()
            CompHand = CompHand + CompCardThree[1]
            print("The dealer hits and gets")
            print(CompCardThree[0], CompCardThree[1])
            print()
            print("The dealers total is now")
            print(CompHand)
            print()
            if CompHand >= 22:
                print("The dealer busts, You win")
                CompStand = "false"
        CompStand == "true"
        if CompStand == "true":
            print("The dealer Stands")

    def win():
        while CompStand == "true":
            if CompHand > PlayerHand:
                print("The dealer wins, unlucky!")
            elif PlayerHand > CompHand:
                print("You win, well done!")

    ShuffleCards()
    PlayerCardOne = shuffledCards.pop ()
    PlayerCardTwo = shuffledCards.pop ()
    PlayerHand = PlayerCardOne[1] + PlayerCardTwo[1]
    CompCardOne = shuffledCards.pop ()
    CompCardTwo = shuffledCards.pop ()
    CompHand = CompCardOne[1] + CompCardTwo[1]
    print()
    print("You have been dealt ")
    print (PlayerCardOne[0], PlayerCardOne[1])
    print (PlayerCardTwo[0], PlayerCardTwo[1]) 
    print()
    print("Your total is ")
    print (PlayerHand)
    print()
    print()
    print("The dealer has")
    print(CompCardOne[0], CompCardOne[1])
    print()
    print()
    choices = input("Would you like to stand or hit? ")
    print()
    PlayerHit(choices) 

    if choices == "stand":
        print("The dealer has")
        print (CompCardOne[0], CompCardOne[1])
        print (CompCardTwo[0], CompCardTwo[1])
        print()
        print("The dealers total is ")
        print(CompHand)

    CompChoice()
    CompChoice()
    #def Bust():
    #    if PlayerHand >= 22:
    #        print("You have gone bust, The dealer wins ")
    #    elif CompHand >= 22:
    #        print("The dealer has gone bust, You win")
    return Money
