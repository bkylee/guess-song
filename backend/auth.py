import spotipy
from spotipy.oauth2 import SpotifyOAuth


def authenticate_spotify():
    SPOTIPY_CLIENT_ID = "your-client-id"
    SPOTIPY_CLIENT_SECRET = "your-client-secret"
    SPOTIPY_REDIRECT_URI = "your-redirect-uri"

    sp_oauth = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="user-library-read playlist-read-private",
    )

    sp = spotipy.Spotify(auth_manager=sp_oauth)
    return sp
