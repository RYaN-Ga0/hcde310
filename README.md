# HW3: First Live API Call

Run everything from inside this folder (`cd hw3`). Before you start: install `requests` in your venv (see Class 5).

| File | Part |
|---|---|
| `sample_response.json` | 1: a saved Art Institute search to read (don't edit) |
| `notes.md` | 1: your answers and your first prediction |
| `fetch.py` | 2, 3 and 4: your code |
| `check.py` | 2, 3 and 4: run `python3 check.py` to check your work (it pretends to be the museum's API) |
| `ai_log.md` | 4: your log for `save_results` |

<!-- Instructions below = the HW3 assignment on Canvas. -->

**Due:** Mon Oct 26, 10am  **AI:** Stage 2 and Stage 3  **Individual**

Your first **live** API call. The starter (`hw3.zip`) has `fetch.py` with most of the `requests` code; you fill in the URL, parameters, and loop.

Write Parts 1–3 **yourself** (you can still ask the tutor, as in HW2).

## Part 1 – Read the response first
AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:
1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
2. Find 3 more fields you'd want to show a user, and their paths
3. Which fields are `null` for some works?
4. **Predict:** open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?
5. **Run it:** run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of **your** file caused it?

## Part 2 – Call it live
AI Use: Stage 2 (Tutor)

In `fetch.py` (run it again after each step):
1. Ask the user for a search term with `input()`
2. Call `https://api.artic.edu/api/v1/artworks/search` with `q=<term>` and `fields=id,title,artist_title,artist_display,date_display`
3. **Check `status_code`** before using the data. If it isn't 200, print a friendly message that includes the code and the reason (`response.reason`), e.g. `500 Internal Server Error`.
4. Loop over the results and print them using **your HW2 printing code** (reuse it!). Also print the **3 fields you picked in Part 1** (add them to `FIELDS`). For the fields you found are `null` in Part 1, print a default (like "Unknown artist") instead of `None`.
5. Handle "no results" with a helpful message
6. **Run it three ways:** a normal search, `12345678901234` (no results), and a misspelled URL (error). All three should print a message, not a traceback. Then fix the URL again.
7. **Run `python3 check.py`** until it passes. It pretends to be the museum's API, so it gives the same answer every time.

## Part 3 – Count by artist
AI Use: Stage 2 (Tutor)

Bring your `count_by_artist` function from HW2 into `fetch.py`, and print the counts after the results.
- The API's field names aren't the same as HW2's. What does the function need to look up now?
- Where does the call go? Check: the counts show up when you search, and nothing breaks when there are no results or an error. `check.py` tests this too.

## Part 4 – Save the results
AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

1. **Try:** paste your own attempt or plan for the function, even if it doesn't work
2. **Chat (AI only):** paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."
3. **Predict, then compare:** before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)
4. **What surprised me:** one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."
5. **Change one thing yourself:** once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.

Done early? Add `sort_by_date(artworks)` too (not graded).

## Rubric (30 pts)

| Row | Pts |
|---|---|
| JSON paths correct; null fields identified | 5 |
| Live call works; status, no results and errors handled; `check.py` passes | 8 |
| `count_by_artist` reused, fixed for the API's fields, called in the right place | 3 |
| `save_results` works; results file from a real search committed | 4 |
| `ai_log.md`: attempt, chat, prediction vs. actual, what surprised you, your change | 10 |

## Relevant reading

- *Python for Everybody* [Ch 13 Using Web Services](https://www.py4e.com/html3/13-web): JSON, APIs, and API keys. (Optional background: [Ch 12 Networked Programs](https://www.py4e.com/html3/12-network).) Note: py4e uses `urllib`; we use `requests`, which does the same job with less code.
- [Requests Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/): making a request, query parameters, `status_code`, and `.json()`.
- *Composing Programs* has no chapter on web data yet. The nested-list examples in [2.2 Sequences](https://composingprograms.com/3ed/sequences/#lists) (`pairs[1][0]`) are good practice for reading JSON paths like `data["data"][0]["title"]`.

## Course objectives we cover

| # | Objective |
|---|---|
| 4 | Use or incorporate external resources (e.g., third party software libraries or APIs) into the designed systems. |
| 5 | Apply basic computational thinking concepts and practices, including reading, debugging, and testing code. |
| 8 | Use AI tools deliberately: verify their output, and explain what you built and what the AI did. |
