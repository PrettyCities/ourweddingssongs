from jinja2 import Template

from ows_settings import WEBSITE_INDEX_HTML_OUT
from ows_settings import WEBSITE_TEMPLATE_DIRECTORY
from websitemaker.aws_services import AwsServices
from websitemaker.renderer.renderer_factory import RendererFactory


class WebsiteMaker:
    @classmethod
    def render(cls):
        with open(WEBSITE_TEMPLATE_DIRECTORY / "index.html.tmpl") as template_file:
            template = Template(template_file.read())

        items = cls.get_items()

        rendered = template.render(**items)

        with open(WEBSITE_INDEX_HTML_OUT, 'w') as template_file_out:
            template_file_out.write(rendered)

    @classmethod
    def get_items(cls):
        cocktail_songs = []
        dinner_songs = []
        party_songs = []

        for item in AwsServices.get_items():
            renderer = RendererFactory.create(item)

            if item["time"] == "c":
                cocktail_songs.append(renderer)
            if item["time"] == "d":
                dinner_songs.append(renderer)
            if item["time"] == "p":
                party_songs.append(renderer)

        return {
            "cocktail_songs": cocktail_songs,
            "dinner_songs": dinner_songs,
            "party_songs": party_songs
        }


if __name__ == "__main__":
    WebsiteMaker.render()
