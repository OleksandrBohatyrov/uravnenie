from tkinter import *

aken=Tk()
aken.geometry("1200x400")
aken.title("Square")

def initUI(self):
    lbl2.place(x=30,y=20)
lbl=Label(aken,text="Решение квадратного уравнения", bg="lightblue", fg="black",font="Arial 16", height=1, width=30)
ent=Entry(aken, fg="blue", bg="lightblue",width=5, font="Arial 20", justify=CENTER)
lbl2=Label(aken,text="x**2", bg="lightblue", fg="black",font="Arial 16", height=1, width=10)
ent2=Entry(aken, fg="blue", bg="lightblue",width=5, font="Arial 20", justify=CENTER)


lbl.pack()

ent.pack(side=LEFT, padx=20, pady=30)
lbl2.pack()
ent2.pack(side=LEFT, padx=20, pady=30)
aken.mainloop()   
