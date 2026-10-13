# HW1 notes

## Part 4: Predict, run, explain

**My prediction for `predict.py` (written BEFORE running it):**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**What it actually printed:**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?
 I predicted the output correctly. The last two lines print different numbers because len(titles) counts the number of artworks in the list, which is 10, while len(titles[0]) counts the characters in the first title, "The Bedroom", which is 11. Spaces count as characters, too.

## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?

## Part 5: Short Reflection

Looking back at my Day 1 app, I can now better recognize some basic programming concepts. For example, a list could store multiple artworks or items that appear in the app. A loop could go through the list and display each item without writing the same code many times. An `if` statement could check what the user types or selects and decide what to show next. If I only had screenshots, I would guess that the code used variables to store information, loops to display repeated elements, and conditions to handle different user actions. I understand better now how these basic concepts work together to make an interactive app.