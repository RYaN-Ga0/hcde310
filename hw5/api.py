import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display,image_id"


def get_artworks(artist):
    params = {"q": artist, "fields": FIELDS, "limit": 10}
    headers = {"User-Agent": "hcde310-artist-search/1.0"}
    response = requests.get(URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json().get("data", [])[:10]
