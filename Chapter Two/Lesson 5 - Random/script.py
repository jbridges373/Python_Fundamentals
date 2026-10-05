import random

# lunch_spots = [
#     "Subway",
#     "Pizza Hut",
#     "Burger King"
# ]

# def get_random_lunch_spot():
#     return random.choice(lunch_spots)
# print(get_random_lunch_spot())

# random.shuffle(lunch_spots)
# print(lunch_spots)

# print(sorted(lunch_spots))
# print(lunch_spots)

# Challenge: Turn Order
# You're building a feature for a board game app that sets up each match.
# At the start of a game, you need to put the players in a random turn
# order, and also randomly choose one player to deal the cards.

# 1. Shuffle the players into a random turn order, then print the list.
# 2. Randomly choose one player to be the dealer and print:
#    "<name> deals first"

# Example list of players
players = ["Alice", "Bob", "Charlie", "Diana"]

# 1. Shuffle the players into a random turn order, then print the list
# Note: random.shuffle() modifies the original list in place
random.shuffle(players)
print("Turn order:", players)

# 2. Randomly choose one player to be the dealer and print
dealer = random.choice(players)
print(f"{dealer} deals first")
