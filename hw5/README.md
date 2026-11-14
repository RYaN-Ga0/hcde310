# HW5: Break the AI's Code

Run everything from inside this folder (`cd hw5`). Before you start: in your venv, `pip install -r requirements.txt`. Run the app with `python3 app.py`, then open http://127.0.0.1:5000.

| File | What it is |
|---|---|
| `prompt.md` | the prompt Copilot got (read it first) |
| `app.py`, `api.py`, `templates/` | the app Copilot made, unchanged |
| `test_app.py` | one example `pytest` test; add yours here if you write tests |
| `findings.md` | everything you hand in, with headings to fill in |

<!-- Instructions below = the HW5 assignment on Canvas. -->

**Due:** Thu Nov 12, 10am  **AI:** Stage 4 – Spec first  **Individual**

## What you'll make

We give you a small Flask app: an artist search on the Art Institute of Chicago API, the same kind of app as your HW4. **Copilot built it in VS Code from the prompt in `prompt.md`, and we didn't change anything.** This is what you'd get if you asked it yourself. It mostly works.

You'll hand in one file, `findings.md` (the starter has the headings), plus your fixed code and `ai_use.md`.

**From HW4 you need:** your checks from `plan.md` and your HW4 app. You don't need to change your HW4.

## Steps

1. **Read and draw (no AI).** Read `prompt.md`, `app.py`, `api.py` and the two templates. Don't run anything yet. Then draw boxes and arrows for what happens when someone searches "Monet": the form → the route → the API call → the template → the page. Label each arrow with the variable that carries the data (for example `artist`, `artworks`). Add a photo to `findings.md`.
2. **2 questions.** Write 2 questions about code you don't understand (for example: what does `request.values` do? why is there a `methods=` list?).
3. **Checks.** Write at least 4 checks of what the app *should* do, based on `prompt.md` and your HW4 checks. **At least 2 must be `pytest` tests** in `test_app.py` (it has one example); the rest can be plain sentences ("search for nothing → see a message"). Run the app and the tests (`python3 -m pytest`), and write pass or fail next to each check. A failing check is a good find.
4. **AI review.** Now ask an AI to review the app. Paste in `app.py` and `api.py` and ask: *"Review this Flask app for bugs, missing error handling, accessibility and security problems. For each one, point to the line."* In `findings.md`: what did it find that you missed? What did it get wrong? Then ask it your 2 questions and write the answers in your own words.
5. **Fix one thing** (AI allowed): a failing check or something from the review. Commit first, fix it, check `git diff`, then commit the fix. In `findings.md`, say what was wrong, what you changed, and how you checked it works. If a change makes things worse, go back with `git restore`.
6. **Can we ship it?** A PM asks, "Can we ship this tomorrow?" In 100–150 words, answer yes or no and say why. Then compare it with your HW4: name one thing your HW4 does better than the AI's app, and one thing the AI's app does better.
7. **`ai_use.md`.** Fill it in (the five points on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)): the full chat for step 4 plus any other AI you used, what the AI wrote, and a short reflection. Or write "No AI used." If you already started the AI log in `findings.md`, you can leave it there.

## You're done when

- [ ] `findings.md` has your drawing, 2 questions (with answers), 4+ checks with pass/fail, the AI review, your fix, and your ship-it answer with the HW4 comparison
- [ ] At least 2 of your checks are `pytest` tests in `test_app.py`, and you ran them
- [ ] Your fix is committed, with a commit before it
- [ ] `ai_use.md` is filled in, or says "No AI used"

## Rubric (25 pts)

| Row | Pts |
|---|---|
| Drawing of one search, arrows labeled | 4 |
| 2 questions about the code, answered in your own words | 2 |
| 4+ checks tied to the prompt, with pass/fail, at least 2 as `pytest` tests | 10 |
| AI review compared with your own checks | 2 |
| One fix + how you confirmed it (commits before and after) | 4 |
| Ship-it answer + HW4 comparison: honest and specific | 3 |

## Background (read if you're stuck)

- **Checks vs. tests:** a check is something you try by hand ("search for nothing → see a message"). A `pytest` test does the same thing in code with `assert`, so you can rerun it any time. Both count. Class 10 and Class 11 show one `pytest` example.
- **Searching for something that shouldn't exist?** Try a made-up word. Then open the API URL in your browser with that word, and add `_score` to the `fields` list. Compare with a real artist's search. What does that tell you about what the user sees, and what would you change?
- **Why the AI review comes last:** if you ask the AI first, you'll only look where it points. Finding problems yourself is the skill; the AI is a second opinion.
- **GET vs. POST:** GET puts what you typed in the URL (`/results?artist=Monet`), so you can bookmark, share and refresh it: right for searches. POST hides the data inside the request: right for things that save or change something, like a sign-up.
- **Where to look for checks:** the states from HW4 (empty input, no results, API error, missing field), accessibility, keys and secrets, and things the prompt didn't ask for. The states are in the [HW4 help page](https://canvas.uw.edu/courses/1959879/pages/hw4-help-what-we-didnt-get-to-in-class-9), section 1. `try/except` and `timeout` are on the Class 10 slides.

## Relevant reading

- *Composing Programs* [1.5 Control → Testing](https://composingprograms.com/3ed/control/#testing): `assert` statements and test functions.
- [pytest: Get Started](https://docs.pytest.org/en/stable/getting-started.html): for `test_app.py`.

## Course objectives we cover

| # | Objective |
|---|---|
| 5 | Apply basic computational thinking concepts and practices, including reading, debugging, and testing code. |
| 8 | Use AI tools deliberately: verify their output, and explain what you built and what the AI did. |
