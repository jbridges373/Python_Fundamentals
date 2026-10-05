# Challenge: Check if the Guess Is Correct
# Add interactivity so a player
# can either a) skip the word and get the correct answer or b) guess the word and find out if
# they're correct.

# 1. Prompt the player for input and give them two options: type a guess or type 'skip' to skip the
# word.
# 2. Use string methods to clean the player's guess and improve the display:
#   - We want to be as forgiving as we can with the player's guess. Clean the player's guess so
#     that capitalization and white space don't matter when comparing to the correct answer.
#   - Display the scrambled word in all caps so it stands out on screen.
# 3. Use if/elif/else to handle three cases:
#   - Player types "skip": Skipped! The word was 'apple'.
#   - Player's guess is correct: ✅ Correct!
#   - Player's guess is incorrect: ❌ Sorry, the word was 'apple'.


import random

# Setting up our target word and its scrambled version
words = ["python", "jargon", "scramble", "challenge", "programming"]
secret_word = random.choice(words)
char_list = list(secret_word) # Convert string to list of characters
random.shuffle(char_list)     # Rearrange the characters randomly

# 2. Display the scrambled word in all caps so it stands out
scrambled_word = "".join(char_list).upper() # Convert list back to string and make it uppercase
print(f"SCRAMBLED WORD: {scrambled_word}\n") # Display the scrambled word to the player

# 1. Prompt the player for input
player_input = input("Type a guess or type 'skip' to skip the word: ")

# 2. Clean the player's guess so capitalization and whitespace don't matter
cleaned_guess = player_input.strip().lower() # Remove leading/trailing whitespace and convert to lowercase

# 3. Use if/elif/else to handle the three cases
if cleaned_guess == "skip":
    print(f"Skipped! The word was '{secret_word}'.")
elif cleaned_guess == secret_word:
    print("✅ Correct!")
else:
    print(f"❌ Sorry, the word was '{secret_word}'.")


