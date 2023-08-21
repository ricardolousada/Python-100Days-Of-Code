# created by Ricardo Lousada
import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth



SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
#print(SPOTIFY_CLIENT_ID)
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
#print(SPOTIFY_CLIENT_SECRET)
#print(os.environ)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Ricardo Lousada",
    )
)

user_id = sp.current_user()["id"]
print(user_id)

date=input("What year do you would like to travel in 'YYYY-MM-DD' format: ")

URL = "https://www.billboard.com/charts/hot-100/" + date + "/"

# Write your code below this line 👇
request = requests.get(URL,verify=False)

web_site_text = request.text
#print(web_site_text)
soup = BeautifulSoup(web_site_text,'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
#print(song_names)

song_uris=[]
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)

