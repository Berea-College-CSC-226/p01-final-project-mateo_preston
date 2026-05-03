import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self):
        #setup
        super().__init__()
        self.title("Game Of Nim")
        self.geometry("600x600")
        self.minsize(600, 600)


        #widgets
        self.menu = Menu(self)

        #run the app
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

def main():
    test = App()

if __name__ == "__main__":
    main()