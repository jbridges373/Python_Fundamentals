# recipe = "chicken tikka masala"
# header = recipe.upper()

# search = "PASTA CARBONARA"
# print(search.lower())

# chef = "grace smith"
# print(chef.title())

# print("50%".strip("%"))  # Output: 50

# recipe = "      chicken korma"
# print(recipe.strip())  # Output: "chicken korma"

# raw = "       CHinkEn TIKKA MasALA    "
# query = raw.strip().lower()
# print(query)  # Output: "chinken tikka masala"

# Challenge: Data Cleanup
# You're building a sign-up form that tidies up whatever users type in.
# Each value below comes in messy. Figure out which string method (or
# methods) gets it to the clean version, then print the result. Some need
# just one method, and some need two chained together:
# 1. promo_code   "spring25"           -> "SPRING25"
# 2. full_name    "jamie rivera"       -> "Jamie Rivera"
# 3. email        " Jamie@Example.COM" -> "jamie@example.com"
# 4. display_name "  the ROCK  "       -> "The Rock"

# 1. Convert to uppercase
promo_code = "spring25"
clean_promo = promo_code.upper()
print(f"Promo Code:   '{clean_promo}'")

# 2. Capitalize the first letter of each word
full_name = "jamie rivera"
clean_name = full_name.title()
print(f"Full Name:    '{clean_name}'")

# 3. Strip whitespace and convert to lowercase (chained)
email = " Jamie@Example.COM"
clean_email = email.strip().lower()
print(f"Email:        '{clean_email}'")

# 4. Strip whitespace and convert to title case (chained)
display_name = "  the ROCK  "
clean_display = display_name.strip().title()
print(f"Display Name: '{clean_display}'")
