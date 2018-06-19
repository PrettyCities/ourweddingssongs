from abc import abstractmethod

from jinja2 import Template


class Renderer:
    def __init__(self, template_location):
        self.template_location = template_location

    def get_template(self) -> Template:
        with open(self.template_location) as template_file:
            return Template(template_file.read())

    @abstractmethod
    def render(self) -> str:
        pass
