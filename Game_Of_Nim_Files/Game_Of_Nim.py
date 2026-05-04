import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self):
        #setup
        super().__init__()
        self.title("Game Of Nim")
        self.geometry("600x600")
        self.minsize(400, 400)

        self.container = ttk.Frame(self)
        self.container.pack(expand=True, fill="both")

        self.show_frame("menu")

        self.mainloop()

    def show_frame(self, page_name, **kwargs):
        for widget in self.container.winfo_children():
            widget.destroy()

        if page_name == "menu":
            self.current_frame = Menu(self.container, self)
        elif page_name == "game":
            self.current_frame = GameBoard(self.container, self, kwargs.get("count"))

class Menu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pack(expand=True, fill='both')

        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2,3,4), weight=1)

        self.item_count = tk.IntVar(value=15)
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Select Number of Items:", font=("Arial", 12))
        label.grid(column=1, row=1, pady=10)

        slider = tk.Scale(self, from_=15, to=30, orient=tk.HORIZONTAL, variable = self.item_count)
        slider.grid(column=1, row=2, sticky="ew", padx=50)

        start_btn = ttk.Button(self, text = "Start Game", command=self.start_game)
        start_btn.grid(column=1, row=3, pady=20, ipadx=20, ipady=10)



    def start_game(self):
        count = self.item_count.get()
        self.controller.show_frame("game", count=count)

class GameBoard(ttk.Frame):
    def __init__(self, parent, controller, count):
        super().__init__(parent)
        self.pack(expand=True, fill='both')
        ttk.Label(self, text=f"Game started with {count} Balls!").pack(pady=20)
        ttk.Button(self, text="back", command=lambda: controller.show_frame("menu")).pack()

if __name__ == "__main__":
    App()