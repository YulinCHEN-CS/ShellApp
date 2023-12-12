from collections import deque
from abc import abstractmethod, ABC


'''
    Command interface
    Each command has an unique output stored in a deque
    @:method eval()
        + evaluate the command lines
'''


class Command(ABC):

    """
        Constructor
        @:var output(DEQUE): defined a unique queue for each command
    """
    @abstractmethod
    def __init__(self):
        self.output = deque()

    @abstractmethod
    def eval(self):
        pass
