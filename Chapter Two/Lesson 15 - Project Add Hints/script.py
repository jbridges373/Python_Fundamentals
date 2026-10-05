# Challenge: Let the Player Ask for a Hint
# The word_bank below pairs each word with a hint. Wire up a 'hint' option
# so a stuck player can reveal the clue and then keep guessing.

# 1. Pick a random pair from word_bank and unpack it into word and hint.
# 2. Update the guess prompt so the player knows 'hint' is now an option.
# 3. If the player types 'hint', show them the hint, then ask them to guess again.
#    * Hint: this will require adding a second input prompt!
#    * Hint: keep the 'hint' check in its own separate if, above the
#      skip/correct/wrong block. Skip, correct, and wrong all end the turn,
#      but a hint doesn't. Keeping it separate lets the game show the hint
#      and then still check the guess the player types next.
# 4. Optional: add a couple of your own word/hint pairs to the bank.


import random

# Setting up our target word and its scrambled version
word_bank = [
    ("standup", "Every morning, our fifteen-minute ___ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ___ error."),
    ("debug", "I spent four hours trying to ___ my code. Turns out I was missing comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ___ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ___."),
    ("meeting", "That ninety-minute ___ could have been an email."),
    ("deadline", "Of course we'll hit the ___, no problem! Well, within a couple of days. Maybe a week."),
    ("backup", "We finally made a ___ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ___ is down again."),
    ("prototype", "It's just an early ___, so please ignore that clicking anywhere crashes it."),
]

word, hint = random.choice(word_bank)
letters = list(word) # Convert string to list of characters
random.shuffle(letters)     # Rearrange the characters randomly

# 2. Display the scrambled word in all caps so it stands out
scrambled_word = "".join(letters).upper() # Convert list back to string and make it uppercase
print(f"SCRAMBLED WORD: {scrambled_word}\n") # Display the scrambled word to the player

# 1. Prompt the player for input
player_input = input("Type a guess or type 'skip' to skip the word or 'hint' to get a hint: ")

# 2. Clean the player's guess so capitalization and whitespace don't matter
player_guess = player_input.strip().lower() # Remove leading/trailing whitespace and convert to lowercase

# 3. Use if/elif/else to handle the three cases
if player_guess == "skip":
    print(f"Skipped! The word was '{word}'.")
elif player_guess == "hint":
    print()
    print(f"Hint: {hint}")
    print()
    # Ask for another guess after showing the hint
    player_input = input("Type your guess: ")
    player_guess = player_input.strip().lower()
    if player_guess == word:
        print("✅ Correct!")
    else:
        print(f"❌ Sorry, the word was '{word}'.")
elif player_guess == word:
    print("✅ Correct!")
else:
    print(f"❌ Sorry, the word was '{word}'.")


