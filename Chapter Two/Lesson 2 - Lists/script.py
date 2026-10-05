# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
# ratings = ["excellent", "good", "average", "poor", "terrible"]
# prices = [0.99, 1.49, 2.99, 3.49, 4.99, 5.99, 6.49, 7.99, 8.49, 9.99]
# scores = [[100, 200, 300], [400, 500, 600], [700, 800, 900, 1000]]
# mood = ["😊", "😒", "😍", "🤣"]

# print("Fruits List:", fruits)
# print("Ratings List:", ratings)
# print("Prices List:", prices)
# print("Scores List:", scores)
# print("Mood List:", mood)

# playlist = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5"]

# print("Playlist:", playlist[0:3])  # Print the first three songs in the playlist
# top_song = playlist[0]  # Get the top song in the playlist
# print(f"Now Playing: {top_song}")  # Print the top song

# Challenge: Build a Support Queue
# You're building a help desk feature that shows who's waiting
# in line for support.

# Use indexing to print a status display that looks like this:
#
#   Now helping: Ada
#   Next in line: Grace
#   Just added: Alan
#
# "Now helping" is the first person in line, "Next in line" is second, and "Just added" is the last
# person in the queue.

# 1. Define the queue list containing the names
queue = ["Ada", "Grace", "Alan"]

# 2. Use list indexing to print the status display
# [0] fetches the first item, [1] fetches the second, and [-1] fetches the last item
print(f"Now helping: {queue[0]}")
print(f"Next in line: {queue[1]}")
print(f"Just added: {queue[-1]}")  # Using -1 to get the last person in the queue