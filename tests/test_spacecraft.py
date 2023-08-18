from spacecraft import Spacecraft


def test_empty():
    sc = Spacecraft()
    assert sc.mass == 0
    assert sc.cost == 0


def test_one_comp():
    sc = Spacecraft.from_str("Aldrin")
    assert sc.mass == 3
    assert sc.cost == 4


def test_multi_comp():
    sc = Spacecraft.from_str("Juno, Probe")
    assert sc.mass == 2
    assert sc.cost == 3


def test_repeat_comp():
    sc = Spacecraft.from_str("Saturn x2, Juno x4, Probe")
    assert sc.mass == 45
    assert sc.cost == 36
