#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    """this is for operators inverted"""
    def __eq__(self, num):
        """return True if not equal operators passed"""
        return not super().__eq__(num)

    def __ne__(self, num):
        """return False if equal operators passed"""
        return not super().__ne__(num)
