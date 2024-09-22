import requests


def get_access_token():
    # Implement Spotify OAuth2 token retrieval
    pass


def get_playlist_tracks(playlist_id):
    token = get_access_token()
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    songs = [
        {
            "id": item["track"]["id"],
            "name": item["track"]["name"],
            "artist": item["track"]["artists"][0]["name"],
            "album": item["track"]["album"]["name"],
            "preview_url": item["track"]["preview_url"],
        }
        for item in data["items"]
    ]
    return songs
