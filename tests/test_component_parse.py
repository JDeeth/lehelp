from component import parse_components, SATURN, JUNO, PROBE


def test_parse_single_component():
    test_str = "Probe"
    assert parse_components(test_str) == [PROBE]


def test_parse_multiple_components():
    test_str = "Juno, Probe"
    assert parse_components(test_str) == [JUNO, PROBE]


def test_parse_x3_syntax():
    test_str = "Saturn x2, Juno x4, Probe"
    assert parse_components(test_str) == [SATURN, SATURN, JUNO, JUNO, JUNO, JUNO, PROBE]
