# first_word = list("listen")
# second_word = list("silent")

# print(sorted(first_word))
# print(sorted(second_word))

# Challenge: Anagram Check
# Anagrams are two words made from the exact same letters rearranged,
# like "listen" and "silent".

# For each pair below, split both words into lists, sort them, and print
# the results. If the two lists match, the words are anagrams.

# 1. "earth" and "heart"
# 2. "below" and "elbow"
# 3. "night" and "tight"


# Function to check if two words are anagrams
def check_anagram(word1, word2):
    # Convert words to lists of characters and sort them
    list1 = sorted(list(word1))
    list2 = sorted(list(word2))
    
    # Check if the sorted lists are identical
    is_anagram = list1 == list2
    
    print(f"Checking '{word1}' and '{word2}':")
    print(f"  Sorted 1: {list1}")
    print(f"  Sorted 2: {list2}")
    print(f"  Are they anagrams? {is_anagram}\n")

# 1. "earth" and "heart"
check_anagram("earth", "heart")

# 2. "below" and "elbow"
check_anagram("below", "elbow")

# 3. "night" and "tight"
check_anagram("night", "tight")
