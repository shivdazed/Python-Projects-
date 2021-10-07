from tkinter import*
from tkinter import messagebox

page = Tk()
page.title("My 1st Page")
page.geometry("500x500")
page.configure(bg="")

l1= Label(page,text='violet',bg='violet',fg='violet',width="500",height="5")
l2= Label(page,text='indigo',bg='indigo',fg='indigo',width="500",height="5")
l3= Label(page,text='blue',bg='blue',fg='blue',width="500",height="5")
l4= Label(page,text='green',bg='green',fg='green',width="500",height="5")
l5= Label(page,text='yellow',bg='yellow',fg='yellow',width="500",height="5")
l6= Label(page,text='orange',bg='orange',fg='orange',width="500",height="5")
l7= Label(page,text='red',bg='red',fg='red',width="500",height="5")

l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()

page.mainloop#infinite time run the tk function
