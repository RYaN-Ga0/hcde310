# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display"

# Functions go here (above the code that runs)


term = input("Search the Art Institute for: ")

url = ""      # TODO: the search URL from step 2
params = {}   # TODO: q (the search term) and fields (FIELDS)
response = requests.get(url, params=params)

# TODO step 3: check response.status_code before you use the data

data = response.json()

# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results
