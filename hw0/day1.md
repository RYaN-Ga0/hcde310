# Day 1 "before" snapshot

**Name:** Ruihan(Ryan) Gao

**Partner (if any):** Murphy Jiang

## Before we prompted

### 1. Who is it for, and what do they want to do?

It's for **art students, curious visitors, and people exploring the Art Institute of Chicago collection who want to discover artworks through text or a simple sketch**.

**"The user can..." sentences:**

1. The user can **search the Art Institute of Chicago collection by typing keywords and applying filters such as year, art form, and subject**.

2. The user can **draw a simple sketch and use it as a starting point for finding related artworks, then browse the results and save interesting artworks to a personal collection**.

### 2. Our sketch

![sketch](sketch.png)

### 3. Our prediction

We expected the app would **closely follow our sketch, with a search bar at the top, navigation tabs, filters on the left, a drawing canvas in the center, and a grid of artwork search results**.

We also expected the app to **connect to the Art Institute of Chicago API so that searches and filters would produce real artwork images and information rather than placeholder results**.

## What we got

### 4. What the AI made
I used AI in several steps to build the app.

First, I used AI to refine my hand-drawn sketch. I gave the AI my original sketch and asked it to improve the visual organization while keeping the main layout and ideas from my drawing.

Then, I took the refined sketch and combined it with the prompt provided in Canva. I gave both the sketch and the prompt to the AI and asked it to build the web app based on them. The AI generated the HTML, CSS, and JavaScript code for the application.

After the initial code was generated, I also asked the AI questions about parts of the code that I did not understand. For example, I asked it to explain how the API search worked, how the filters were implemented, how the artwork results were displayed, and how the sketch canvas and saved collection worked.

Through this process, the AI was not only generating the final code, but also helping me understand parts of the implementation that I was unfamiliar with.
![screenshot](screenshot.png)

### 5. Sketch vs. app

* **Matches our sketch:**
  The AI followed the main structure of the sketch quite closely. It created a top search bar, tabs for Sketch Search, Text Search, and My Collection, a left sidebar containing filters, a drawing canvas, a "Use Sketch to Search" button, and a grid of artwork results. The results also contain images, titles, artists, and dates, which matches the main purpose of the sketch.

* **Different from our sketch:**
  The AI added some functionality and interface details that were not explicitly shown in the sketch. For example, it added responsive behavior for smaller screens, pagination controls, a save/favorite feature, and error handling for API failures. The exact visual styling, spacing, and number of results were also different from the hand-drawn sketch.

* **The AI decided** (something we never said):
  The AI decided that the "Use Sketch to Search" feature should use a **one-word text label** to search the Art Institute API. We did not specify this behavior. The AI also decided to use browser storage to implement the "My Collection" feature.

### 6. What did I keep, change, or reject, and why?

I kept the overall layout because it matched the main structure of my sketch and made the different functions easy to understand. I also kept the real API search, artwork image results, filters, drawing canvas, and My Collection because these features support the main goal of exploring artworks.

I would change the sketch-search behavior. The AI explained that the Art Institute API only supports text-based search, so it cannot directly understand the content of a drawing. Instead, the generated app uses a text label to represent the sketch. This is different from what I originally imagined, but it is a reasonable solution given the limitations of the API.

I would also consider simplifying some of the additional features if they make the interface more complicated than necessary. For example, pagination and the saved collection are useful, but making the core search and sketch interaction work reliably is more important.

## 7. Explain back

One important part of the code is the search function.

In my own words, when the user clicks Search, the program collects the information currently entered in the search box and the selected filters. It combines these into a request to the Art Institute of Chicago API. The API returns a list of artworks, and the program takes the artwork information and creates a result card for each one. Each card can show an image, title, artist, and date.

The important idea is that the app itself does not contain all of the artwork data. Instead, it requests the data from the external API when the user searches.

## Looking ahead

### 8. What does it do? Does it work? What broke?

The app is intended to let users search and explore artworks from the Art Institute of Chicago collection using text, filters, and a drawing interface. It also provides a way to save artworks in a personal collection.

The basic interface and code structure were generated successfully. However, the AI said it had not tested the app against the live API, so I still need to verify that the search and filter functions work correctly with the real API.

The biggest limitation I noticed is the sketch-search feature. The Art Institute API cannot directly perform image or drawing recognition, so the app cannot actually compare the user's drawing with artwork images. Instead, the current implementation uses a text label to perform the search.

### 9. How much do I understand about how it works? (0–100%)

**My number:** 90%

**Why that number:**

I understand most of the overall structure and logic of the app. I understand how the HTML creates the interface, how CSS controls the layout and appearance, and how JavaScript handles user interactions, API requests, filtering, drawing, pagination, and the saved collection.

I also understand the main flow of the application: the user's input is collected, the app constructs a request to the Art Institute of Chicago API, the API returns artwork data, and the JavaScript uses that data to generate the artwork cards shown on the page.

I chose 90% rather than 100% because there are still some implementation details and JavaScript/API parameters that I would need to inspect more carefully to explain precisely. However, I understand enough of the code that I could follow its logic and make meaningful changes to the application.

### 10. What would I need to know to tell whether it's *well designed or well built*?

I would need to know whether the app actually satisfies the user's main goals and whether the interface is easy to understand without additional instructions.

For the implementation, I would want to check:

* Whether searches and filters return the expected artworks.
* Whether the API requests are constructed correctly.
* Whether the app handles API errors, empty results, and slow network connections.
* Whether the drawing interface works reliably with a mouse, touchscreen, or stylus.
* Whether the layout works on different screen sizes.
* Whether saved artworks remain available after refreshing the page.
* Whether the code is organized clearly enough that another person can understand and modify it.
* Whether the app stays within the assignment's requirement of being a small, single-page application.

For the sketch-search feature specifically, I would also need to decide whether converting a drawing into a text keyword actually provides enough value to the user.

### 11. What do I hope to be able to do by week 10?

By week 10, I hope to be able to **understand and modify AI-generated code rather than simply accepting the AI's implementation**.

I want to be able to identify which parts of the code control the interface, user interactions, API requests, and data processing, and make meaningful changes myself.

I also hope to become better at evaluating whether an AI-generated application is actually well designed and functional, including recognizing limitations or incorrect assumptions made by the AI. Ideally, I want to be able to describe what I want, use AI to help implement it, test the result, and then make informed changes to the code myself.
