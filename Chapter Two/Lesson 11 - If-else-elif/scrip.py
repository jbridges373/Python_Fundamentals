# test_score = 59

# if test_score >= 90:
#     print("You got an A!")
# elif test_score >= 80:
#     print("You got a B!")
# elif test_score >= 70:
#     print("You got a C!")
# elif test_score >= 60:
#     print("You got a D!")
# else:
#     print("You got an F!")

# Challenge: Wi-Fi Signal
# You're building a feature for a coffee shop that has spotty wi-fi. The feature should give
# customers a discount based on how many signal bars they're getting.
# Write an if/elif/else chain that prints a message for the customer's discount:
#   0 bars: "50% off, sorry about the Wi-Fi!"
#   1 or 2 bars: "25% off"
#   3 or 4 bars: "10% off"
#   5 bars: "Full bars, no discount today!"

# Prompt the user to enter the number of signal bars
bars = int(input("Enter the number of Wi-Fi signal bars (0-5): "))

# Determine the discount using an if/elif/else chain
if bars == 0:
    print("50% off, sorry about the Wi-Fi!")
elif bars == 1 or bars == 2:
    print("25% off")
elif bars == 3 or bars == 4:
    print("10% off")
elif bars == 5:
    print("Full bars, no discount today!")
else:
    print("Invalid input. Please enter a number between 0 and 5.")