# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

# 1. Print titles of works made after 1900
for i in range(len(titles)):
    if years[i] > cutoff:
        print(titles[i])

# 2. Print whether each work is old or modern
print()
for i in range(len(titles)):
    if years[i] < cutoff:
        print(f"{titles[i]}: old")
    else:
        print(f"{titles[i]}: modern")

# 3. Count old and modern works
old_count = 0
modern_count = 0

for i in range(len(titles)):
    if years[i] < cutoff:
        old_count += 1
    else:
        modern_count += 1

print()
print(f"Old: {old_count}")
print(f"Modern: {modern_count}")
