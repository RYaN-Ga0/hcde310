# HW4 Check: Art Explorer

## Test 1: Search for Matching Artworks

**Purpose:** Check whether searching for an artist returns relevant artworks.

**Method:** Enter `Monet` in the search form and click Search.

**Expected Output:** The results page displays artworks related to Claude Monet, including titles such as *Water Lilies*, along with available artist, date, and artwork type information.

**Actual Output:** The page displayed relevant artworks by Claude Monet, including *Water Lilies* and *Arrival of the Normandy Train, Gare Saint-Lazare*.

**Status:** Pass

---

## Test 2: Search for a Term with No Matches

**Purpose:** Check whether the app correctly handles searches that return no matching artworks.

**Method:** Search for `xyzqwerty987654` in the browser.

**Expected Output:** The page displays a helpful no-results message instead of unrelated artworks.

**First Attempt — Fail:** The page displayed 10 unrelated artworks instead of a no-results message.

**My Hypothesis:** I suspected that the API request was not applying the search term correctly. The API might have been returning a general list of artworks rather than filtering them by the user's query.

**AI Tutoring and Changes:** I used AI as a tutor to help me inspect the API request and understand why the search results were incorrect. Through this process, I identified that the request needed to send the search query in the correct format. I changed the API request to use a POST request with an explicit `multi_match` query that searches the artwork title and artist information.

**Second Attempt — Pass:** After the change, searching for `xyzqwerty987654` returned no matching artworks, and the page displayed the no-results message as expected.

**Final Status:** Pass (after debugging)

---

## Test 3: API Request Failure

**Purpose:** Check whether the app displays a helpful error message when the API request fails.

**Method:** Temporarily set `artworks = None` in the results route to simulate an API failure, then search for `Monet` in the browser.

**Expected Output:** The results page displays an API error message instead of artwork results or a no-results message.

**Actual Output:** The page displayed `Sorry, the artwork search failed. Please try again.` The page did not display the no-results message, and the Back to Search link remained available.

**Status:** Pass

---

## Test 4: Missing Artwork Fields

**Purpose:** Check whether the results page handles artwork records with missing fields.

**Method:** Temporarily replaced the API results with a test record containing `None` for the title, artist, date, and artwork type.

**Expected Output:** The page displays fallback text instead of `None` and loads without errors.

**Actual Output:** The page displayed `Untitled artwork`, `Unknown artist`, `Unknown date`, and `Unknown type`. The page loaded correctly without errors.

**Status:** Pass