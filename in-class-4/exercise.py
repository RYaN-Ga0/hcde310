# Class 4 in-class exercise: read tracebacks (pairs, AI: Tutor for one snippet)
# Each snippet below has a bug. Don't run this yet: write your predictions in predictions.md first.
# Then run it:  python3 exercise.py      Check it:  python3 check.py
# Python stops at the first error, so fix one bug, run again, and see the next one.

# Snippet 1
exhibit = {"title": "Water Lilies", "room": 243, "year": 1906}
print("Find it in room " + exhibit["Room"])

# Snippet 2
exhibit = {"title": "Water Lilies", "room": 243, "year": 1906}
print("Find it in room " + exhibit["room"])

# Snippet 3
exhibits = ["Water Lilies", "Nighthawks", "The Bedroom"]
for i in range(len(exhibits) + 1):
    print(i + 1, exhibits[i])

# Snippet 4
def count_visits(visits, room):
    """Return how many visits went to one room."""
    total = 0
    for v in visits:
        if v == room:
            total = total + 1
    return total

visits = [243, 101, 243, 262, 243]
print(count_visits(visit, 243))

# Snippet 5
def longest_title(titles):
    """Return the longest title in a list of titles."""
    longest = ""
    for t in titles:
        if len(t) > len(longest):
            longest = t
    print(longest)

title = longest_title(["Nighthawks", "The Bedroom", "Water Lilies"])
print(title.upper())
