# Challenge: Avoid Repeating Words
# Ensure that a word shows up no more than once per game.
# 1. Outside the game loop, make an empty list called `used` to track already used (word, hint)
# pairs.
# 2. Inside the game loop, write another loop that checks if the picked (word, hint) pair is
# already in `used`, and keeps re-picking until it finds an unused word.
# 3. Once a fresh pair is found, append it to `used` so it won't come up again.
# 4. Test your game to make sure it plays five unique words.



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

used = [] # List to track already used (word, hint) pairs

print("Welcome to the Word Scramble Game!")
print()
print("You will be given a scrambled word and a hint. Try to guess the word!, or 'quit' at any time to exit the game. \n")

# Initialize the round counter
round_num = 1

# Wrap the game code in a loop that runs for 5 rounds
while round_num <= 5: # Loop for 5 rounds
    # Display the round number at the beginning of each round
    print()
    print(f"--- Round {round_num} of 5 ---")
    print()

    while True:
        # Pick a random (word, hint) pair from the word bank
        word, hint = random.choice(word_bank)

        # Check if the picked (word, hint) pair is already in `used`
        if (word, hint) not in used:
            # If it's not used, break out of the loop
            break

    # Add the picked (word, hint) pair to the `used` list
    used.append((word, hint))

    # Pick and scramble a word
    letters = list(word) # Convert string to list of characters
    random.shuffle(letters)     # Rearrange the characters randomly

    # Display the scrambled word in all caps so it stands out
    scrambled_word = "".join(letters).upper() # Convert list back to string and make it uppercase
    print(f"SCRAMBLED WORD: {scrambled_word}\n") # Display the scrambled word to the player

    # Prompt the player for input
    player_input = input("Type a guess or type 'skip' to skip the word  or 'hint' to get a hint or 'quit' to quit the game: ")

    # Clean the player's guess so capitalization and whitespace don't matter
    player_guess = player_input.strip().lower() # Remove leading/trailing whitespace and convert to lowercase

     # Give the player a way to quit early by typing 'quit'
    if player_input == "quit":
        print("\nThanks for playing! Goodbye.")
        break  # Breaks out of the loop completely

    # Use if/elif/else to handle the three cases
    elif player_guess == "skip":
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

    # Increment the round counter
    round_num += 1

# Check if the player successfully completed all rounds
if round_num > 5:
    print("\nCongratulations! You've completed all 5 rounds of the game!")


