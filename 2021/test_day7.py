import pytest
import day7


@pytest.fixture()
def example_input():
	l = [16,1,2,0,4,2,7,1,2,14]
	return l

@pytest.mark.skip
def test_calc_fuel_constant_rate(example_input):
	assert day7.calc_fuel_constant_rate(example_input, 2) == 37
	assert day7.calc_fuel_constant_rate(example_input, 1) == 41
	assert day7.calc_fuel_constant_rate(example_input, 10) == 71


def test_calc_fuel_linear_rate(example_input):
	assert day7.calc_fuel_linear_rate(example_input, 2) == 206
	assert day7.calc_fuel_linear_rate(example_input, 5) == 168


def test_align_crabs(example_input):
	assert day7.align_crabs(example_input, 'linear') == 168