import os
from flask import Flask, request, render_template
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

@app.route('/albums/<id>', methods=['GET'])
def get_one_album(id):
    conn = get_flask_database_connection(app)
    album_repo = AlbumRepository(conn)
    artist_repo = ArtistRepository(conn)

    album = album_repo.find(id)
    artist = artist_repo.find(album.artist_id)

    return render_template('albums.html', albums=[album], artist=artist)

@app.route('/albums', methods=['POST'])
def create_new_album():
    conn = get_flask_database_connection(app)
    repo = AlbumRepository(conn)

    title = request.form['title']
    release_year = int(request.form['release_year'])
    artist_id = int(request.form['artist_id'])

    repo.create(title, release_year, artist_id)
    return ''

@app.route('/artists', methods=['GET'])
def get_all_artist_names():
    conn = get_flask_database_connection(app)
    repo = ArtistRepository(conn)

    artists = repo.all()

    return render_template('artists.html', artists=artists)

@app.route('/artists/<id>', methods=['GET'])
def get_one_artist(id):
    conn = get_flask_database_connection(app)
    repo = ArtistRepository(conn)

    artist = repo.find_with_albums(id)

    return render_template('artists.html', artists=[artist], albums=artist.albums)

@app.route('/artists', methods=['POST'])
def create_artist():
    conn = get_flask_database_connection(app)
    repo = ArtistRepository(conn)

    name = request.form['name']
    genre = request.form['genre']

    repo.create(name, genre)
    return ''


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

