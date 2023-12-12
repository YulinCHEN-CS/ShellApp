from abc import ABC, abstractmethod

from factories.SpecialArgs import SpecialArgs

'''
    Application is an interface that represents a command line application.
'''


class Application(ABC):

    """
        Constructor
        @:param args is a list of arguments passed to the application
        @:param output is a deque that stores the output of the application
    """
    def __init__(self, args, output):
        self.args = args
        self.output = output

    '''
        @:method exec()
        + need to be implemented by the child class
        + takes no input and appends all outputs to self.output
    '''
    @abstractmethod
    def exec(self):
        pass

    def _read_lines(self, file_name):
        if isinstance(file_name, SpecialArgs):
            return file_name.get_parsed_args()
        else:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                return [line.rstrip('\n') for line in lines]
