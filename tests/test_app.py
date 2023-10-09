from lib.album_repository import *
from lib.artist_repository import *
from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_list_all_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    
    page.goto(f'http://{test_web_address}/albums')

    divs = page.locator('div')

    expect(divs).to_have_count(12)