# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
The path to the first artwork's title is:

data["data"][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths
Artist: data["data"][0]["artist_title"]

Date: data["data"][0]["date_display"]

Artwork type: data["data"][0]["artwork_type_title"]

## 3. Which fields are `null` for some works?
The artist_title field is null for some artworks. For example, the artwork "Baroque Pearl Mounted as a Cat Holding a Mouse" has a null value for artist_title.

In Python, JSON null becomes None. I should handle this case by displaying a default value, such as "Unknown artist", instead of displaying None.

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
Before running the program, I noticed that `url` was an empty string (`""`). I predicted that the API request would fail because `requests.get()` needs a valid URL to send a request.

## 5. Run it
I ran fetch.py and entered cat as the search term. The program raised a traceback instead of displaying the search results.

The error occurred on line 16 of fetch.py:

response = requests.get(url, params=params)

The final exception was:

requests.exceptions.MissingSchema: Invalid URL '': No scheme supplied. Perhaps you meant https://?

The problem was that the url variable was an empty string (""). The program tried to send a request without a valid URL, so the request failed before it could retrieve any artwork data.
