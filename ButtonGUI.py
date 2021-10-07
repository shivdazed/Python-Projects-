from tkinter import*
from tkinter import messagebox

a = Tk()
a.title("Button")
a.geometry("500x500")
a.configure(bg="white")
def func():
    messagebox.showinfo("Message","YOOO IT worked!")
    
    print("It worked here tooo!!")

w=Button(a,text='Press',width=25,command= func)

w.place(relx= 0.5,rely=0.5,anchor = CENTER)

a.mainloop()
