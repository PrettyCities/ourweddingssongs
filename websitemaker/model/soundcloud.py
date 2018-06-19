from websitemaker.model.song import Song
from websitemaker.renderer.renderable import Renderable


class Soundcloud(Renderable, Song):
    def __init__(self, artist, title, uri):
        Song.__init__(self, artist, title)
        self.uri = uri

    def render(self) -> str:

        pass
