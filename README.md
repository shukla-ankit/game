# game


import tkinter as tk
import pygame as pg

def main():
    window = tk.Tk()
    window.title("Snake")
    window.geometry("400x300")

    #Create a label
    label = tk.Label(window, text= "Use arrow keys to move..")
    label.pack()

    window.mainloop()
    
if __name__ == "__main__":
    main()


