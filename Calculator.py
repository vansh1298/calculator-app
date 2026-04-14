#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      hp
#
# Created:     14 04 2026
# Copyright:   (c) hp 2026
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from tkinter import *

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.delete(0, END)
            screen.insert(END, result)
        except:
            screen.delete(0, END)
            screen.insert(END, "Error")

    elif text == "C":
        screen.delete(0, END)

    elif text == "⌫":
        current = screen.get()
        screen.delete(0, END)
        screen.insert(END, current[:-1])

    else:
        screen.insert(END, text)

root = Tk()
root.title("Calculator")
root.geometry("300x450")

screen = Entry(root, font="Arial 20")
screen.pack(fill=X, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "⌫", "+"],
    ["="]
]

for row in buttons:
    frame = Frame(root)
    frame.pack()

    for btn in row:
        button = Button(frame, text=btn, font="Arial 14", padx=20, pady=15)
        button.pack(side=LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()