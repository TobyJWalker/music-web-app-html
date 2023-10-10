from lib.album_repository import *
from lib.artist_repository import *
from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_list_all_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    
    page.goto(f'http://{test_web_address}/albums')

    album_list = page.locator('.l-albums')

    expect(album_list).to_have_count(12)

def test_list_one_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')

    page.goto(f'http://{test_web_address}/albums/1')

    h2 = page.locator('h2')

    expect(h2).to_have_text('Doolittle')
    expect(h2).to_have_count(1)

def test_click_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')

    page.goto(f'http://{test_web_address}/albums')
    page.click(f'text=Album: Doolittle')

    h2 = page.locator('h2')
    expect(h2).to_have_text('Doolittle')

def test_list_all_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')

    page.goto(f'http://{test_web_address}/artists')
    divs = page.locator('div')

    expect(divs).to_have_count(4)

def test_list_one_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')

    page.goto(f'http://{test_web_address}/artists/1')
    h2 = page.locator('h2')
    h3 = page.locator('h3')

    expect(h2).to_have_text('Pixies')
    expect(h3).to_have_text('Albums')

def test_click_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')

    page.goto(f'http://{test_web_address}/artists')
    page.click(f'text=Artist: Pixies')

    h2 = page.locator('h2')

    expect(h2).to_have_text('Pixies')

def test_create_new_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')

    page.goto(f'http://{test_web_address}/albums')
    page.click('text=Add new album')
    page.fill('input[name="title"]', 'New Album')
    page.fill('input[name="release_year"]', '2021')
    page.fill('input[name="artist"]', 'Pixies')
    page.click('input[type="submit"]')

    h2 = page.locator('h2')
    expect(h2).to_have_text('New Album')