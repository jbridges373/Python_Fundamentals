# BINGO!
# bingo_numbers = ["B-7", "I-16", "N-31", "G-46", "O-61", "B-2", "I-20", "N-34", "G-50", "O-65"]
# already_called = ["B-7", "I-16", "N-31"]

# print("B-7" in already_called)  # True
# print("G-46" in already_called)  # False

# import random

# pick = random.choice(bingo_numbers)

# while pick in already_called:
#     pick = random.choice(bingo_numbers)

# print(f"New call: {pick}")
# already_called.append(pick)
# print(f"Already called: {already_called}")


# Challenge: Raffle Drawing
# Build a feature that manages a charity raffle. The program picks a random winner but
# makes sure nobody wins twice. If the random winner has already won a prize, keep
# drawing a random winner until you land on someone new.
# 1. Draw a random name from entrants.
# 2. If that name is already in winners, keep drawing until you get one
#    that isn't.
# 3. Add the new winner to winners and print: "Winner: <name>"

import random

entrants = ["Alice", "Bob", "Charlie", "David", "Eva"]
winners = ["Alice", "Eva"] # Alice and Eva have already won

# 1. Start a loop that keeps drawing a random name from entrants
while True:
    winner = random.choice(entrants)

    # 2. If that name is NOT already in winners, we found our new winner!
    if winner not in winners:
        break # Stop drawing

# 3. Add the new winner to winners and print the result
winners.append(winner)
print(f"Winner: {winner}")
print(f"Winners list: {winners}")