# api.py: will call Open Library for books by an author.
# SKELETON: get_books() returns fake data for now, so the whole path works before the API does.
import requests

URL = "https://openlibrary.org/search.json"

# Fake data, same shape as the real API's "docs" list.
# One variable per case, so you can check how your page handles each one.
FAKE_BOOKS = [
    {"title": "Fake Book One", "first_publish_year": 2001},
    {"title": "Fake Book Two", "first_publish_year": 2002},
    {"title": "Fake Book Three", "first_publish_year": 2003},
]

FAKE_EMPTY = []                                           # no results

FAKE_MISSING_FIELDS = [
    {"title": "Fake Book One", "first_publish_year": 2001},
    {"title": "Fake Book Two"},                           # no year
    {"title": None, "first_publish_year": 2003},          # title is there, but null
    {"first_publish_year": 2004},                         # no title at all
]

FAKE_ERROR = None                                         # what get_books_real() returns when the call fails

# Change this line to try a different case
FAKE_DATA = FAKE_BOOKS


def get_books(author):
    # Fake for now. When the path works, switch app.py to get_books_real().
    return FAKE_DATA


# ---- Next step: the real call ----
# try/except (Class 10) is OPTIONAL for HW4: a status code check is enough.
# It catches the case where the API never answers: no wifi, wrong domain, too slow.
def get_books_real(author):
    try:
        # timeout=10: stop waiting after 10 seconds instead of hanging forever
        r = requests.get(URL, params={"author": author}, timeout=10,
                         headers={"User-Agent": "HCDE310 books app"})
    except requests.RequestException:
        # No answer at all. There's no status code to check, so return None
        print("API error: no answer")     # for you, in the terminal
        return None

    if r.status_code != 200:
        # The API answered, and the answer was "no" (404, 500...)
        print("API error:", r.status_code, r.reason)
        return None

    return r.json()["docs"][:10]          # [:10] = the first 10 books
