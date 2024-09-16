# noqa: D100
from pathlib import Path
from urllib.parse import quote

from docutils import nodes
from sphinx.writers.html5 import HTML5Translator


class audio(nodes.image):  # noqa: D101
    pass


def visit_audio(self: HTML5Translator, node: audio):  # noqa: D103
    attributes = {}
    # Resolve audio file uri
    uri = node["uri"]
    if uri in self.builder.images:
        node["uri"] = Path(self.builder.imgpath) / quote(self.builder.images[uri])
    attributes["src"] = node["uri"]
    # Set boolean attributes
    if "controls" in node:
        attributes["controls"] = "controls"
    # Set starttag
    element = ""
    element += self.starttag(node, "audio", **attributes)
    self.body.append(element)


def depart_audio(self: HTML5Translator, node: audio):  # noqa: D103
    self.body.append("</audio>")
    pass
