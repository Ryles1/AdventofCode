import pytest
import day1


@pytest.mark.parametrize('examples1, answers1', [
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9)
])



def test_main(examples1, answers1):
    assert day1.main(examples1, 1) == answers1



