import time
#creates menu list
with open("menu2.txt","r") as f:
    global menu
    menu=f.readline()
    menu=menu.split(',')
#creates prices list
with open("prices2.txt","r") as f:
    global prices
    prices=f.readline()
    prices=prices.split(',')
    prices=list(map(float, prices))
#creates order frequency list
with open("Frequency.txt","r") as f:
    global Frequency
    Frequency=f.readline()
    Frequency=Frequency.split(',')
    Frequency=list(map(int,Frequency))


#sub program to order food
def Order():
    total=0
    #input order and turn to list
    userInput=str((input("Enter Your Order in the correct format. Example: '6(table number), 4, 4, 7, 8, 10, 10'. Type 'c' to cancel order:  ")).replace(' ',''))
    #cancel order
    if userInput.lower()=="c":
        print("Returning you to main menu...")
        return
    userInput=userInput.split(',')
    #input validation
    try:
        userInput=list(map(int, userInput))
    except:
        print("You entered a value that is not an integer, returning you to main menu.")
        return
    #creates tableNumber variable for the first digit entered
    tableNumber=userInput[0]
    if tableNumber>10:
        print("Invalid Table number, returning to menu.")
        return
    elif tableNumber<1:
        print("Invalid Table number, returning to menu.")
        return
    #removes table number from order list
    userInput.remove(userInput[0])
    print(userInput)
    #Ask user if they want to change their order
    choice=input('You have ordered these numbered items. Would you like to change them? (Yes/No)')
    if choice.upper()=="YES":
        Order()
        return
    print("Table number: ",str(tableNumber))
    for i in range(len(userInput)):
        #input validation
        if int(userInput[0])<1 or int(userInput[i])>len(menu):
            print("The number of your item is out of bounds, returning you to main menu.")
            return
        #prints and saves order to file
        print(menu[int(userInput[i])-1])
        saveOrder=open("Orders2.txt","a")
        saveOrder.write(menu[int(userInput[i])-1]+"\n")
        #adds 1 to the frequency list with index[i]
        Frequency[int(userInput[i])-1]+=1
        #outputs total cost of order
        total+=prices[int(userInput[i])-1]
    print('£'+str(total))
    saveOrder.write('£'+str(total))
    saveOrder.write('\n\n\n\n\n')
    #saves frequency to file
    saveFreq=open("Frequency.txt",'w')
    with open("Frequency.txt","w") as f:
        saveFreq.write(str(Frequency[0]))
        for i in range(len(Frequency)-1):
            saveFreq.write(","+str(Frequency[i+1]))

#adding to menu
def addMenu():
    item=input("Enter the name of the item you want to add: ")
    itemprice=input("Enter the price of the item you want to add: ")
    #input validation
    try:
        itemprice=float(itemprice)
    except:
        print("The number you wrote is not a valid number, please return to main menu and try again. The correct format is x.xx (1.25). ")
        return
    #adds to menu and price
    menu.append(item)
    prices.append(float(itemprice))
    #writes menu and prices to file
    with open("menu2.txt","w") as f:
        f.write(menu[0])
        for i in range(len(menu)-1):
            f.write(","+menu[i+1])
    with open("prices2.txt","w") as f:
        f.write(str(prices[0]))
        for i in range(len(menu)-1):
            f.write(","+str(prices[i+1]))


#deleting item from menu
def delMenu():
    item=input("Enter the name of the item you want to Remove: ")
    index=menu.index(item)
    menu.remove(item)
    prices.remove(prices[index])
    with open("menu2.txt","w") as f:
        f.write(menu[0])
        for i in range(len(menu)-1):
            f.write(","+menu[i+1])
    with open("prices2.txt","w") as f:
        f.write(str(prices[0]))
        for i in range(len(menu)-1):
            f.write(","+str(prices[i+1]))


#viewing the menu
def vMenu():
    for i in range(len(menu)):
        print(str(i+1)+": "+menu[i]+", £"+str(prices[i]))


#main loop for choice
while True:
    decision=input("""
    Do you want to:
    Order(1)
    Add to Menu(2)
    Remove from Menu(3)
    View Menu(4)
    menuFrequency(5)
    Exit(6)

    """)
    if decision=="1":
        Order()
    elif decision=="2":
        addMenu()
    elif decision=="3":
        delMenu()
    elif decision=="4":
        vMenu()
    elif decision=="5":
        print(Frequency)
    elif decision=="6":
        print("Thank you for stopping by! ")
        exit()
    else:
        print("Your Choice was not valid, returning to main menu.")
    time.sleep(3)