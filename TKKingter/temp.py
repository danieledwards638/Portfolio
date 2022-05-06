import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter! ")
window.geometry("300x150")
window.maxsize(width=300,height=150)
window.minsize(width=300,height=150)

def convert1():
    ent2.delete(0,tk.END)
    ent2.insert(0,(str(round(((float(ent1.get())-32)*(5/9)),2))))
def convert2():
    ent1.delete(0,tk.END)
    ent1.insert(0,(str(round((float(ent2.get())*(9/5))+32))))

frm=tk.Frame(master=window)
frm.pack()

lbl1=tk.Label(master=frm,text="Enter your temperature in Farenheit")
lbl1.pack()

ent1=tk.Entry(master=frm,text='')
ent1.pack(padx=20)

btn1=tk.Button(master=frm,text="Convert F to C",command=convert1)
btn1.pack()

lbl2=tk.Label(master=frm,text="Enter your temperature in Celsius")
lbl2.pack()
ent2=tk.Entry(master=frm,text='')
ent2.pack()

btn2=tk.Button(master=frm,text="Convert C to F",command=convert2)
btn2.pack()

window.mainloop()