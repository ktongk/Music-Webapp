from flask import Flask, render_template
import os, requests, random
app = Flask(__name__)

API_TOKEN =  \
    "JiwPumUVzR09r0Amrig4U14cGcYdoiNVcGTtncZUwYMNTt0SuEVmeuOV7kAPI4HW"
API_URL = 'https://api.genius.com/'

def random_song():
    search_term = random.choice(
        [
            'love',
            'life',
            'happy',
            'sad',
            'rock',
            'pop',
        ]
    )
    response = requests.get(
        f"{API_URL}search",
        headers={'Authorization': f'Bearer {API_TOKEN}'},
        params={'q': search_term}
    )
    data = response.json()
    song = random.choice(data['response']['hits'])['result']
    return {
        'title': song['title'],
        'artist': song['primary_artist']['name'],
        'image_url': song['song_art_image_url']
    }




@app.route('/')
def index():
    song = random_song()
    return render_template('index.html', song=song)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)