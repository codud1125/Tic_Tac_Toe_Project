from tkinter import *
import os
from PIL import ImageTk, Image

class startScreen:

    def __init__(self, root, canvas):

        for child in canvas.winfo_children():
            child.destroy()


        self.wd = os.getcwd()
        self.block_image = ImageTk.PhotoImage(Image.open(self.wd + '/block.png'))
        self.jinbae_image = ImageTk.PhotoImage(Image.open(self.wd + '/jinbae.png'))
        self.chunbae_image = ImageTk.PhotoImage(Image.open(self.wd + '/chunbae.png'))

        self.click_attempt = 0

        self.player1_list = []
        self.player2_list = []

        self.winning_list = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (2, 0), (2, 2)]
        ]

        for row in range(0, 3):
            for col in range (0, 3):
                cell = Button(canvas, image = self.block_image, borderwidth = 1, highlightthickness=0)
                cell.configure(command = lambda cellinput = cell, rowinput = row, colinput = col: self.click_block(root, canvas, cellinput, rowinput, colinput))
                cell.image = self.block_image
                cell.grid(row=row, column=col, rowspan=1, columnspan=1, sticky=N+S+E+W)

        self.label_player1 = Label(canvas, text='Player 1', font = 'Helvetica 14', fg='red')
        self.label_player1.grid(row=3, column=0)

        self.label_player2 = Label(canvas, text='Player 2', font = 'Helvetica 14')
        self.label_player2.grid(row=3, column=2)


    def click_block(self, root, canvas, cell, row, col):

        self.click_attempt += 1
        
        if (self.click_attempt % 2 == 1):
            cell.configure(image=self.jinbae_image)
            cell['command']=0
            self.label_player1.config(font = 'Helvetica 14', fg='black')
            self.label_player2.config(font = 'Helvetica 14', fg='red')
            self.player1_list.append((row, col))
        else:
            cell.configure(image=self.chunbae_image)
            cell['command']=0
            self.label_player2.config(font = 'Helvetica 14', fg='black')
            self.label_player1.config(font = 'Helvetica 14', fg='red')
            self.player2_list.append((row, col))

        for winning_entry in self.winning_list:
            if (all(x in self.player1_list for x in winning_entry)):
                for child in canvas.winfo_children():
                    child.destroy()

                self.winning_label = Label(canvas, text='Player 1 wins!', font = 'Helvetica 14', fg='red')
                self.winning_label.grid(row=0, column=0)

                self.restart_btn = Button(canvas, text='Restart the game', font = ('Helvetica', 10), borderwidth = 0, highlightthickness=0, command=lambda: self.restart(root, canvas))
                self.restart_btn.grid(row=1, column=0)


            if (all(x in self.player2_list for x in winning_entry)):
                for child in canvas.winfo_children():
                    child.destroy()

                self.winning_label = Label(canvas, text='Player 2 wins!', font = 'Helvetica 14', fg='red')
                self.winning_label.grid(row=0, column=0)

                self.restart_btn = Button(canvas, text='Restart the game', font = ('Helvetica', 10), borderwidth = 0, highlightthickness=0, command=lambda: self.restart(root, canvas))
                self.restart_btn.grid(row=1, column=0)


    def restart(self, root, canvas):
        restartScreen = startScreen(root, canvas)



