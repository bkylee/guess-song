from flask import Flask, request, jsonify
from spotify_integration import get_playlist_tracks
from database import (
    initialize_db,
    add_user,
    add_playlist,
    record_guess,
    get_high_scores,
)

app = Flask(__name__)

# Initialize the database connection
initialize_db()


@app.route("/api/songs", methods=["GET"])
def fetch_songs():
    playlist_id = request.args.get("playlist_id")
    songs = get_playlist_tracks(playlist_id)
    return jsonify(songs)


@app.route("/api/guess", methods=["POST"])
def handle_guess():
    data = request.json
    guess = data["guess"]
    song_id = data["songId"]

    result = record_guess(guess, song_id)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
