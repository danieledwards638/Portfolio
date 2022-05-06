from tkinter import *

calculation=''
def addtocalc(symbol):
    global calculation
    calculation+=symbol
    calcans.config(text=calculation)

def clearcalc():
    global calculation
    calc.config(text='')
    calcans.config(text='')
    calculation=''

def execcalc():
    global calculation
    calculation=calculation.replace(")(",")*(")
    try:
        calcans.config(text=(eval(calculation)))
    except:
        calcans.config(text="ERROR")



window = Tk()
window.title("Calculator")
Grid.rowconfigure(window, 0,weight=1,minsize=20)
Grid.columnconfigure(window, 0,weight=1,minsize=20)
frame = Frame(master=window)
frame.rowconfigure([0,1,2,3,4,5],weight=1)
frame.columnconfigure([0,1,2,3,4],weight=1)
frame.grid(sticky="nsew",padx=5,pady=5)

calc=Label(text="",font='Helvetica 13 bold')
calc.grid(row=4,sticky="nsew")
calcans=Label(text="",font='Helvetica 13 bold')
calcans.grid(row=5,sticky="nsew")

one=Button(master=frame,text="1",command=(lambda: addtocalc("1")),height=7,width=14,font='Helvetica 13 bold')
one.grid(row=0,column=0,sticky="nsew")

two=Button(master=frame,text="2",command=(lambda: addtocalc("2")),height=7,width=14,font='Helvetica 13 bold')
two.grid(row=0,column=1,sticky="nsew")

three=Button(master=frame,text="3",command=(lambda: addtocalc("3")),height=7,width=14,font='Helvetica 13 bold')
three.grid(row=0,column=2,sticky="nsew")

four=Button(master=frame,text="4",command=(lambda: addtocalc("4")),height=7,width=14,font='Helvetica 13 bold')
four.grid(row=1,column=0,sticky="nsew")

five=Button(master=frame,text="5",command=(lambda: addtocalc("5")),height=7,width=14,font='Helvetica 13 bold')
five.grid(row=1,column=1,sticky="nsew")

six=Button(master=frame,text="6",command=(lambda: addtocalc("6")),height=7,width=14,font='Helvetica 13 bold')
six.grid(row=1,column=2,sticky="nsew")

seven=Button(master=frame,text="7",command=(lambda: addtocalc("7")),height=7,width=14,font='Helvetica 13 bold')
seven.grid(row=2,column=0,sticky="nsew")

eight=Button(master=frame,text="8",command=(lambda: addtocalc("8")),height=7,width=14,font='Helvetica 13 bold')
eight.grid(row=2,column=1,sticky="nsew")

nine=Button(master=frame,text="9",command=(lambda: addtocalc("9")),height=7,width=14,font='Helvetica 13 bold')
nine.grid(row=2,column=2,sticky="nsew")

zero=Button(master=frame,text="0",command=(lambda: addtocalc("0")),height=7,width=14,font='Helvetica 13 bold')
zero.grid(row=3,column=1,sticky="nsew")

point=Button(master=frame,text=".",command=(lambda: addtocalc(".")),height=7,width=14,font='Helvetica 13 bold')
point.grid(row=3,column=2,sticky="nsew")

clear=Button(master=frame,text="Clear equation.",command=clearcalc,height=7,width=14,font='Helvetica 13 bold')
clear.grid(row=3,column=0,sticky="nsew")

add=Button(master=frame,text="+",command=(lambda: addtocalc("+")),height=7,width=14,font='Helvetica 13 bold')
add.grid(row=0,column=3,sticky="nsew")

minus=Button(master=frame,text="-",command=(lambda: addtocalc("-")),height=7,width=14,font='Helvetica 13 bold')
minus.grid(row=1,column=3,sticky="nsew")

times=Button(master=frame,text="x",command=(lambda: addtocalc("*")),height=7,width=14,font='Helvetica 13 bold')
times.grid(row=2,column=3,sticky="nsew")

divide=Button(master=frame,text="/",command=(lambda: addtocalc("/")),height=7,width=14,font='Helvetica 13 bold')
divide.grid(row=3,column=3,sticky="nsew")

sum=Button(master=frame,text="=",command=execcalc,height=7,width=14,font='Helvetica 13 bold')
sum.grid(row=3,column=4,sticky="nsew")

leftBracket=Button(master=frame,text="(",command=(lambda: addtocalc("(")),height=7,width=14,font='Helvetica 13 bold')
leftBracket.grid(row=1,column=4,sticky="nsew")

rightBracket=Button(master=frame,text=")",command=(lambda: addtocalc(")")),height=7,width=14,font='Helvetica 13 bold')
rightBracket.grid(row=2,column=4,sticky="nsew")

window.mainloop()