import pytest
import day6


@pytest.mark.parametrize('examples1, answers1', [
    ([0,2,7,0], 5)
])



def test_main(examples1, answers1):
    assert day6.main(examples1) == answers1
