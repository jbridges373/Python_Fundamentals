# guests = [("Alice", "lasagna"), ("Bob", "pizza"), ("Charlie", "burgers"), ("David", "pasta"), ("Eve", "salad")]

# for guest, food in guests:
#     print(f"Hello, {guest}! Welcome to the party. I hope you enjoy the {food}.")

# Challenge: Festival Lineup
# Each act in this festival lineup is a tuple: the band, their genre, and how many
# minutes they play.

lineup = [
    ("The Wailers", "reggae", 45),
    ("Daft Punk", "electronic", 90),
    ("Adele", "pop", 60),
    ("Metallica", "metal", 100),
]

# Loop over the lineup, unpacking each act into band, genre, and minutes. Use if/else to
# print a "long set" line for any act playing 90 minutes or more, and a normal line for
# the rest:
#
#   The Wailers (reggae) plays 45 minutes
#   Daft Punk (electronic) plays a long set: 90 minutes
#   Adele (pop) plays 60 minutes
#   Metallica (metal) plays a long set: 100 minutes

for band, genre, minutes in lineup:
    if minutes >= 90:
        print(f"{band} ({genre}) plays a long set: {minutes} minutes")
    else:
        print(f"{band} ({genre}) plays {minutes} minutes")