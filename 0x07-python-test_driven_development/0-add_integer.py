#!/usr/bin/python3
def add_integer(a, b=98):
    """add functione:
    That return the result in type ineteger if type of
    argumentareinteger or float else it will raise a typeerror
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
