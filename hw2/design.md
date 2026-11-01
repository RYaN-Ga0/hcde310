# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
A list of dictionaries represents a collection of artworks, where each dictionary stores the information for one artwork. This makes it easy to iterate through all artworks, process each one, and add new artworks to the collection. Each artwork can also have different fields because some information may be missing.

If we used one big dictionary instead, we could look up an artwork directly by its key, such as its title. However, we would need unique keys, and artworks with duplicate titles could overwrite each other. A list also makes it natural to preserve the order of the artworks.

## 2. Which fields are sometimes missing? What should the app show when they are?
The fields that are sometimes missing are artist, year, and medium. The app should handle missing information gracefully instead of crashing. For example, it could display "Unknown" for a missing artist or year, and "Unknown" or "Not specified" for a missing medium. The app should use a consistent placeholder so users can tell that the information is unavailable.
