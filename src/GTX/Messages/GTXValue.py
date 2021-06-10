from enum import Enum

class GTXValuechoice(enum):
    NotSet = -1
    Null = 0
    ByteArray = 1
    String = 2
    Integer = 3
    Dict = 4
    Array = 5

"""
Not quite sure if this is needed, will leave it for now.
"""
class GTXValue:

    def __init__(self):
        self.Choice = GTXValuechoice.NotSet
