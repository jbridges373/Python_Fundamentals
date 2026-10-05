# Challenge: Add a Game Loop
# Right now the game ends after a single word. Add the ability to play multiple rounds and quit out
# of the game at any point.

# 1. Wrap the game code in a loop that runs for 5 rounds.
# 2. Display the round number at the beginning of each round.
# 3. Give the player a way to quit early by typing 'quit'.
#    * Hint: you'll want to break out of the loop when they do.



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

print("Welcome to the Word Scramble Game!")
print()
print("You will be given a scrambled word and a hint. Try to guess the word!, or 'quit' at any time to exit the game. \n")

# Initialize the round counter
round_num = 1

# 1. Wrap the game code in a loop that runs for 5 rounds
while round_num <= 5: # Loop for 5 rounds
    # 2. Display the round number at the beginning of each round
    print()
    print(f"--- Round {round_num} of 5 ---")
    print()

    # Pick and scramble a word
    word, hint = random.choice(word_bank)
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


