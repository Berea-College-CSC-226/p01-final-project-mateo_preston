import random

def start_game():
    print("Welcome to the game of Nim!")
    print("Rules:")
    print(" - You choose a number of balls to play with (minimum 15).")
    print(" - On your turn, you can remove 1, 2, 3, or 4 balls.")
    print(" - Players take turns until someone takes the last ball — that player wins!")

    while True:
        try:
            balls = int(input("How many balls do you want to use? Minimum 15: "))
            if balls >= 15:
                return balls
            else:
                print("Number must be at least 15.")
        except ValueError:
            print("Please enter a valid number.")

def game_of_nim_user(balls):
    balls_left = balls
    max_remove = min(4, balls_left)

    print(f"\nYou have {balls_left} balls left.")
    print(f"You may remove between 1 and {max_remove} balls.")

    while True:
        try:
            user_input = int(input(f"How many balls do you want to remove (1-{max_remove})? "))
            if 1 <= user_input <= max_remove:
                break
            else:
                print("This is an invalid input.")
        except ValueError:
            print("Please enter a valid number.")

    balls_left -= user_input

    if balls_left == 0:
        print("You win!")

    return balls_left

def game_of_nim_computer(balls):
    balls_left = balls
    computer_remove = balls_left % 5
    if computer_remove == 0:
        computer_remove = random.randint(1, 4)

    balls_left -= computer_remove
    print(f"\nComputer removed {computer_remove} balls")

    if balls_left == 0:
        print("You lose!")

    return balls_left

def main():
    balls = start_game()

    while balls > 0:
        balls = game_of_nim_user(balls)
        if balls == 0:
            break
        balls = game_of_nim_computer(balls)

main()