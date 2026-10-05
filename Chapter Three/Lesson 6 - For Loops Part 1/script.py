# guests = ["Alice", "Bob", "Charlie", "David", "Eve"]

# for guest in guests:
#     print(f"Hello, {guest}! Welcome to the party.")

# print("All guests have been greeted.")


# Challenge: Award Night!
# It's awards night, and here are the nominees for Best New App. The list can grow or
# shrink year to year, so your program shouldn't care how many names are on it.

nominees = ["PixelPal", "TaskTanic", "SnackMap", "MoodTunes"]

# 1. Loop over the nominees and print each one on its own line, formatted like the
#    example below so it reads like a real program.
#    Each line should look like:
#    Nominated for Best New App: PixelPal

# 2. After the loop, print one closing line: "And those are your nominees!"
#    It should print just once, after all the names.

for nominee in nominees:
    print(f"Nominated for Best New App: {nominee}")

print("And those are your nominees!")