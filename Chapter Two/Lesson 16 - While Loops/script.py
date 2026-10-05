count = 1

# while count <= 5:
#     print(count)
#     count += 1

# while count <= 5:
#     if count == 3:
#         break
#     print(count)
#     count += 1

# TOTAL_LAPS = 5
# lap = 1

# while lap <= TOTAL_LAPS:
#         print(f"Lap: {lap}")
#         lap += 1

# Challenge: Boarding Passes
# You're building an airport app that prints a boarding pass for each
# passenger on a group booking.

PASSENGERS = 5
passenger_num = 1

# Write a while loop that prints one line per passenger, like this:
while passenger_num <= PASSENGERS:
    # "Printing boarding pass 1 of 5..."
    # "Printing boarding pass 2 of 5..."
    # ...and so on until the last passenger.
    print(f"Printing boarding pass {passenger_num} of {PASSENGERS}...")    
    passenger_num += 1