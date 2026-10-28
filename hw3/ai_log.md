# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*

def save_results(artworks):
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown"
            date = artwork.get("date_display") or "Unknown date"
            file.write(f"{title} | {artist} | {date}\n")


## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*

 I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.
 
My attempt so far: 

def save_results(artworks):
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown"
            date = artwork.get("date_display") or "Unknown date"
            file.write(f"{title} | {artist} | {date}\n")
Where I'm stuck: can't achieve the function which can save the results 
The function I need: save the results when every searching, and print one line per artwork (title, artist, date) to a file
Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.

Choosing a realistic sample input to test prediction
python
# AI-written
def save_results(artworks):
    """Takes a list of artwork dictionaries, returns nothing, and appends one line per artwork to results.txt."""
    with open("results.txt", "a", encoding="utf-8") as file:
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown"
            date = artwork.get("date_display") or "Unknown date"
            file.write(f"{title} | {artist} | {date}\n")
Two new things in it:

open(filename, "a", encoding="utf-8") opens a text file for adding to the end (creating it if it doesn’t exist), and the encoding keeps accented characters in names from causing errors.
with ... as file: runs the indented block while the file is open, then closes it automatically.
Predict: Imagine you run this one real input, where the list holds one artwork:

python
save_results([{"title": "Water Lilies", "artist_title": "Claude Monet", "date_display": "1906"}])
What value does the call give back?
What will results.txt contain afterward?
If you ran that exact line a second time, what would the file contain then?
Write your predictions down before you run it, then tell me what you predicted and what actually happened. I’ll hold off on explaining anything until then.



## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*

I predict that search_results.txt will contain one line for each artwork in the sample data. Each line will include the artwork's title, artist, and date, separated by |. If an artwork is missing an artist or date, the function will use the default value instead of writing None. I expect the file to contain five lines because the sample data has five artworks.


After testing save_results() with the sample data used by check.py, the file contained:

Lion (One of a Pair, South Pedestal) | Edward Kemeys | 1893
Nude with Cats | Pablo Picasso | 1901
Baroque Pearl Mounted as a Cat Holding a Mouse | Unknown | 17th century
Cat Making Up | Inagaki Tomoo | 1962
Homesickness | René Magritte | c. 1948


## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*

I learned that writing each artwork to a file requires opening the file in write mode and passing the file object to file.write(). I also learned that using or with .get() handles both missing fields and fields whose values are None, so the output contains a readable fallback instead of None.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*

I changed the output format so that the date appears before the title and artist. I made this change because I wanted to see the artwork's date first when reading the saved results.