from tkinter import*

t = Tk()
t.title("TEST")
t.geometry("500x500")
t.configure(bg="light blue")
l = Label(t,text = "Sign IN please")
def shows():
    email = a.get()
    
    pw = b.get()
    l.configure(text= pw)
    

b = Button(t,text= "Sign in", command = shows, bg ="red",fg="black")
l.grid(column= 0,row = 0)
a = Entry(t,width= 10)
a.grid(column= 1,row= 0)

b = Entry(t,width=10)
b.grid(column= 1,row= 0)
t.mainloop()


