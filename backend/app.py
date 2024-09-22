from auth import authenticate_spotify
from playlist import get_user_playlists, get_playlist_tracks
from game import start_guessing_game


def main():
    # Authenticate with Spotify
    sp = authenticate_spotify()

    # Fetch user playlists
    playlists = get_user_playlists(sp)
    if not playlists:
        print("No playlists found.")
        return

    # Display available playlists and choose one
    playlist_id = playlists[0]["id"]  # Select the first playlist for this example

    # Fetch tracks from the chosen playlist
    songs = get_playlist_tracks(sp, playlist_id)
    if not songs:
        print("No songs available in the playlist.")
        return

    # Start the guessing game
    start_guessing_game(songs)


if __name__ == "__main__":
    main()
