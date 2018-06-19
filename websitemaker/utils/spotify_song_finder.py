from ows_settings import SPOTIFY_CLIENT_ID
from ows_settings import SPOTIFY_CLIENT_SECRET
import spotipy
from spotipy.client import Spotify
from spotipy.client import SpotifyException
import spotipy.oauth2 as oauth2


class SpotifySongFinder:
    sp: Spotify = None

    @classmethod
    def find(cls, artist, track, retry=False):
        if not cls.sp:
            cls.sp = cls._refresh_credentials()

        try:
            results = cls.sp.search(q="artist:{a} track:{t}".format(a=artist, t=track))
        except SpotifyException:
            if not retry:
                cls.sp = cls._refresh_credentials()
                return cls.find(artist, track, retry=True)
            raise
        return results["tracks"]["items"]

    @classmethod
    def interactive_find(cls, artist, track):
        tracks = cls.find(artist, track)
        cls._display_tracks(tracks)
        print("Enter the number of the song. If you do not see the number, enter nothing.")
        number = input()
        if number:
            return tracks[int(number) - 1]["uri"]
        else:
            return None

    @classmethod
    def lucky_find(cls, artist, track):
        tracks = cls.find(artist, track)
        if len(tracks) > 0:
            return tracks[0]["uri"]

    @classmethod
    def _display_tracks(cls, tracks):
        print("Do any of these look right?")
        for idx, track in enumerate(tracks):
            select_num = idx + 1
            artist = ",".join(map(
                lambda a: a["name"],
                track["artists"]
            ))
            album = track["album"]["name"]
            print("{select_num}: \tArtist: {a}, Album: {alb}".format(
                select_num=select_num, a=artist, alb=album
            ))
        print()

    @classmethod
    def _refresh_credentials(cls) -> Spotify:
        credentials = oauth2.SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET
        )
        token = credentials.get_access_token()
        return spotipy.Spotify(auth=token)


if __name__ == "__main__":
    SpotifySongFinder.find("Heartless Bastards", "Only For You")
