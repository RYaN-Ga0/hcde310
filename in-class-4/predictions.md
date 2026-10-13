# Class 4: Five broken snippets

Your name: Ruihan Gao
Collaborator: Murphy Jiang

### Snippet 1
- **Which line breaks?** `print("Find it in room " + exhibit["Room"])`
- **What error will Python show?** `KeyError: 'Room'`
- **What's the fix?** Change `"Room"` to `"room"` because dictionary keys are case-sensitive.

### Snippet 2
- **Which line breaks?** `print("Find it in room " + exhibit["room"])`
- **What error will Python show?** `TypeError: can only concatenate str (not "int") to str`
- **What's the fix?** Convert the room number to a string: `print("Find it in room " + str(exhibit["room"]))`.

### Snippet 3
- **Which line breaks?** `print(i + 1, exhibits[i])`
- **What error will Python show?** `IndexError: list index out of range`
- **What's the fix?** Change `range(len(exhibits) + 1)` to `range(len(exhibits))`.

### Snippet 4
- **Which line breaks?** `print(count_visits(visit, 243))`
- **What error will Python show?** `NameError: name 'visit' is not defined`
- **What's the fix?** Change `visit` to `visits`.

### Snippet 5
- **Which line breaks?** `print(title.upper())`
- **What error will Python show?** `AttributeError: 'NoneType' object has no attribute 'upper'`
- **What's the fix?** Add `return longest` at the end of `longest_title()` so the function returns the longest title instead of returning `None`.


### Snippet 1
- **Which line broke?** `print("Find it in room " + exhibit["Room"])`
- **What error did Python show?** `KeyError: 'Room'`
- **What's the fix?** Change `exhibit["Room"]` to `exhibit["room"]`.

### Snippet 2
- **Which line broke?** `print("Find it in room " + exhibit["room"])`
- **What error did Python show?** `TypeError: can only concatenate str (not "int") to str`
- **What's the fix?** Convert the integer to a string using `str(exhibit["room"])`.

### Snippet 3
- **Which line broke?** `print(i + 1, exhibits[i])`
- **What error did Python show?** `IndexError: list index out of range`
- **What's the fix?** Remove `+ 1` from `range(len(exhibits) + 1)`.

### Snippet 4
- **Which line broke?** `print(count_visits(visit, 243))`
- **What error did Python show?** `NameError: name 'visit' is not defined`
- **What's the fix?** Change `visit` to `visits`.

### Snippet 5
- **Which line broke?** `print(title.upper())`
- **What error did Python show?** `AttributeError: 'NoneType' object has no attribute 'upper'`
- **What's the fix?** Add `return longest` at the end of the `longest_title()` function.

### Bonus
Snippet 5 prints `Water Lilies` before crashing. The function prints the longest title but does not return it. Therefore, `title` receives `None`, and calling `title.upper()` raises an `AttributeError`.

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- **Snippet #:** 5
- **Our guess before asking:** The error is probably caused by `title` not being a string. The function prints the longest title, but maybe it does not return a value.
- **Chat:**

  - **Snippet #:** 5

- **Our guess before asking:** I think the problem might be that `title` is not a string. The function seems to print the longest title, but I am not sure why `title.upper()` causes an error.

- **Chat:**

  **Me:** I'm working on Snippet 5 in Python. It prints something and then crashes at `title.upper()`. Can you help me understand why? Please give me hints instead of directly giving me the solution.

  **AI:** Sure! Let's think about what happens before `title.upper()` runs. Where does the variable `title` get its value? Look at the function call that assigns a value to it. What does Python return from a function if there is no `return` statement?

  **Me:** I think Python returns `None` if the function doesn't return anything. Does that mean `title` is `None`?

  **AI:** Exactly! A function can print a value without returning that value. If your function only prints the longest title, the variable receiving the function's result will still be `None`. Since `None` doesn't have an `.upper()` method, Python raises an `AttributeError`. Can you think of how to make the function give the longest title back to the caller?

  **Me:** I should use a `return` statement to return the longest title instead of only printing it.

- **Did it give you too much? What did you do?**

  No. The AI gave me hints and helped me understand the difference between `print()` and `return`. I figured out the fix myself instead of having the AI give me the answer immediately.
