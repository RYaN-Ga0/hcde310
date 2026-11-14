from app import app


def test_home_shows_search_form():
    client = app.test_client()
    page = client.get("/")
    assert page.status_code == 200
    assert b"Artist name" in page.data


def test_empty_search_shows_message():
    client = app.test_client()
    page = client.post("/results", data={"artist": ""})

    assert page.status_code == 200
    assert b"No search term entered." in page.data


def test_search_displays_artwork(monkeypatch):
    def fake_get_artworks(artist):
        assert artist == "Monet"
        return [
            {
                "id": 123,
                "title": "Water Lilies",
                "artist_title": "Claude Monet",
                "date_display": "1906",
                "image_id": "test-image-id"
            }
        ]

    monkeypatch.setattr("app.get_artworks", fake_get_artworks)

    client = app.test_client()
    page = client.post("/results", data={"artist": "Monet"})

    assert page.status_code == 200
    assert b'Results for "Monet"' in page.data
    assert b"Water Lilies" in page.data
    assert b"1906" in page.data
    assert b"test-image-id" in page.data


def test_no_results_shows_message(monkeypatch):
    def fake_get_artworks(artist):
        return []

    monkeypatch.setattr("app.get_artworks", fake_get_artworks)

    client = app.test_client()
    page = client.post("/results", data={"artist": "Unknown Artist"})

    assert page.status_code == 200
    assert b"No results found." in page.data
