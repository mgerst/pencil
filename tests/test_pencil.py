from pencil import Pencil


def test_pencil_writes_to_paper():
    pencil = Pencil()
    pencil.write("She sells sea shells")
    assert pencil.paper == "She sells sea shells"
