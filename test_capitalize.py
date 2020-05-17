# test_capitalize.py

import pytest

def capital_case(x):
	if not isinstance(x, str):
		raise TypeError('Please provided a string argument')
	return x.capitalize()

def test_capitalize():
	assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
	with pytest.raises(TypeError):
		capital_case(9)
