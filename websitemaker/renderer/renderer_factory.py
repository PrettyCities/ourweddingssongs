from typing import Dict

from websitemaker.model.song import Song
from websitemaker.renderer import BaseSongRenderer
from websitemaker.renderer import SoundCloudRenderer
from websitemaker.renderer import SpotifyRenderer


class RendererFactory:
    @classmethod
    def create(cls, item: Dict[str, str]):
        if item.get("spotify_uri", None):
            song = Song.apply(item, uri=item["spotify_uri"])
            return SpotifyRenderer(song)
        elif item.get("soundcloud_uri", None):
            song = Song.apply(item, uri=item["soundcloud_uri"])
            return SoundCloudRenderer(song)
        else:
            song = Song.apply(item)
            return BaseSongRenderer(song)
