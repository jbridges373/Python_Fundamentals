#468284
# steel_blue = (70, 130, 180)

#unpacking
# red, green, blue = steel_blue
# print(red)
# print(green)
# print(blue)

# colour_palette = [
#     (70, 130, 180),
#     (240, 128, 128),
#     (60, 179, 113),
# ]

# red, green, blue = colour_palette[0]
# print(f"RGB: {red}, {green}, {blue}")

# red, green, blue = colour_palette[1]
# print(f"RGB: {red}, {green}, {blue}")

# Challenge: Inventory Check
# Build an inventory display feature for a small office supply store.
# 1. Unpack the item and quantity for each entry in the list of tuples.
# 2. Print each item and it's quantity in this format: "notebooks: 42 in stock"

inventory = [
    ("notebooks", 42),
    ("pens", 18),
    ("post-it notes", 24)
]

for item, quantity in inventory:
    print(f"{item}: {quantity} in stock")