"""
wordle.py

This program attempts to create wordle in python using tkinter
"""

__author__ = "James Miller"
__version__ = "May 26, 2023"

from tkinter import *
from tkinter import ttk

def create_window():
    global guess_num
    win = Tk()
    win.geometry("500x500")
    keyboard = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], 
                ["A", "S", "D", "F", "G", "H", "J", "K", "L"], 
                ["enter", "Z", "X", "C", "V", "B", "N", "M", "backspace"]]

    guess_num = 0

    def key_press(e):
        global guess_num
        before = guesses[guess_num].cget("text")
        if e == "backspace" or e == "\b":
            guesses[guess_num].configure(text=before[0:len(before)-1])
        elif (e == "enter" or e == "\n") and len(before) == 5:
            guess_num += 1
        else:
            if len(before) < 5:
                guesses[guess_num].configure(text=before + e)

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