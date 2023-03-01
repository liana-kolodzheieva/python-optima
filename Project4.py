from tkinter import *

from tkinter import messagebox


def change1(event):
    w1.geometry('400x400')

    w1['bg'] = 'violet'

    w1.title('8_-Class')

    w1.minsize(100, 200)

    w1.maxsize(600, 900)


def change2(event):
    messagebox.showinfo('Liana Kolodgeeva', 'Yep, I did it!')


w1 = Tk()

w1.bind('<Button-1>', change1)

w1.bind('<Button-3>', change2)

w1.mainloop()
