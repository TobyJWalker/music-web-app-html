from lib.album import Album
from lib.album_repository import AlbumRepository

def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    albums = repo.all()

    assert albums == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

def test_find_one_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    album = repo.find(1)

    assert album == Album(1, "Doolittle", 1989, 1)

def test_create_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    album = repo.create('World of Walker', 2021, 5)

    assert len(repo.all()) == 13

def test_delete_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    repo.delete(1)

    all_albums = repo.all()

    assert len(all_albums) == 11
    assert all_albums[0] == Album(2, 'Surfer Rosa', 1988, 1)