# Import the Flask tools needed to create the web app and render HTML pages.

# Create the Flask application.

# Home route:
# When a user visits the home page,
# show the search form.

# Results route:
# Get the search term submitted by the user through the form.
# Remove unnecessary spaces from the search term.

# If the search term is empty:
#     Show a helpful message asking the user to enter a search term.

# Otherwise:
#     Search for artworks using the API helper function in api.py.
#     Handle an API request error and prepare a helpful error message.
#     If the search succeeds but returns no artworks:
#         Prepare a message saying no results were found.
#     If artworks are found:
#         Prepare the artwork data for the results page.
#         Handle missing fields so that missing information
#         does not appear as None.

# Render the results page with the search term,
# the artwork data, and any relevant message.

# Start the Flask development server when app.py is run directly.

from flask import Flask, render_template, request
from api import search_art

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", message="")


@app.route("/results")
def results():
    term = request.args.get("term", "").strip()

    if not term:
        return render_template(
            "home.html",
            message="Please enter an artist name or artwork title."
        )

    artworks = search_art(term)

    if artworks is None or not isinstance(artworks, list):
        return render_template(
            "results.html",
            term=term,
            artworks=[],
            error_message=(
                "Sorry, the artwork search failed. Please try again."
            )
        )

    artworks = [
        artwork for artwork in artworks
        if isinstance(artwork, dict)
    ]

    return render_template(
        "results.html",
        term=term,
        artworks=artworks,
        error_message=""
    )


if __name__ == "__main__":
    app.run(debug=True)
