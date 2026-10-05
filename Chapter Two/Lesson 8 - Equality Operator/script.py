password = "SECRET"

# user_password = input("Enter the password: ")

# if user_password == password:
#     print("Password correct!")
# else:
#     print("Incorrect password.")

# Challenge: Discount Code
# You're building a promo code checker for an online shop, so a shopper
# can enter a code and find out whether it unlocks the flash sale discount.


promo_code = "FLASH50"

# 1. Prompt the user to enter a promo code. Hint: use an input() prompt.
user_input = input("Enter the promo code: ")

# 2. Print whether the user's input is equal to promo_code.
print("Is it equal?", user_input == promo_code)

# 3. Print whether the user's input is NOT equal to promo_code.
print("Is it not equal?", user_input != promo_code)

# 4. Enter both "FLASH50" and "flash50" as a prompt. Notice that because == is case-sensitive, the
#    results will flip.