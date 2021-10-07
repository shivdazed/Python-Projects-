from tkinter import *
from tkinter import messagebox
a = Tk()
a.title("my 1st page")
a.geometry("500x500")
a.configure(bg="red")


messagebox.showinfo('information','The page is created')
messagebox.showwarning('warning','careful...')
a.mainloop()

