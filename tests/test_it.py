"""Standard tests."""

from io import StringIO

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""
    app.build()
    soup = BeautifulSoup((app.outdir / "index.html").read_text(), "html.parser")
    assert soup.audio
    assert soup.audio["src"] == "_images/dummy.mp3"
