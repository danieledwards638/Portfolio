import tkinter as tk

def entry():
    name=entry1.get()
    if name=='':
        return
    email=entry2.get()
    if email=='':
        return
    message=text1.get("1.0",tk.END)
    if message=='':
        return
    gender=list1.get(tk.ACTIVE)
    if gender=='':
        return
    print(name+"\n"+email+"\n"+gender+"\n"+message)



window = tk.Tk()
window.minsize(400,100)
window.configure(bg="#29bdc1")
window.title("Entry Form")

window.columnconfigure(0,minsize=250,weight=1)
window.rowconfigure([0,6],minsize=100,weight=1)

entry1=tk.Entry(master=window)
lbl1=tk.Label(text="Enter your name.",bg="#29bdc1",font="ComicSans")
lbl1.grid(row=0,sticky="n")
entry1.grid(row=0,sticky="ew",padx=200)

entry2=tk.Entry(master=window)
lbl2=tk.Label(text="Enter your Email.",bg="#29bdc1",font="ComicSans")
lbl2.grid(row=1,sticky="n")
entry2.grid(row=2,sticky="ew",padx=80,pady=20)

# Found on TkDocs
choices=["MALE","FEMALE","other"]
choicesvar=tk.StringVar(value=choices)
lbl3=tk.Label(text="Choose your gender.",bg="#29bdc1",font="ComicSans")
lbl3.grid(row=3,padx=15)
list1=tk.Listbox(selectmode="SINGLE",listvariable=choicesvar)
list1.grid(row=4,padx=15)

text1=tk.Text(master=window)
lbl3=tk.Label(text="Enter your message. ",bg="#29bdc1",font="ComicSans")
lbl3.grid(row=5,sticky="ew",padx=15)
text1.grid(row=6,sticky="nsew",padx=80,pady=15)

button1=tk.Button(master=window,text="Submit",command=entry,bg="light green",font="ComicSans")
button1.grid(row=7)




window.mainloop()