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

    box = ttk.Entry().grid(row=0, column=2)

    """def key_press(e):
        if e.char == "\b":
            if len(prev_text) > 0:
                prev_text = prev_text[0:len(prev_text)-1]
        elif e.char == "\n":
            pass
        else:
            pt += e.char
            ttk.Label(text=prev_text).grid(column=3, row=0)"""

    for key in range(len(top_row)):
        ttk.Button(text=top_row[key]).grid(column=key, row=7)

    for key in range(len(mid_row)):
        ttk.Button(text=mid_row[key]).grid(column=key, row=8)
    
    for key in range(len(bot_row)):
        ttk.Button(text=bot_row[key]).grid(column=key, row=9)

    ttk.Button(text="quit", command=root.destroy).grid(column=0, row=10)

    #root.bind('<KeyPress>', key_press)

    root.mainloop()
    

def main():
    create_window()

if __name__ == "__main__":
    main()