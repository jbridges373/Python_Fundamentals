# import math

# # 1. Ensure your previous function actually RETURNS the value
# def get_slices():
#     # Example calculation or input
#     total_slices = 16 
#     return total_slices  #  Make sure this 'return' is present!

# def pizzas_needed(slices):
#     return math.ceil(slices / 8)

# # 2. Get the slices (now properly returned)
# slices = get_slices()

# # 3. Calculate pizzas (this will now work perfectly)
# pizzas = pizzas_needed(slices)
# print(f"Pizzas needed: {pizzas}")


# Challenge: Returning functions
# For each function, save the result to a variable, then use the result to print an f string.


# 1. Write room_area(length, width) that returns the area of a room. Get the area of a
#    12 by 10 room.
#    Example output:
#    The room is 120 square feet.


# 2. Write add_tax(price) that returns a price with 8% tax added (multiply by 1.08). Get
#    the total for a $50 item.
#    Example output:
#    With tax, that comes to $54.0.


# 3. Write full_name(first, last) that returns a first and last name joined with a space.
#    Use it to build a name, then print a greeting with it.
#    Example output:
#    Welcome, Mike Reed!


def room_area(length, width):
    return length * width

area = room_area(12, 10)
print(f"The room is {area} square feet.")

def add_tax(price):
    return price * 1.08

total_price = add_tax(50)
print(f"With tax, that comes to ${total_price:.2f}.")

def full_name(first, last):
    return f"{first} {last}"

my_name = full_name("Mike", "Reed")
print(f"Welcome, {my_name}!")

