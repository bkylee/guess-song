import webbrowser


def get_user_playlists(sp):
    playlists = sp.current_user_playlists(limit=10)  # Fetch up to 10 playlists
    playlist_list = []

    for playlist in playlists["items"]:
        print(f"Playlist: {playlist['name']} - ID: {playlist['id']}")
        playlist_list.append({"name": playlist["name"], "id": playlist["id"]})

    return playlist_list


def get_playlist_tracks(sp, playlist_id):
    tracks = sp.playlist_tracks(playlist_id)
    track_list = []

    for item in tracks["items"]:
        track = item["track"]
        track_list.append(
            {
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "preview_url": track["preview_url"],  # Song preview
            }
        )

    return track_list


def play_song_preview(song):
    if song["preview_url"]:
        print(f"Playing preview of: {song['name']} by {song['artist']}")
        webbrowser.open(song["preview_url"])
    else:
        print(f"No preview available for {song['name']}")
