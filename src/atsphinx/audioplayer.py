"""Register directive to render audio element."""

from pathlib import Path
from urllib.parse import quote

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.directives import SphinxDirective
from sphinx.util.docutils import SphinxRole
from sphinx.writers.html5 import HTML5Translator

__version__ = "0.0.0"


class audio(nodes.image):  # noqa: D101
    pass


class AudioDirective(SphinxDirective):  # noqa: D101
    required_arguments = 1
    option_spec = {
        "controls": directives.flag,
    }

    def run(self):  # noqa: D102
        uri = directives.uri(self.arguments[0])
        self.options["uri"] = uri
        node = audio(**self.options)
        return [
            node,
        ]


class AudioRole(SphinxRole):  # noqa: D101
    def run(self):  # noqa: D102
        options = {
            "uri": directives.uri(self.text),
            "controls": True,
        }
        node = audio(**options)
        return [node], []


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


def setup(app: Sphinx):  # noqa: D103
    app.add_node(audio, html=(visit_audio, depart_audio))
    app.add_directive("audio", AudioDirective)
    app.add_role("audio", AudioRole())
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
