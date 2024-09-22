def add_user(username):
    """
    Add a user to the Users table if the user does not already exist.

    Parameters:
    username (str): The username of the user.

    Returns:
    None
    """
    conn = create_connection()
    cursor = conn.cursor()

    # Create Users table if it doesn't exist
    cursor.execute(
        """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Users' AND xtype='U')
        CREATE TABLE Users (
            id INT PRIMARY KEY IDENTITY(1,1),
            username NVARCHAR(50) UNIQUE NOT NULL
        )
    """
    )

    # Insert user if they don't exist
    cursor.execute(
        """
        IF NOT EXISTS (SELECT * FROM Users WHERE username = ?)
        INSERT INTO Users (username) 
        VALUES (?)
    """,
        (username, username),
    )

    conn.commit()
    conn.close()


def add_playlist(playlist_id, playlist_name):
    """
    Add a playlist to the Playlists table if the playlist does not already exist.

    Parameters:
    playlist_id (str): The Spotify ID of the playlist.
    playlist_name (str): The name of the playlist.

    Returns:
    None
    """
    conn = create_connection()
    cursor = conn.cursor()

    # Create Playlists table if it doesn't exist
    cursor.execute(
        """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Playlists' AND xtype='U')
        CREATE TABLE Playlists (
            id INT PRIMARY KEY IDENTITY(1,1),
            playlist_id NVARCHAR(50) UNIQUE NOT NULL,
            playlist_name NVARCHAR(100) NOT NULL
        )
    """
    )

    # Insert playlist if it doesn't exist
    cursor.execute(
        """
        IF NOT EXISTS (SELECT * FROM Playlists WHERE playlist_id = ?)
        INSERT INTO Playlists (playlist_id, playlist_name)
        VALUES (?, ?)
    """,
        (playlist_id, playlist_name),
    )

    conn.commit()
    conn.close()
