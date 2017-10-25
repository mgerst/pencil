from pencil import Pencil


def test_pencil_writes_to_paper():
    pencil = Pencil()
    pencil.write("She sells sea shells")
    assert pencil.paper == "She sells sea shells"


def test_pencil_writes_to_paper_twice():
    pencil = Pencil()
    pencil.write("She sells sea shells")
    pencil.write(" down by the sea shore")
    assert pencil.paper == "She sells sea shells down by the sea shore"
