import pytest

from pencil import Pencil


@pytest.fixture
def pencil():
    return Pencil()


def test_pencil_writes_to_paper(pencil):
    pencil.write("She sells sea shells")
    assert pencil.paper == "She sells sea shells"


def test_pencil_writes_to_paper_twice(pencil):
    pencil.write("She sells sea shells")
    pencil.write(" down by the sea shore")
    assert pencil.paper == "She sells sea shells down by the sea shore"


def test_writing_decreases_durability(pencil):
    pencil.write("text")
    # Starting point is 50
    assert pencil.durability == 50 - 4


def test_writing_caps_decreases_durability_by_2(pencil):
    pencil.write("Text")
    # Starting point is 50
    assert pencil.durability == 50 - 5


def test_writing_space_doesnt_degrade(pencil):
    pencil.write("value with spaces")
    assert pencil.durability == 50 - 15


def test_writing_newline_doesnt_degrade(pencil):
    pencil.write("value with\nnewline")
    assert pencil.durability == 50 - 16
