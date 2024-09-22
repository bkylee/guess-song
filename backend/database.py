import pyodbc


def initialize_db():
    global conn
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=your-server.database.windows.net;"
        "Database=your-database;"
        "Uid=your-username;"
        "Pwd=your-password;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )
    cursor = conn.cursor()
    cursor.execute(
        """
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Users')
    CREATE TABLE Users (
        UserId INT PRIMARY KEY IDENTITY,
        Username NVARCHAR(50)
    );
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Playlists')
    CREATE TABLE Playlists (
        PlaylistId INT PRIMARY KEY IDENTITY,
        PlaylistName NVARCHAR(100)
    );
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Guesses')
    CREATE TABLE Guesses (
        GuessId INT PRIMARY KEY IDENTITY,
        UserId INT FOREIGN KEY REFERENCES Users(UserId),
        PlaylistId INT FOREIGN KEY REFERENCES Playlists(PlaylistId),
        SongId NVARCHAR(50),
        Guess NVARCHAR(100),
        IsCorrect BIT
    );
    """
    )
    conn.commit()


def add_user(username):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (Username) VALUES (?)", username)
    conn.commit()


def add_playlist(playlist_name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Playlists (PlaylistName) VALUES (?)", playlist_name)
    conn.commit()


def record_guess(guess, song_id):
    cursor = conn.cursor()
    # Logic to check if guess is correct and store it
    is_correct = True  # Replace with actual checking logic
    cursor.execute(
        "INSERT INTO Guesses (UserId, PlaylistId, SongId, Guess, IsCorrect) VALUES (?, ?, ?, ?, ?)",
        1,
        1,
        song_id,
        guess,
        is_correct,
    )
    conn.commit()
    return {"correct": is_correct, "points": 1 if is_correct else 0}


def get_high_scores():
    cursor = conn.cursor()
    cursor.execute(
        "SELECT Username, SUM(IsCorrect) as Score FROM Guesses INNER JOIN Users ON Guesses.UserId = Users.UserId GROUP BY Username ORDER BY Score DESC"
    )
    return cursor.fetchall()
