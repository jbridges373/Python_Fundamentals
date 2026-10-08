# try:
#     age = int(input("How old are you? "))
#     print(f"You'll be {age + 1} next year!")
# except ValueError:
#     print("Please enter a number!")


# Challenge: Hot Dog Contest
# You're building a signup for a hot dog eating contest. Entrants type how many
# hot dogs they think they can eat, but nothing stops them from typing something
# that isn't a number.

# 1. Ask the entrant how many hot dogs they can eat and convert the answer to an int.

# 2. If the answer isn't a whole number, print "I need a number to sign you up."

# 3. If the answer is a whole number, print "Signed up for {count} hot dogs. Good luck!"

# Here's what your output should look like:
#
# How many hot dogs can you eat? 7
# Signed up for 7 hot dogs. Good luck!
#
# How many hot dogs can you eat? a lot
# I need a number to sign you up.

# Challenge: Hot Dog Contest (Using a try/except block)

user_input = input("How many hot dogs can you eat? ").strip()

try:
    # Attempt to convert the answer to an int
    count = int(user_input)
    # If successful, print the confirmation message
    print(f"Signed up for {count} hot dogs. Good luck!")
except ValueError:
    # If int() fails because it isn't a whole number, catch the error here
    print("I need a number to sign you up.")
