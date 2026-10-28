# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,artwork_type_title"

def count_by_artist(artworks):
    """Takes a list of artworks, returns a dictionary of artist names and their work counts."""
    counts = {}
    for artwork in artworks:
        artist = artwork.get("artist_title") or "Unknown"
        counts[artist] = counts.get(artist, 0) + 1
    return counts

def save_results(artworks, filename):
    """Save artwork titles, artists, and dates to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown"
            date = artwork.get("date_display") or "Unknown date"
            file.write(f"{title} | {artist} | {date}\n")


term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"
params = {
    "q": term,
    "fields": FIELDS
}

response = requests.get(
    url,
    params=params,
    headers={"AIC-User-Agent": "HCDE310 student project"}
)

if response.status_code != 200:
    print(f"Error: {response.status_code} {response.reason}")
    exit()

data = response.json()

artworks = data["data"]

if not artworks:
    print("No artworks found.")
else:
    for artwork in artworks:
        title = artwork.get("title") or "Unknown title"
        artist = artwork.get("artist_title") or "Unknown artist"
        artist_display = artwork.get("artist_display") or "Unknown"
        date = artwork.get("date_display") or "Unknown date"
        artwork_type = artwork.get("artwork_type_title") or "Unknown artwork type"

        print(f"Title: {title}")
        print(f"Artist: {artist}")
        print(f"Artist information: {artist_display}")
        print(f"Date: {date}")
        print(f"Artwork type: {artwork_type}")
        print()
print("Counts by artist:")
print(count_by_artist(artworks))
filename = "search_results.txt"
save_results(artworks, filename)
print(f"Results saved to {filename}")