# Challenge: Update the Excuse Generator to accept user input.

# Right now all the variables are hardcoded. Let's fix that.
# 1. Replace each variable's value with an input() prompt.
# 2. Print and test – make sure your output still looks like this:
#    "Sorry [Ted], I can't go to [the movies] – I have [345] [bees] to [crochet]
#    and honestly it's taking longer than expected."

# 1. Replace each variable's value with an input() prompt
first_name = input("Enter a name: ")
event = input("Enter an event (e.g., the movies): ")
number = input("Enter a number: ")
noun = input("Enter a plural noun (e.g., bees): ")
verb = input("Enter a verb (e.g., crochet): ")

# 2. Construct the f-string using the user inputs
excuse = f"Sorry {first_name}, I can't go to {event} - I have {number} {noun} to {verb} and honestly it's taking longer than expected."

# 3. Print and test the output
print("\n" + excuse)


# On the terminal, the program will now prompt the user for input, and the output will reflect the user's responses.
#Type the following command in the terminal to run the program:
# python excuse_generator.py