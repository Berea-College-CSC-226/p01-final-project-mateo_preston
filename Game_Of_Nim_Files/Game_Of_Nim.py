import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self):
        #setup
        super().__init__()
        self.title("Game Of Nim")
        self.geometry("600x600")
        self.minsize(400, 400)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        #widgets
        self.menu = Menu(self)

        #run the app
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand=True, fill='both')

        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2,3,4), weight=1)

        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Number of Items:", font=("Arial", 12))
        label.grid(column=1, row=1, pady=10)

        slider = ttk.LabeledScale(self, from_=15, to=30)
        slider.grid(column=1, row=2, sticky="ew", padx=50)

        start_btn = ttk.Button(self, text = "Start Game", command=self.start_game)
        start_btn.grid(column=1, row=3, pady=20, ipadx=20, ipady=10)



    def start_game(self):
        print(f"Starting game with {self.item_count.get()} items!")



if __name__ == "__main__":
    App()