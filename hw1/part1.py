# HW1 Part 1: Strings
# Run it:  python3 part1.py
# Your output must match expected/part1.txt exactly.

# 1.Store the title, artist, and year
title = "The Bedroom"
artist = "Vincent van Gogh"
year = 1889

# 2.Print the artwork information
print(f"{title} ({year}) by {artist}")

# 3. Print the title in uppercase and its length
print(title.upper(), len(title))

# 4.Check whether the title contains "Bed"
print("Bed" in title)
