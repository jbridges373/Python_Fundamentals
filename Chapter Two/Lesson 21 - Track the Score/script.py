# Challenge: Track the Score
# Tell the player their score and how they did!
# 1. Before the loop, set up a 'score' variable to count correct guesses. Initialize to 0.
# 2. Each time the player guesses correctly, increment the score by one.
# 3. Once the game ends, show a final score out of the total rounds. Example: "Final score: 3/5"
# 4. Use an if/elif/else chain to give fun feedback based on their score. Here's an example output,
# but feel free to write your own:
#    A score of 5: "Flawless! All tests passing, zero bugs."
#    A score of 4: "Near perfect, only one failing test!"
#    A score of 3: "Good effort! The code runs, and that's what counts."
#    A score under 3: "Have you tried turning it off and on again?"




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

print("=" * 60)
print()
print("Welcome to the Word Scramble Game!")
print()
print("You will be given a scrambled word and a hint. Try to guess the word!, or 'quit' at any time to exit the game. \n")
print("=" * 60)

# Initialize the round counter
round_num = 1
used = [] # List to track already used (word, hint) pairs
score = 0 # Initialize score variable to count correct guesses

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
            score += 1 # Increment score for correct guess
        else:
            print(f"❌ Sorry, the word was '{word}'.")
    elif player_guess == word:
        print("✅ Correct!")
        score += 1 # Increment score for correct guess
    else:
        print(f"❌ Sorry, the word was '{word}'.")

    # Increment the round counter
    round_num += 1

# Check if the player successfully completed all rounds
if round_num > 5:
    print("\nCongratulations! You've completed all 5 rounds of the game!")

# Once the game ends, show a final score out of the total rounds
print()
print("=" * 60)
print()
print(f"Final score: {score}/{round_num - 1}")  # Subtract 1 because round_num was incremented after the last round

# Use an if/elif/else chain to give fun feedback based on their score
if score == 5:
    print("Feedback: Flawless! All tests passing, zero bugs.")
elif score == 4:
    print("Feedback: Near perfect, only one failing test!")
elif score == 3:
    print("Feedback: Good effort! The code runs, and that's what counts.")
else:
    print("Feedback: Have you tried turning it off and on again?")
print()
print("=" * 60)
print()



