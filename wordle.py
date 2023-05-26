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
    keyboard = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], ["A", "S", "D", "F", "G", "H", "J", "K", "L"], ["enter", "Z", "X", "C", "V", "B", "N", "M", "backspace"]]

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
        if e == "backspace":
            print("\\b")
        elif e == "enter":
            print("\\n")
        else:
            before = guesses[0].cget("text")
            guesses[0].configure(text=e)

    guesses = [Label(win, text="", font="Times 24") for _ in range(6)]
    for g in guesses:
        g.config(bg="black", fg="white")
        g.pack()

    for row in range(len(keyboard)):
        for ch in range(len(keyboard[row])):
            if keyboard[row][ch] == "backspace":
                key = ttk.Button(text=keyboard[row][ch], command=(lambda c=keyboard[row][ch] : key_press(c)))
                key.place(anchor=NW, x=50*ch, y=300+row*50, width=100, height=50)
            else:
                key = ttk.Button(text=keyboard[row][ch], command=(lambda c=keyboard[row][ch] : key_press(c)))
                key.place(anchor=NW, x=50*ch, y=300+row*50, width=50, height=50)

    quit = ttk.Button(text="quit", command=win.destroy)
    quit.place(anchor=NW, x=450, y=350, width=50, height=50)

    #root.bind('<KeyPress>', key_press)

    win.mainloop()
    

def main():
    create_window()

if __name__ == "__main__":
    main()