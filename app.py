from flask import Flask, render_template
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GENIUS_API_TOKEN = os.getenv('GENIUS_API_TOKEN')
GENIUS_API_URL = 'https://api.genius.com/'

def get_random_song():
    try:
        search_terms = ['love', 'life', 'happy', 'sad', 'rock', 'pop', 'dance', 'music']
        search_term = random.choice(search_terms)
        
        headers = {
            'Authorization': f'Bearer {GENIUS_API_TOKEN}'
        }
        
        params = {
            'q': search_term,
            'per_page': 50
        }
        
        response = requests.get(f"{GENIUS_API_URL}/search", headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        hits = data.get('response', {}).get('hits', [])
        
        if not hits:
            return None
        
        song = random.choice(hits)['result']
        
        return {
            'title': song.get('title', 'Unknown Title'),
            'artist': song.get('primary_artist', {}).get('name', 'Unknown Artist'),
            'artist_image': song.get('primary_artist', {}).get('image_url', 'https://via.placeholder.com/150x150.png?text=No+Image+Available'),
            'image_url': song.get('song_art_image_url', 'https://via.placeholder.com/500x500.png?text=No+Image+Available'),
            'lyrics_url': song.get('url', '#')
        }
    except Exception as e:
        print(f"Error fetching song: {e}")
        return None

@app.route('/')
def index():
    song = get_random_song()
    if song:
        return render_template('index.html', song=song)
    else:
        return "<h1>Could not fetch a song at this time. Please try again later.</h1>"

if __name__ == '__main__':
    app.run(
        port= int(os.getnv('PORT', 8080)),
        host= os.getnv('IP', '0.0.0.0'),
        debug=True
    )
