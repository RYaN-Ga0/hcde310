# Class 10 in-class exercise: States in a Flask app (AI: Stage 4, spec first)

Goal: take a working skeleton and make it handle the states, one at a time. This is a books app (Open Library), not your HW4 API: same thinking, different data.

The whole path already works with fake data: type an author, press Find books, see a page of fake books.

**Run it** (in this folder, with your venv on):

    pip install flask requests
    flask --app app run --debug

Open http://127.0.0.1:5000. Ctrl+C stops it.

## Steps

1. **Run it as is.** Search for anything and see the fake books.
2. **See the states break.** In `api.py`, change `FAKE_DATA = FAKE_BOOKS` to `FAKE_EMPTY`, then to `FAKE_MISSING_FIELDS`. What does the page show? Is that useful to a user?
3. **Fill in the states** in `/results` in `app.py` (the numbered comments), one at a time:
   - empty input (step 2)
   - API error (step 4): try it with `FAKE_DATA = FAKE_ERROR`
   - no results (step 5): try it with `FAKE_EMPTY`
   - missing fields: try it with `FAKE_MISSING_FIELDS`

   Each bad state goes back to `home.html` with a message. Add a `{% if message %}` block to `home.html` so the message shows. Write each message for the user: what should they do next?
4. **Switch to the real API.** In `app.py`, use `get_books_real` instead of `get_books`. Search "Ferrante", then a nonsense word. Break the URL in `api.py` on purpose to test your error message, then put it back. (`try/except` is already in `get_books_real`. It's optional for HW4: a status code check is enough.)
5. **Commit each time a state works.**

**Submit:** commit and push, then submit your **commit link** on Canvas **by midnight tonight**. Graded on completion.
