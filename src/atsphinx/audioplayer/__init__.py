"""Register directive to render audio element."""

from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.directives import SphinxDirective
from sphinx.util.docutils import SphinxRole

from . import nodes

__version__ = "0.0.0"


class AudioDirective(SphinxDirective):  # noqa: D101
    required_arguments = 1
    option_spec = {
        "no-controls": directives.flag,
    }

    def run(self):  # noqa: D102
        attributes = {
            "uri": directives.uri(self.arguments[0]),
            "controls": self.options.get("no-controls", False),
        }
        node = nodes.audio(**attributes)
        return [
            node,
        ]


class AudioRole(SphinxRole):  # noqa: D101
    def run(self):  # noqa: D102
        options = {
            "uri": directives.uri(self.text),
            "controls": True,
        }
        node = nodes.audio(**options)
        return [node], []


def setup(app: Sphinx):  # noqa: D103
    app.add_node(nodes.audio, html=(nodes.visit_audio, nodes.depart_audio))
    app.add_directive("audio", AudioDirective)
    app.add_role("audio", AudioRole())
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
