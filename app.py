import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.artist_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def get_all_albums():
    conn = get_flask_database_connection(app)
    repo = AlbumRepository(conn)

    albums = repo.all()

    return render_template('albums.html', albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def get_one_album(id):
    conn = get_flask_database_connection(app)
    album_repo = AlbumRepository(conn)
    artist_repo = ArtistRepository(conn)

    album = album_repo.find(id)
    artist = artist_repo.find(album.artist_id)

    return render_template('albums.html', albums=[album], artist=artist)

@app.route('/albums/new', methods=['GET'])
def new_album_form():
    return render_template('new_album.html')

@app.route('/albums', methods=['POST'])
def create_new_album():
    conn = get_flask_database_connection(app)
    album_repo = AlbumRepository(conn)
    artist_repo = ArtistRepository(conn)

    title = request.form['title']
    try:
        release_year = int(request.form['release_year'])
    except ValueError:
        release_year = f'1'
    artist_name = request.form['artist']
    artist = artist_repo.find_by_name(artist_name)

    if type(artist) == Artist:
        artist_id = artist.id
    else:
        artist_id = None
    
    album = Album(None, title, release_year, artist_id)

    if album.is_valid():
        new_id = album_repo.create(title, release_year, artist_id).id
        return redirect(f'/albums/{new_id}')
    else:
        return render_template('new_album.html', album=album, errors=album.generate_errors()), 400

@app.route('/artists', methods=['GET'])
def get_all_artist_names():
    conn = get_flask_database_connection(app)
    repo = ArtistRepository(conn)

    artists = repo.all()

    return render_template('artists.html', artists=artists, more_info=False)

@app.route('/artists/<int:id>', methods=['GET'])
def get_one_artist(id):
    conn = get_flask_database_connection(app)
    repo = ArtistRepository(conn)

    artist = repo.find(id)
    try:
        artist.albums = repo.find_with_albums(id).albums
    except IndexError:
        artist.albums = []

    return render_template('artists.html', artists=[artist], more_info=True)

@app.route('/artists/new', methods=['GET'])
def new_artist_form():
    return render_template('new_artist.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    conn = get_flask_database_connection(app)
    repo = ArtistRepository(conn)

    name = request.form['name']
    genre = request.form['genre']

    artist = Artist(None, name, genre)

    if artist.is_valid():
        new_id = repo.create(name, genre).id
        return redirect(f'/artists/{new_id}')
    else:
        return render_template('new_artist.html', artist=artist, errors=artist.generate_errors()), 400


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

