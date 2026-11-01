# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
TypeError: 'builtin_function_or_method' object is not iterable


### 2. What I thought it meant
I thought max() could use counts.get to find the artist with the highest count.

### 3. What it actually meant
counts.get is a dictionary method, not a collection of values. I needed to tell Python to compare the dictionary keys using their corresponding counts.

### 4. The fix
I changed:

most_works_artist = max(counts.get)

to:

most_works_artist = max(counts, key=counts.get)

The key=counts.get argument tells Python to compare artists by their counts and return the artist with the largest count.
## Entry 2

### 1. Error message
KeyError: 'Vincent van Gogh'


### 2. What I thought it meant
I thought I could increase an artist's count directly using counts[artist] += 1.

### 3. What it actually meant
The dictionary was initially empty, so the artist's key did not exist when Python tried to increase its count.

### 4. The fix
I changed counts[artist] += 1 to counts[artist] = counts.get(artist, 0) + 1. This initializes a new artist's count at 1 and increases the count for artists who already exist in the dictionary.