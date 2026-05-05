import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox #    WHY DO I HAVE TO IMPORT IT MANUALLY
import random
# import PIL

def test_message():
    messagebox.showinfo("Yay!", "Something happened")

class Single_Nim ():

    def __init__(self, marble_count):
        # Make the window
        self.window = tk.Tk()
        self.window.title("Game of Nim WOOO HELL YEAH SO COOL")

        frame1 = ttk.Frame(self.window, relief=tk.RIDGE) # no idea what relief does
        frame1.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S, padx=30, pady=4)

        # Look at this diarrhea of buttons. Hideous.
        button1 = tk.Button(frame1, text="Take 1 ball", command=self.button_take_1)
        button1.grid(row=1, column=1)

        button2 = tk.Button(frame1, text="Take 2 balls", command=self.button_take_2)
        button2.grid(row=1, column=2)

        button3 = tk.Button(frame1, text="Take 3 balls", command=self.button_take_3)
        button3.grid(row=1, column=3)

        button4 = tk.Button(frame1, text="Take 4 balls", command=self.button_take_4)
        button4.grid(row=1, column=4)
        self.marble_count = marble_count


        #self.marble_frame = tk.Frame(self.window, bg='red', width=300, height=300)
        #self.button_frame = tk.Frame(self.window, bg='green', width=300, height=100)
        #     = self.create_frames() # okay, this is rather confusing but I think I get it
        # Now with frames created, we make a button

        #self.test1 = tk.Button(self.button_frame, text="Take 1 ball", command=self.player_take)
        #self.test1.grid(row=1, column=1)

    def create_frames(self): # This makes the frames. We do this first
        test_frame1 = tk.Frame(self.window, bg='red', width=300, height=300)
        test_frame1.grid(row=1, column=1)

        test_frame2 = tk.Frame(self.window, bg='green', width=300, height=100)
        test_frame2.grid(row=2, column=1)

        return test_frame1, test_frame2

    #def create_buttons (): # Now we want to make the buttons in the frames
    #    pass

    # Tasks for you to do:
    # make a single frame for it to work.
    # FIXME: needs implementation for the following variables:
    # max_take: defaults to 4
    # marble_count: the amount of marbles currently in the field. Can only decrease
    # turn: remembers who's turn it is



    # God this is putrid -----------------------
    def button_take_1(self):
        self.player_take(1)

    def button_take_2(self):
        self.player_take(2)

    def button_take_3(self):
        self.player_take(3)

    def button_take_4(self):
        self.player_take(4)
    # ------------------------------------------

    def player_take(self, taken_marbles):
        # First the player takes marbles
        self.marble_count -= taken_marbles
        print(self.marble_count)
        # Check if they lose
        if self.marble_count == 0:
            print("victory")
            victory("computer")
        else: # Else, pass it to computer's turn
            print("computer's turn")
            self.computer_take()

    def computer_take(self):
        if (self.marble_count - 1) % (4 + 1) != 0:  # Try to stay on the winning path
            print("I'll steal ", self.marble_count % 5)
            self.marble_count -= self.marble_count % 5
        else:
            self.marble_count -= randint(1, 4)
            print("Okay, I'll steal a random amount")

    def change_turn(self):

        while marble_count > 0:
            if marble_count == 0:
                break
            marble_count = computer_take(marble_count)

    def check_win(self):
        pass

    def update_log(self):
        pass


def main ():
    program = Single_Nim(500)
    program.window.mainloop()

if __name__ == "__main__":
    main()