"""Standard tests."""

from io import StringIO

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__directive(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""
    app.build()
    soup = BeautifulSoup((app.outdir / "index.html").read_text(), "html.parser")
    assert soup.audio
    assert soup.audio["src"] == "_images/dummy.mp3"
    assert soup.audio["controls"]


@pytest.mark.sphinx("html")
def test__domain(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""
    app.build()
    soup = BeautifulSoup((app.outdir / "use-domain.html").read_text(), "html.parser")
    assert soup.audio
    assert soup.audio["src"] == "_images/dummy.mp3"
    assert soup.audio["controls"]


@pytest.mark.sphinx("html")
def test__http_url(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""
    app.build()
    soup = BeautifulSoup((app.outdir / "http-url.html").read_text(), "html.parser")
    assert soup.audio
    assert (
        soup.audio["src"]
        == "https://github.com/atsphinx/audioplayer/raw/main/tests/test-root/dummy.mp3"
    )
    assert soup.audio["controls"]
