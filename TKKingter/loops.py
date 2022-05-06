import tkinter as tk
import random

def roll():
    lbl_value["text"]=random.randint(1,6)


window = tk.Tk()
window.rowconfigure([0,1],minsize=50,weight=1)
window.columnconfigure([0],minsize=50,weight=1)
window.configure(bg="light blue")

btn=tk.Button(master=window,text="Roll",command=roll,bg="light green")
btn.grid(row=1,column=0,sticky="nsew")

lbl_value=tk.Label(master=window,text="0",bg="lightblue")
lbl_value.grid(row=0,column=0)


window.mainloop()