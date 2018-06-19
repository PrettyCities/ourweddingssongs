from typing import Dict


class Song:
    def __init__(self, artist, title, uri=None):
        self.artist = artist
        self.title = title
        self.uri = uri

    @classmethod
    def apply(cls, item: Dict[str, str], uri=None):
        return Song(
            artist=item["artist"],
            title=item["title"],
            uri=uri
        )

    @classmethod
    def unapply(cls, song) -> Dict[str, str]:
        return {
            "artist": song.artist,
            "title": song.title,
            "uri": song.uri
        }
