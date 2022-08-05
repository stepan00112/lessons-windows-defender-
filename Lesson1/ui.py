from logging import root
import imports
from tkinter import *
from random import randint
def send(input_,output):
    global root
    print(input_,output)
    if imports.password.a_to_b(input)==output:
        
        root.quit()
        
def start():
    global num,root
    root=Tk()
    num=randint(1,9)
    Label(text=num).pack()

    password = Entry(show='*')
    password.pack()

    Button(text='send',command=lambda:send(int(password.get()),num)).pack()

    root.mainloop()