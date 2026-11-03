import requests

URL = "https://api.artic.edu/api/v1/artworks/search"

FIELDS = "id,title,artist_title,artist_display,date_display,artwork_type_title"


def search_art(term):
    """Search artworks by title or artist information.

    Return a list of matching artworks, an empty list if no
    results are found, or None if the API request fails.
    """
    payload = {
        "query": {
            "multi_match": {
                "query": term,
                "fields": [
                    "title",
                    "artist_title",
                    "artist_display"
                ]
            }
        },
        "fields": FIELDS,
        "size": 10
    }

    try:
        response = requests.post(
            URL,
            json=payload,
            headers={
                "AIC-User-Agent": "HCDE310 student project"
            },
            timeout=10
        )
    except requests.RequestException as error:
        print("Request error:", error)
        return None

    print("Status:", response.status_code)

    if response.status_code != 200:
        print("Response:", response.text[:500])
        return None

    try:
        data = response.json()

        if not isinstance(data, dict):
            return None

        artworks = data.get("data")

        print("Pagination:", data.get("pagination"))
        print(
            "First titles:",
            [
                item.get("title")
                for item in artworks[:3]
                if isinstance(item, dict)
            ]
            if isinstance(artworks, list)
            else "Invalid data"
        )

        if not isinstance(artworks, list):
            return None

        return [
            artwork for artwork in artworks
            if isinstance(artwork, dict)
        ]

    except (ValueError, TypeError, AttributeError) as error:
        print("Response parsing error:", error)
        return None
