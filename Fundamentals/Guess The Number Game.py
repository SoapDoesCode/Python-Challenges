import random
import os
from os import system, name

max_num = int(input("Maximum number: "))

def clear_output():
    if name == "nt":
        system("cls")
    else:
        system("clear")

num_wins = 0

def choose_number(max_num):
    global num_wins

    clear_output()

    print("Type 'quit' to stop the game")
    print(f"Choosing number from 1-{max_num}")

    chosen_number = random.randint(1, max_num)

    correct_num = False

    while not correct_num:
        user_guess = input("Your guess: ")
        user_guess_int = int(user_guess)
        
        if user_guess == "quit":
            print(f"You won {num_wins} games!\nQuitting game...")
            exit()
        elif user_guess_int == chosen_number:
            num_wins += 1
            print(f"Well done! Your guessed correctly!")
            
            play_again = input("Play again? (y/n): ")
            play_again = play_again.lower()

            clear_output()

            if play_again == "y" or play_again == "yes":
                print("Type 'quit' to stop the game")
                correct_num = True
            else:
                print(f"You won {num_wins} games!\nQuitting game...")
                exit()
        else:
            if user_guess_int > chosen_number:
                print("Too high! Try again!")
            else:
                print("Too low! Try again!")

while True:
    choose_number(max_num)
