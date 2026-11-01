# HW2 Part 6 – AI log (`ai_log.md`)

The tutor walks you through the routine (Try → Predict → Run → Explain → Log) as you chat, so your transcript shows most of it. In `ai_log.md`:

---

## 1. One prediction
*copy one prediction you made in a chat. Were you right? If not, what surprised you?*
Before running part2.py, I predicted that artworks with missing fields could cause errors when accessing dictionary keys directly.
I learned that using .get("artist", "Unknown") or .get("year", "Unknown") provides a default value when a key is missing, avoiding a KeyError in that situation.
My prediction was correct, and I was surprised by how easily .get() handles missing fields without requiring extra if statements.

## 2. What clicked
*pick one thing you were stuck on or didn't know. Without looking at the transcript, explain it in your own words.*
I learned how dictionaries can be used to count occurrences. For each artwork, I get the artist's name and check whether it already exists in the counting dictionary. If it does, I increase the count by one; otherwise, I initialize the count to one. This pattern makes it easy to count how many artworks belong to each artist.

## 3. Too much?
*Did the tutor ever give you too much? What did you do? (one line)*


## 4. Transcripts
*paste every tutor chat you used for HW2 (one is fine if that's all you had)*
When the tutor explained too much at once, I focused on one concept at a time and asked follow-up questions to clarify what I did not understand.