import pytest

from calc.ops import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-5, 5, 0),
    (0, 0, 2)
])
def test_add(a, b, expected):
    assert add(a, b) == expected