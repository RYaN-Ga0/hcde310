# app.py: the routes for the books app.
# SKELETON: the whole path works (form → /results → results page) with fake data.
# Next: replace one piece at a time, and commit each time something works.
from flask import Flask, render_template, request   # request (Flask), not requests!
from api import get_books_real

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    # 1. Read the search term from the form
    author = request.args.get("author_search", "")

    # 2. Empty input? → home page + message (check BEFORE calling the API)
    if not author.strip():
        return render_template(
            "home.html",
            message="Please enter an author name."
    )
    # 3. Call the API (fake data for now)
    books = get_books_real(author)

    # 4. API error? (get_books returned None) → home page + message
    if books is None:
        return render_template(
            "home.html",
            message="Sorry, the book search failed. Please try again."
        )
        # Remove books without a usable title
    books = [
        book for book in books
        if isinstance(book, dict) and book.get("title")
    ]
    # 5. No results, or nothing useful to show? → home page + message
    if not books:
        return render_template(
            "home.html",
            message="No books found. Please try another author."
        )
    # 6. Otherwise → results page
    return render_template("results.html", books=books, author=author)
