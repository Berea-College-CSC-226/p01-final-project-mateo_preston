#importing everything needed for the program
import tkinter as tk
from tkinter import ttk
import random

#class app used to create the screen and do basic set up such as screen size and title
#also created a way to switch between screens with container mainloop keeps the screen up
#and style updates the windows to look more modern
class App(tk.Tk):

    def __init__(self):
        #setup
        super().__init__()
        self.title("Game Of Nim")
        self.geometry("800x800")
        self.minsize(400, 200)

        self.container = ttk.Frame(self)
        self.container.pack(expand=True, fill="both")

        self.show_frame("menu")

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.mainloop()
# used to switch between frames to act as differen screens
    def show_frame(self, page_name, **kwargs):
        for widget in self.container.winfo_children():
            widget.destroy()

        if page_name == "menu":
            self.current_frame = Menu(self.container, self)
        elif page_name == "game":
            self.current_frame = GameBoard(self.container, self, kwargs.get("count"))

#basic set up for menu screen such as collumn and row set up and all logic
class Menu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pack(expand=True, fill='both')

        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2,3,4), weight=1)

        self.item_count = tk.IntVar(value=15)
        self.vs_computer=tk.IntVar(value=0)

        self.create_widgets()

#where all the gui for the menu screen is created
    def create_widgets(self):
        toggle = ttk.Checkbutton(self, text="Play against Computer?", variable=self.vs_computer)
        toggle.grid(column=1, row=3, pady=10)

        label = ttk.Label(self, text="Select Number of Items:", font=("Arial", 12))
        label.grid(column=1, row=1, pady=10)

        slider = tk.Scale(self, from_=15, to=30, orient=tk.HORIZONTAL, variable = self.item_count)
        slider.grid(column=1, row=2, sticky="ew", padx=50)

        start_btn = ttk.Button(self, text="Start Game", command=self.start_game)
        start_btn.grid(column=1, row=4, pady=20, ipadx=20, ipady=10)

#logic for start game button switches frames
    def start_game(self):
        count = self.item_count.get()
        self.controller.show_frame("game", count=count)

#setup for the gameboard screen
class GameBoard(ttk.Frame):
#basic setup for gameboard logic and buttons
    def __init__(self, parent, controller, count):
        super().__init__(parent)
        self.controller = controller
        self.count = count
        self.current_player = 1
        self.pack(expand=True, fill='both')

        self.reset_btn = ttk.Button(self, text="play again", command=self.reset_game)

        self.turn_label = ttk.Label(self, text="Player 1's Turn:", font=("Arial", 16, "bold"))
        self.turn_label.pack(pady=10)

        self.count_label = ttk.Label(self, text=f"{count} Balls Left!", font=("Arial", 12))
        self.count_label.pack(pady=10)

        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10)

        self.btn1 = ttk.Button(self.button_frame, text="Take 1", command=self.take_1)
        self.btn1.grid(row=1, column=0, padx=5)

        self.btn2 = ttk.Button(self.button_frame, text="Take 2", command=self.take_2)
        self.btn2.grid(row=1, column=1, padx=5)

        self.btn3 = ttk.Button(self.button_frame, text="Take 3", command=self.take_3)
        self.btn3.grid(row=1, column=2, padx=5)

        self.btn4 = ttk.Button(self.button_frame, text="Take 4", command=self.take_4)
        self.btn4.grid(row=1, column=3, padx=5)

        ttk.Button(self, text="Quit To Menu", command=self.go_back).pack(side="bottom")

        self.draw_marbles()

#this functions use the canvas to draw the balls also used to update the screen
    def draw_marbles(self):
        self.canvas.delete("all")

        for i in range(self.count):
            x = 20 + (i % 10) * 35
            y = 20 + (i // 10) * 35
            self.canvas.create_oval(x, y, x+25, y+25, fill="red", outline="black")

#setup for the take buttons maps to the makemove function below
    def take_1(self): self.make_move(1)
    def take_2(self): self.make_move(2)
    def take_3(self): self.make_move(3)
    def take_4(self): self.make_move(4)

#call by the take functions above used for the real logic to take the balls and update the game
    def make_move(self, amount):
        if self.count >= amount:
            self.count -= amount
            self.update_game()

#calls the draw_marbles function from above to update the game when needed also sets new text on the label
#changes players turn and colors
    def update_game(self):
        self.draw_marbles()
        self.count_label.configure(text=f"Balls Remaining: {self.count}")

        if self.count <= 0:
            self.turn_label.config(text=f"Game Over! Player {self.current_player} Wins!", foreground="green")
            self.final_disable()
        else:
            if self.current_player == 1:
                self.current_player = 2
                self.turn_label.config(text="Player 2's Turn", foreground="darkorange")
            else:
                self.current_player = 1
                self.turn_label.config(text="Player 1's Turn", foreground="royalblue")
            self.check_disable()

#checks to make sure no buttons need to be disabled due to not enough balls after each turn
    def check_disable(self):
        self.btn1.config(state="normal" if self.count >= 1 else "disabled")
        self.btn2.config(state="normal" if self.count >= 2 else "disabled")
        self.btn3.config(state="normal" if self.count >= 3 else "disabled")
        self.btn4.config(state="normal" if self.count >= 4 else "disabled")

#gets called and disables all take buttons while displaying a play again button
    def final_disable(self):
        self.btn1.config(state="disabled")
        self.btn2.config(state="disabled")
        self.btn3.config(state="disabled")
        self.btn4.config(state="disabled")
        self.reset_btn.pack(pady=10)

#reset button to logic to reset the game at the end to skip the menu screen
    def reset_game(self):
        self.controller.show_frame("game", count=15)

#go back button is similar to reset but takes you to the menu screen to be able to make changes
    def go_back(self):
        self.controller.show_frame("menu")


#creates the object for app class and starts the program
if __name__ == "__main__":
    App()