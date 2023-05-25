"""
wordle.py

This program attempts to create wordle in python using tkinter
"""

__author__ = "James Miller"
__version__ = "May 22, 2023"

from tkinter import *
from tkinter import ttk

def create_window():
    root = Tk()
    root.geometry("800x500")
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
            print(e)

    for key in range(len(top_row)):
        ttk.Button(text=top_row[key], command=(lambda c=top_row[key] : key_press(ops[c]))).grid(column=key, row=7)

    for key in range(len(mid_row)):
        ttk.Button(text=mid_row[key], command=(lambda c=mid_row[key] : key_press(ops[c]))).grid(column=key, row=8)
    
    for key in range(len(bot_row)):
        ttk.Button(text=bot_row[key], command=(lambda c = bot_row[key] : key_press(ops[c]))).grid(column=key, row=9)

    ttk.Button(text="quit", command=root.destroy).grid(column=0, row=10)

    #root.bind('<KeyPress>', key_press)

    root.mainloop()
    

def main():
    create_window()

if __name__ == "__main__":
    main()