# The prompt Copilot got

We pasted this into Copilot Chat in VS Code, in a new empty folder, and kept what it made: `app.py`, `api.py` and `templates/`. Nothing was changed.

```
Build me a small Flask app that searches the Art Institute of Chicago API for artworks by an artist.

Files:
- api.py: a function get_artworks(artist) that calls https://api.artic.edu/api/v1/artworks/search with the artist name as the search term (q), and asks for these fields: id, title, artist_title, date_display, image_id. Return the first 10 results.
- app.py: two routes.
  - "/" shows home.html, a page with a search form (one text box for the artist name and a Search button).
  - "/results" gets the artist name from the form, calls get_artworks, and shows results.html with a list of the artworks: title, date, and the image. The image URL is https://www.artic.edu/iiif/2/{image_id}/full/843,/0/default.jpg
- templates/home.html and templates/results.html

Keep it simple. I'm a beginner.
```
