result = ", ".join(["peace", "love", "happiness"])
print(result)


# Challenge: Four Joiners

# 1. Join ["mysite.com", "products", "sale"] with "/" to build a URL path
url_parts = ["mysite.com", "products", "sale"]
url_path = "/".join(url_parts)
print(url_path)

# 2. Join ["2026", "05", "29"] with "-" to format a date
date_parts = ["2026", "05", "29"]
formatted_date = "-".join(date_parts)
print(formatted_date)

# 3. Join ["hip", "hip", "hooray"] with " " for the crowd
cheer_parts = ["hip", "hip", "hooray"]
cheer = " ".join(cheer_parts)
print(cheer)

# 4. Join `letters` into a single word with no separator.
letters = ["p", "y", "t", "h", "o", "n"]
word = "".join(letters)
print(word)
