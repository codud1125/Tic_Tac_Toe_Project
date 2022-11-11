from tkinter import *
from start_screen import *

root = Tk()
root.title("Tic Tac Toe game")
root.config(padx=50, pady=50)

canvas = Canvas(width = 300, height = 300)
canvas.pack()

startScreen = startScreen(root, canvas)

root.mainloop()