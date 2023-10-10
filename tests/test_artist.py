from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""
def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist", "Test Genre")
    artist2 = Artist(1, "Test Artist", "Test Genre")
    assert artist1 == artist2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.

def test_artist_validation():
    artist1 = Artist(None, "Test Artist", "Test Genre")
    artist2 = Artist(None, "", "Test Genre")
    artist3 = Artist(None, "Test Artist", "")
    artist4 = Artist(None, 1, "Test Genre")

    assert artist1.is_valid()
    assert not artist2.is_valid()
    assert not artist3.is_valid()
    assert not artist4.is_valid()

def test_generate_errors():
    artist = Artist(None, '', 1)

    assert len(artist.generate_errors()) == 2
