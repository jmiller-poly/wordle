"""
wordle.py

This program attempts to create wordle in python using tkinter
"""

__author__ = "James Miller"
__version__ = "May 22, 2023"

from tkinter import *
from tkinter import ttk

def create_window():
    win = Tk()
    win.geometry("500x500")
    top_row = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
    mid_row = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
    bot_row = ["enter", "Z", "X", "C", "V", "B", "N", "M", "backspace"]

    ops = {
        "A" : "A",
        "B" : "B",
        "C" : "C",
        "D" : "D",
        "E" : "E",
        "F" : "F",
        "G" : "G",
        "H" : "H",
        "I" : "I",
        "J" : "J",
        "K" : "K",
        "L" : "L",
        "M" : "M",
        "N" : "N",
        "O" : "O",
        "P" : "P",
        "Q" : "Q",
        "R" : "R",
        "S" : "S",
        "T" : "T",
        "U" : "U",
        "V" : "V",
        "W" : "W",
        "X" : "X",
        "Y" : "Y",
        "Z" : "Z",
        "enter" : "\n",
        "backspace" : "\b"
        
    }

    def key_press(e):
        if e == "\b":
            print("\\b")
        elif e == "\n":
            print("\\n")
        else:
            guesses[0].configure(text=e)

    guesses = [Label(win, text="_ _ _ _ _", font="Times 24") for _ in range(6)]
    for g in guesses:
        g.pack()

    for i in range(len(top_row)):
        key = ttk.Button(text=top_row[i], command=(lambda c=top_row[i] : key_press(ops[c])))
        key.place(anchor=NW, x=50*i, y=300, width=50, height=50)

    for i in range(len(mid_row)):
        key = ttk.Button(text=mid_row[i], command=(lambda c=mid_row[i] : key_press(ops[c])))
        key.place(anchor=NW, x=50*i, y=350, width=50, height=50)

    for i in range(len(bot_row)):
        key = ttk.Button(text=bot_row[i], command=(lambda c = bot_row[i] : key_press(ops[c])))
        key.place(anchor=NW, x=50*i, y=400, width=50, height=50)

    key = ttk.Button(text="backspace", command=(lambda c = bot_row[i] : key_press("\b")))
    key.place(anchor=NW, x=50*i, y=400, width=100, height=50)   

    quit = ttk.Button(text="quit", command=win.destroy)
    quit.place(anchor=NW, x=450, y=350, width=50, height=50)

    #root.bind('<KeyPress>', key_press)

    win.mainloop()
    

def main():
    create_window()

if __name__ == "__main__":
    main()