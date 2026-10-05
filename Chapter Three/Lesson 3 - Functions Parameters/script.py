# shop_name = "Starbucks"

# def show_welcome():
#     print(f"Welcome to {shop_name}!")

# show_welcome()

# def greet(name, unread_messages):
#     print(f"Hello, {name}! You have {unread_messages} new messages.")

# greet("Alice", 5)
# greet("Bob", 3)
# greet("Charlie", 7)

# Challenge: Write two functions with parameters
# Write each function underneath its instructions, then call it with the values given.


# 1. Write a function called add_numbers that prints the sum of the two numbers you pass in.
#    Call it a couple of times with different numbers.
#    Example output:
#    add_numbers(2, 3) prints 5
#    add_numbers(10, 45) prints 55


# 2. You've scrambled a word before: turn it into a list of letters, shuffle them, and
#    join them back together. Let's make that reusable. Write scramble(word) so it takes
#    any word and prints a scrambled version of it.
#    Example output:
#    scramble("python") might print nohtyp

import random

def add_numbers(num1, num2):
    sum_result = num1 + num2
    print(sum_result)

add_numbers(2, 3)
add_numbers(10, 45)

def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    scrambled = ''.join(letters)
    print(scrambled)

scramble("python")