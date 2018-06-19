class SongRequest:
    def __init__(self, artist: str, title: str, time: str, uri: str = None):
        self.artist = artist
        self.title = title
        self.time = time
        self.uri = uri

    def to_kwargs(self):
        """
        TODO: Don't just assume spotify uri
        """
        return {
            "artist": self.artist,
            "title": self.title,
            "time": self.time,
            "spotify_uri": self.uri
        }
