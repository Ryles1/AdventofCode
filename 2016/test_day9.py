import pytest
import day9


@pytest.mark.parametrize("examples2, answers2", [
    ("(3x3)XYZ", 9),
    ("X(8x2)(3x3)ABCY", 20),
    ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
    ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445)
])
def test_decompress2(examples2, answers2):
    assert day9.decompress2(examples2) == answers2


@pytest.mark.parametrize("examples1, answers1", [
    ("ADVENT", 6),
    ("A(1x5)BC", 7),
    ("(3x3)XYZ", 9),
    ("A(2x2)BCD(2x2)EFG", 11),
    ("(6x1)(1x3)A", 6),
    ("X(8x2)(3x3)ABCY", 18)
])
def test_decompress1(examples1, answers1):
    assert day9.decompress1(examples1) == answers1


