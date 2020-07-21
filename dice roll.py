import tkinter
import random
from tkinter import *
root = Tk()
root.geometry('700x450')

l1 = Label(root,font=("times",260))
def roll():
    print("this is dice rool")
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()
b1 = Button(root,text='roll dice..',command=roll,fg='blue')
b1.place(x=300,y=0)
b1.pack()


root.mainloop()



