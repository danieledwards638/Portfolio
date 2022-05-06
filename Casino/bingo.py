import random
from tkinter import *
import time
def Bingo(Mone):
    global Round,Line1,CalledNumber,Round,Points,Line1,Line2,Line3,Line4,FullCard,VerticalLine1,VerticalLine2,VerticalLine3,VerticalLine4,DiagonalLine1,DiagonalLine2,Bet,frame,Money
    Money=Mone
    #Creating some variables that i will be using for out my code
    Round = 0
    Points = 0
    PlayerCard1 = [0,0,0,0]
    PlayerCard2 = [0,0,0,0]
    PlayerCard3 = [0,0,0,0]
    PlayerCard4 = [0,0,0,0]
    NumFound1 = ["False","False","False","False"]
    NumFound2 = ["False","False","False","False"]
    NumFound3 = ["False","False","False","False"]
    NumFound4 = ["False","False","False","False"]
    BackGround1 = ["#C14949","#C14949","#C14949","#C14949"]
    BackGround2 = ["#C14949","#C14949","#C14949","#C14949"]
    BackGround3 = ["#C14949","#C14949","#C14949","#C14949"]
    BackGround4 = ["#C14949","#C14949","#C14949","#C14949"]
    Line1="False"
    Line2="False"
    Line3="False"
    Line4="False"
    VerticalLine1 = "False"
    VerticalLine2 = "False"
    VerticalLine3 = "False"
    VerticalLine4 = "False"
    DiagonalLine1 = "False"
    DiagonalLine2 = "False"
    FullCard = "False"

    #Creates 4 arrays for the playercard and gives them 16 random numbers
    def RandomCard():
        for i in range(0,4):
            PlayerCard1[i] = random.randint(1,100)
        for i in range(0,4):
            PlayerCard2[i] = random.randint(1,100)
        for i in range(0,4):
            PlayerCard3[i] = random.randint(1,100)
        for i in range(0,4):
            PlayerCard4[i] = random.randint(1,100)
        CallOut()

    #Calls a random number from 1-100 and checks if its not gone past the limit of rounds
    def CallOut():
        global CalledNumber,Round
        if Round != 50:
            CalledNumber=random.randint(1,100)
            Round = Round + 1
            NumberCheck()

    #Checks if the number called is on the playercard
    def NumberCheck():
        global Points
        for i in range(0,4):
            if PlayerCard1[i] == CalledNumber:
                if NumFound1[i] == "False":
                    NumFound1[i]= True
                    Points = Points + 10
                    BackGround1[i] = "#77B569"
                #Needs to not do if number found a second time
            if PlayerCard2[i] == CalledNumber:
                if NumFound2[i] == "False":
                    NumFound2[i] = True
                    Points = Points + 10
                    BackGround2[i] = "#77B569"
            if PlayerCard3[i] == CalledNumber:
                if NumFound3[i] == "False":
                    NumFound3[i] = True
                    Points = Points + 10
                    BackGround3[i] = "#77B569"
            if PlayerCard4[i] == CalledNumber:
                if NumFound4[i] == "False":
                    NumFound4[i] = True
                    Points = Points + 10
                    BackGround4[i] = "#77B569"
        LineCheck()

    #Checks if there is a horizontal line of found numbers on a playercard
    def LineCheck():
        global Points,Line1,Line2,Line3,Line4,FullCard
        if NumFound1[0] == True and NumFound1[1] == True and NumFound1[2] == True and NumFound1[3] == True:
            if Line1 == "False":
                Line1 = True
                Points = Points + 50
        if NumFound2[0] == True and NumFound2[1] == True and NumFound2[2] == True and NumFound2[3] == True:
            if Line2 == "False":
                Line2 = True
                Points = Points + 50
        if NumFound3[0] == True and NumFound3[1] == True and NumFound3[2] == True and NumFound3[3] == True:
            if Line3 == "False":
                Line3 = True
                Points = Points + 50
        if NumFound4[0] == True and NumFound4[1] == True and NumFound4[2] == True and NumFound4[3] == True:
            if Line4 == "False":
                Line4 = True
                Points = Points + 50
        if Line1 == True and Line2 == True and Line3 == True and Line4 == True:
            if FullCard == "False":
                FullCard = True
                Points = Points + 500
        VerticalLineCheck()

    #Checks if there is a Vertical line of found numbers on a playercard
    def VerticalLineCheck():
        global Points,VerticalLine1,VerticalLine2,VerticalLine3,VerticalLine4
        if NumFound1[0] == True and NumFound2[0] == True and NumFound3[0] == True and NumFound4[0] == True:
            if VerticalLine1 == "False":
                VerticalLine1 = True
                Points = Points + 50
        if NumFound1[1] == True and NumFound2[1] == True and NumFound3[1] == True and NumFound4[1] == True:
            if VerticalLine2 == "False":
                VerticalLine2 = True
                Points = Points + 50
        if NumFound1[2] == True and NumFound2[2] == True and NumFound3[2] == True and NumFound4[2] == True:
            if VerticalLine3 == "False":
                VerticalLine3 = True
                Points = Points + 50
        if NumFound1[3] == True and NumFound2[3] == True and NumFound3[3] == True and NumFound4[3] == True:
            if VerticalLine4 == "False":
                VerticalLine4 = True
                Points = Points + 50
        DiagonalCheck()

    #Checks if there is a Diagonal line of found numbers on a playercard
    def DiagonalCheck():
        global Points,DiagonalLine1,DiagonalLine2
        if NumFound1[0] == True and NumFound2[1] == True and NumFound3[2] and NumFound4[3] == True:
            if DiagonalLine1 == "False":
                DiagonalLine1 = True
                Points = Points + 50
        if NumFound4[0] == True and NumFound3[1] == True and NumFound2[2] and NumFound1[3] == True:
            if DiagonalLine2 == "False":
                DiagonalLine2 = True
                Points = Points + 50


    RandomCard()

    #Creates a tkinter gui screen that displays the rules of the game and a screen in which you can place your bet
    def SplashScreenFunction():
        global SplashScreen,BetFailed
        SplashScreen = Tk()
        SplashScreen.configure(bg="#95CEDB")
        SplashScreen.geometry("700x700")
        SplashScreen.maxsize(700,700)
        SplashScreen.minsize(700,700)

        SplashLabel = Label(SplashScreen,text="Point System", font="Ariel 30 bold",bg="#95CEDB",fg="White").pack()
        SplashExplain = Label(SplashScreen,text="Rules:\nThe game will last for 50 rounds,\n After the rounds have ended that will be your final score", font="Arial 15",bg="#95CEDB",fg="White").pack()
        SplashExplain = Label(SplashScreen,text="\nYou get score when numbers on your card match with the called number,\n if your card gets a line, a diagonal line or a full card complete\n extra points will be given", font="Arial 15",bg="#95CEDB",fg="White").pack()
        SplashExplain = Label(SplashScreen,text="\nClick the next button in the bottom right for the next number", font="Arial 15",bg="#95CEDB",fg="White").pack()
        SplashExplain = Label(SplashScreen,text="\nAmount of points you earn:\nEach number is worth 10 points\nA line or diagonal line is worth 50 Points\nA full card is worth 500 Points ", font="Arial 15",bg="#95CEDB",fg="White").pack()
        SplashExplain = Label(SplashScreen,text="\nWhat your points amount too,\nIf you dont get above 50 Points you will lose your bet\nIf you get above 50 Points you keep your bet\nIf you get above 100 Points you will earn a 1.2x Payout\nIf you get above 150 Points you will earn a 1.5x Payout\nIf you get above 250 Points you will earn a 2.0x Payout", font="Arial 15",bg="#95CEDB",fg="White").pack()
        SplashExplain = Label(SplashScreen,text="Enter how much you would like to bet below", font="Arial 18 bold",bg="#95CEDB",fg="White").pack()

        BetEntry = Entry(SplashScreen,width=20,font = ("Ariel 20"))
        BetEntry.pack()

    #Grabs the input and sets it as a variable
        def EntryGet():
            global Bet
            Bet = BetEntry.get()
            DestroyFunction()

    #Allows the user to enter incorrect inputs and tells them if so, allowing them to try again
        def DestroyFunction():
            global Money,Bet,BetFailed
    #        BetFailed = Label(SplashScreen,text="",bg="#95CEDB",fg="White",font = "Ariel 15 bold")
            try:
                Bet = int(Bet)
            except:
                BetFailed.config(text ="Bet failed, Enter a Number and make sure there isnt a decimal place")
                BetFailed.pack()
            if Bet <= Money:
                Money = Money - Bet
                SplashScreen.after(0,Main)
            else:
                BetFailed.config(text ="Bet failed, you have not got enough money")
                BetFailed.pack()

        BetButton = Button(SplashScreen,text="Enter",font="Ariel 15 bold",command=EntryGet).pack()
        BetFailed = Label(SplashScreen,text="",bg="#95CEDB",fg="White",font = "Ariel 15 bold")
    #Deletes the first gui screen and creates another
    def Main():
        SplashScreen.destroy()
        window = Tk()
        window.configure(bg="White")

        window.maxsize(800,575)
        window.minsize(800,575)

        window.rowconfigure([1,2,3,4],minsize=50, weight=1)
        window.columnconfigure([1,2,3,4],minsize=50, weight=1)

        frame2 = Frame(window,bg="White",width=600,height=575)
        frame2.grid(column=0,row=1,columnspan=4,rowspan=4,sticky="W")

        frame3 = Frame(window,bg="#95CEDB",width=186,height=560)
        frame3.grid(column=4,row=1,rowspan=4,columnspan=1)
        CallOutText = Label(window,text=CalledNumber,font="Arial 70 bold",bg = "#95CEDB",fg="White")
        CallOutText.grid(column=4,row=1)



    #Adds the players card to the gui allowing them to see there card
        def PlayerCard():
            global frame
            for column in range(4):
                frame=Frame(master=window,relief=RAISED,borderwidth=1,height=100,width=100)
                frame.grid(row=1,column=column)
                label = Label(master=frame,text=PlayerCard1[column],fg="White",font="Arial 45 bold",width=2,bg=BackGround1[column],pady=27,padx=31)
                label.grid(row=1,column=column)
            for column in range(4):
                frame=Frame(master=window,relief=RAISED,borderwidth=1,height=100,width=100)
                frame.grid(row=2,column=column)
                label = Label(master=frame,text=PlayerCard2[column],fg="White",font="Arial 45 bold",width=2,bg=BackGround2[column],pady=27,padx=31)
                label.grid(row=2,column=column)
            for column in range(4):
                frame=Frame(master=window,relief=RAISED,borderwidth=1,height=100,width=100)
                frame.grid(row=3,column=column)
                label = Label(master=frame,text=PlayerCard3[column],fg="White",font="Arial 45 bold",width=2,bg=BackGround3[column],pady=27,padx=31)
                label.grid(row=3,column=column)
            for column in range(4):
                frame=Frame(master=window,relief=RAISED,borderwidth=1,height=100,width=100)
                frame.grid(row=4,column=column)
                label = Label(master=frame,text=PlayerCard4[column],fg="White",font="Arial 45 bold",width=2,bg=BackGround4[column],pady=27,padx=31)
                label.grid(row=4,column=column)

    #Updates the screen so that the number called changes when the button is pressed
        def TextUpdate():
            CallOutText["text"] = CalledNumber

    #Updates the screen so that the points get updates as you earn them
        def PointUpdate():
            PointText["text"] = Points

    #Destroys the finishPage gui when called and resets the rounds
        def DeleteFinished():
            global FinishPage,Round,Money
            Round = 0
            FinishPage.destroy()


    #Destroys the current gui screen and replaces it with a finish screen when they run out of rounds, giving them details on how much they won or lost
        def FinishPage():
            global Bet,Money,FinishPage
            if Round == 50:
                window.destroy()
                FinishPage= Tk()
                FinishPage.configure(bg="#95CEDB")
                FinishPage.maxsize(400,400)
                FinishPage.minsize(400,400)
                FinishLabel = Label(FinishPage,text="FINISHED", font="Arial 35 bold",fg="White",bg="#95CEDB").pack()
                FinishLabel = Label(FinishPage,text=("You earned " + str(Points) + " Points"), font="Arial 20 bold",fg="White",bg="#95CEDB").pack()
                Bet = int(Bet)
                if Points < 50:
                    FinishLabel2 = Label(FinishPage,text="\nUnlucky you lost your bet", font="Arial 20 bold",fg="White",bg="#95CEDB").pack()
                    Bet = 0
                if 50 <= Points < 100:
                    FinishLabel2 = Label(FinishPage, text="\nYou niether win or lose\n you get to keep Your money", font="Arial 20 bold",fg="White",bg="#95CEDB").pack()
                if 100 <= Points < 150:
                    FinishLabel2 = Label(FinishPage,text="\nCongrats you get a 1.2x Payout", font="Arial 18 bold",fg="White",bg="#95CEDB").pack()
                    Bet = Bet *1.2
                if 150 <= Points < 250:
                    FinishLabel2 = Label(FinishPage,text="\nCongrats you get a 1.5x Payout", font="Arial 18 bold",fg="White",bg="#95CEDB").pack()
                    Bet = Bet *1.5
                if Points > 250:
                    Finishlabel2 = Label(FinishPage,text="\nCongrats you doubled your bet", font="Arial 20 bold",fg="White",bg="#95CEDB").pack()
                    Bet = Bet *2
                if Bet != 0:
                    Money = Money + Bet
                    FinishLabel = Label(FinishPage, text=("\nYou increased your bet to " + str(Bet)),font="Arial 18 bold",fg="White",bg="#95CEDB").pack()
                ReturnButton = Button(FinishPage,text="Return To Menu",font="Ariel 20",fg="White",bg="#95CEDB",command=lambda:[DeleteFinished()]).pack()


        Next = Button(window,text="Next",width=5,height=2,bg="#95CEDB",fg="White",relief=FLAT,font="Arial 30 bold",command=lambda:[CallOut(),TextUpdate(),FinishPage(),PointUpdate(),PlayerCard()])
        Next.grid(row=2,column=4)

        PointWord = Label(window,text="\n\nPoints:",font="Arial 30 bold",bg="#95CEDB",fg="White")
        PointWord.grid(column=4,row=3)
        PointText = Label(window,text=Points,font="Arial 50 bold",bg="#95CEDB",fg="White")
        PointText.grid(column=4,row=4)
        PlayerCard()
    SplashScreenFunction()
    mainloop()
    return Money
