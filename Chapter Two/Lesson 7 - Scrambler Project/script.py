import random

words = ["apple", "orange", "banana"]

word = random.choice(words)
print(word)

letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters)

print(f"Scrambled: {scrambled_word}")
