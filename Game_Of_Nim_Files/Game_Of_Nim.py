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
        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        self.create_widgets()

    def create_widgets(self):
        test = ttk.Button(self, text = "test")

        entry = ttk.Entry(self)

        self .columnconfigure((0,1,2), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = "a")

        test.grid(column = 0, row = 0, sticky = "nswe", columnspan = 2)


def main():
    test = App()

if __name__ == "__main__":
    main()