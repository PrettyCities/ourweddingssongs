from websitemaker.renderer import Renderer


class Renderable:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def render(self) -> str:
        return self.renderer.render()
