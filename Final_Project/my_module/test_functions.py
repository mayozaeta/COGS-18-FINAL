"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from test_functions import exit_func

##
##

def test_my_func():

    assert my_func() == None

def test_my_other_func():

    assert my_other_func() == None



def exit_func(str):
    """ return a string
    parameter
    ----------
    there is a singular parameter and it is an input string value
    return
    ---------
    function returns the string inputs
    """
    output = str
    return output


assert exit_func  # tests if variable exists  
assert isinstance(exit_func, str)  # tests that variable is string type 
assert exit_func("hello") == "hello"  # tests functions output
assert exit_func("") == ""
