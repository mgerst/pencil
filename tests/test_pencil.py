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
    assert pencil.durability == Pencil.DEFAULT_DURABILTY - 4


def test_writing_caps_decreases_durability_by_2(pencil):
    pencil.write("Text")
    assert pencil.durability == Pencil.DEFAULT_DURABILTY - 5


def test_writing_space_doesnt_degrade(pencil):
    pencil.write("value with spaces")
    assert pencil.durability == Pencil.DEFAULT_DURABILTY - 15


def test_writing_newline_doesnt_degrade(pencil):
    pencil.write("value with\nnewline")
    assert pencil.durability == Pencil.DEFAULT_DURABILTY - 16


def test_writing_past_durability_writes_space(pencil):
    text = "a" * (Pencil.DEFAULT_DURABILTY + 1)
    pencil.write(text)
    assert pencil.durability == 0
    assert pencil.paper[-1] == " " and pencil.paper[-2] == "a"


def test_sharpen_resets_durabilty(pencil):
    pencil.write("text")
    pencil.sharpen()
    assert pencil.durability == pencil.starting_durability
