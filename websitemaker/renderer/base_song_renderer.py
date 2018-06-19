from websitemaker.renderer import Renderer
from websitemaker.model.song import Song
from ows_settings import WEBSITE_TEMPLATE_DIRECTORY


class BaseSongRenderer(Renderer):
    template_name = "renderable_song.html.tmpl"

    def __init__(self, song: Song):
        self.song = song
        Renderer.__init__(self,
                          template_location=WEBSITE_TEMPLATE_DIRECTORY / self.template_name)

    def render(self) -> str:
        return self.get_template().render(Song.unapply(self.song))
