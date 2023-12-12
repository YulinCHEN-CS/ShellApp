from .Command import Command

'''
    Sequential command class
'''


class Seq(Command):

    """
        Constructor
        @:param commands(LIST): list of commands to be executed sequentially
    """
    def __init__(self, commands):
        super().__init__()
        self.commands = commands

    '''
        execute the commands sequentially and append the output to the output
        deque
    '''
    def eval(self):
        for command in self.commands:
            command.eval()
            self.output.extend(command.output)
