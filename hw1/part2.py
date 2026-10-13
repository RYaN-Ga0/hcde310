# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles

# 1. Print every title with a number
for i, title in enumerate(titles, start=1):
    print(f"{i}. {title}")

# 2. Print how many titles there are
print(f"Titles: {len(titles)}")

# 3. Count titles containing "a" or "A"
count = 0
for title in titles:
    if "a" in title.lower():
        count += 1

print(f'Titles with an "a": {count}')

# 4. Find the longest title
longest = ""
for title in titles:
    if len(title) > len(longest):
        longest = title

print(f"Longest: {longest}")