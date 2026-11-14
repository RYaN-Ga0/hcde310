# HW5 findings

## 1. Drawing: one search for "Monet"
![Application flow diagram](flow_diagram.jpg)

## 2. Two questions about the code
In app.py, what does request.values.get("artist") do? Why is .strip() used after getting the artist name?

request.values.get("artist") retrieves the value entered in the artist search field from the request. request.values can access values from both GET and POST requests. .strip() removes whitespace from the beginning and end of the input, so extra spaces do not affect the search.

In api.py, what does response.json().get("data", [])[:10] do? Why do we use [:10] at the end?

response.json() converts the API response into a Python dictionary. .get("data", []) retrieves the artwork list from the "data" field, or returns an empty list if the field is missing. [:10] limits the results to the first 10 artworks.

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
|---|---|---|
| 1 | Home page displays the artist search form (pytest) | Pass |
| 2 | Empty search displays an error message (pytest) | Pass |
| 3 | Searching for Monet displays artwork information using mocked data (pytest) | Pass |
| 4 | Empty API results display "No results found." using mocked data (pytest) | Pass |
| 5 | Searching for Monet using the real API displays artwork results (manual) | [Pending] |
| 6 | Searching for a made-up artist name displays no results (manual) | [Pending] |

## 4. AI review
I asked Claude to review app.py and api.py for bugs, missing error handling, accessibility, and security problems.

What AI found that I had not noticed:

The API search uses a general q parameter instead of explicitly restricting the search to the artist field (api.py, line 8).

The app displays raw exception details to users (app.py, line 21).

Debug mode is enabled (app.py, line 26).

The API response is assumed to contain a usable data list (api.py, line 12).

What AI got wrong or needed to qualify:

The AI review could have overstated the missing error handling and accessibility issues. The API request already uses a timeout and raise_for_status(), and the Flask route catches exceptions. The HTML also includes a label for the search input and alt text for images.

Answers to my questions:

request.values.get("artist") retrieves the artist name submitted through the GET or POST request. .strip() removes extra whitespace from both ends of the input.

response.json() converts the API response into a Python dictionary. .get("data", []) retrieves the artwork list or an empty list if the key is missing. [:10] limits the returned list to the first ten artworks.

## 5. My fix
**Problem:** The app displayed the raw exception message to users when an API request failed. This could expose technical details that users do not need to see.

**Change:** I changed the exception handler in `app.py`. Instead of displaying the original exception, the app now shows a general error message: "Sorry, something went wrong. Please try again later."

**How I checked it:** I added `test_api_error_shows_generic_message()` to `test_app.py`. The test checks that the general error message appears and that the internal exception message is not displayed. All five pytest tests passed.

**Before fix commit:** `c5718ca`

**After fix commit:** `d940e84`

## 6. Can we ship it? (100–150 words)
I would not ship this app tomorrow. Although the basic artist search works, it still needs more testing and improvements before being ready for users. For example, the search may return irrelevant artworks for an artist name that does not exist. The app also needed better error handling because it originally displayed raw exception messages.

One thing my HW4 app does better is handling different error states, including API failures and missing artwork information, with clearer fallback messages.

One thing the AI-generated app does better is its simpler structure. It has fewer lines of code and is relatively easy to read and understand as a beginner.
