# age = 16
# is_adult = age >= 18
# print("Is the person an adult?", is_adult)

# Challenge: Comparison Checks
# Apps often compare numbers to decide what to show a user. Using the
# values below, use comparison operators inside f-strings to print a labeled
# result for each check. Your output should look like this:
#   Has unread messages (more than 0): False
#   Old enough to rent a car (25 or older): True
#   Under the $50 free-shipping minimum: True
#   Sold out (0 or fewer tickets left): False

unread_messages = 0
age = 25
cart_total = 45
tickets_left = 6

# Use comparison operators inside the f-string curly braces
print(f"Has unread messages (more than 0): {unread_messages > 0}")
print(f"Old enough to rent a car (25 or older): {age >= 25}")
print(f"Under the $50 free-shipping minimum: {cart_total < 50}")
print(f"Sold out (0 or fewer tickets left): {tickets_left <= 0}")
