from lib.album import Album

def test_album_construct():
    album = Album(1, "Test Album", 1, 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 1
    assert album.artist_id == 1

def test_album_format_nicely():
    album = Album(1, "Test Album", 1, 1)
    assert str(album) == "Album(1, Test Album, 1, 1)"

def test_albums_equal():
    album1 = Album(1, "Test Album", 1, 1)
    album2 = Album(1, "Test Album", 1, 1)
    assert album1 == album2

def test_album_not_valid():
    album1 = Album(None, "Test Album", 1, 1)
    album2 = Album(None, 53, 1, 1)
    album3 = Album(None, "Test Album", None, 1)
    album4 = Album(None, "Test Album", 1, '1')

    assert album1.is_valid()
    assert not album2.is_valid()
    assert not album3.is_valid()
    assert not album4.is_valid()

def test_album_generate_errors():
    album1 = Album(None, "Test Album", 1, 1)
    album2 = Album(None, 53, 1, 1)
    album3 = Album(None, "Test Album", '1', 1)
    album4 = Album(None, "Test Album", 1, -1)
    album5 = Album(None, "", 1, 1)

    assert album1.generate_errors() == []
    assert album2.generate_errors() == ["Title must be text"]
    assert album3.generate_errors() == ["Release year must be a number"]
    assert album4.generate_errors() == ["Artist ID must not be a negative number"]
    assert album5.generate_errors() == ["Title must not be blank"]
