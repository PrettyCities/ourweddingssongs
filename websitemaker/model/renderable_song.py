from websitemaker.model.song import Song
from websitemaker.renderer.renderable import Renderable


class RenderableSong(Song, Renderable):
    def __init__(self, artist, title):
        Song.__init__(self, artist, title)

    def render(self) -> str:
        # Default item
        pass