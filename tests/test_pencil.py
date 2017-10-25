import pytest

from pencil import Pencil


@pytest.mark.fixture
def pencil():
    return Pencil()


def test_pencil_writes_to_paper(pencil):
    pencil.write("She sells sea shells")
    assert pencil.paper == "She sells sea shells"


def test_pencil_writes_to_paper_twice(pencil):
    pencil.write("She sells sea shells")
    pencil.write(" down by the sea shore")
    assert pencil.paper == "She sells sea shells down by the sea shore"
