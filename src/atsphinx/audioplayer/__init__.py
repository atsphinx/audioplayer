"""Register directive to render audio element."""

from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.directives import SphinxDirective
from sphinx.util.docutils import SphinxRole

from . import nodes

__version__ = "0.0.0"


class DataPrefixOptions(dict):
    def __getitem__(self, key):
        """Extend dict for custom plugins of revealjs.

        Many plugins may refer ``data-`` attributes
        of ``section`` elements as optional behaviors.
        """
        if key in self:
            return super().__getitem__(key)
        if key.startswith("data-"):
            return directives.unchanged
        return None


class AudioDirective(SphinxDirective):  # noqa: D101
    required_arguments = 1
    option_spec = DataPrefixOptions(
        **{
            "no-controls": directives.flag,
        }
    )

    def run(self):  # noqa: D102
        attributes = {
            "uri": directives.uri(self.arguments[0]),
            "controls": "no-controls" not in self.options,
            "data": {
                k: v or k for k, v in self.options.items() if k.startswith("data-")
            },
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
            "data": {},
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
