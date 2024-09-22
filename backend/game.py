def start_guessing_game(songs, username, playlist_id, playlist_name):
    total_songs = len(songs)
    total_score = 0

    # Add the user and playlist to the database (if not already present)
    add_user(username)
    add_playlist(playlist_id, playlist_name)

    for idx, song in enumerate(songs, start=1):
        print(f"\nSong {idx}/{total_songs}")

        # Get user guesses
        song_guess = input("Guess the song name: ")
        artist_guess = input("Guess the artist: ")
        album_guess = input("Guess the album name: ")

        song_correct = song_guess.lower() == song["name"].lower()
        artist_correct = artist_guess.lower() == song["artist"].lower()
        album_correct = album_guess.lower() == song["album"].lower()

        # Calculate score for this round
        round_score = 0
        if song_correct:
            round_score += 1
            print(f"Correct Song Name! It's '{song['name']}'")
        else:
            print(f"Wrong! The correct song name was '{song['name']}'.")

        if artist_correct:
            round_score += 1
            print(f"Correct Artist! It's '{song['artist']}'")
        else:
            print(f"Wrong! The correct artist was '{song['artist']}'.")

        if album_correct:
            round_score += 1
            print(f"Correct Album! It's '{song['album']}'")
        else:
            print(f"Wrong! The correct album was '{song['album']}'.")

        total_score += round_score
        print(f"Score for this song: {round_score}/3")

    # Final score and save to the database
    print(f"\nGame Over! Your total score: {total_score}/{total_songs * 3}")

    # Record the score in the database
    add_score(username, playlist_id, total_score)
