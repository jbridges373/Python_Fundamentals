# import random

# def roll_dice():    
#     roll = random.randint(1, 6)
#     print(f"You rolled a {roll}!")

# def throw_dice():
#     roll_dice()
#     roll_dice()

# def show_welcome():
#     print()
#     print("Welcome to Dice Fight!")
#     print()

# def play_game():
#     show_welcome()
#     throw_dice()

# play_game()


# Challenge: Write some functions!
# You've very generously decided to pick up coffee for six of your favorite coworkers this morning.

# 1. Write a function announcing your coffee run.
# Example output: "I am headed to the coffee shop! Who wants a latte?"
def announce_coffee_run():
    print("I am headed to the coffee shop! Who wants a latte?")


# 2. Write a function to calculate the total cost if you buy them each a latte for £5. In an f
# string, print how many lattes and what the total comes to.
# Example output:
# 6 lattes comes to £30.
def calc_coffee_total(num_lattes):
    cost_per_latte = 5
    total_cost = num_lattes * cost_per_latte
    print(f"{num_lattes} lattes comes to £{total_cost}.")


# 3. Your coworkers thank you profusely. To save a little time, write a function that prints
# "You're welcome!" twice, then call it as many times as you need to thank all six coworkers.
def say_welcome():
    print("You're welcome!")
    print("You're welcome!")

# 4. Put all your function calls in a new function called coffee_run(), and call it to start your
# coffee run!
def coffee_run():
    announce_coffee_run()
    calc_coffee_total(6)
    say_welcome()
    say_welcome()
    say_welcome()

# Call the coffee_run function to start the coffee run
coffee_run()
