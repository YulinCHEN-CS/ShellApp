from .Command import Command
from factories.SpecialArgs import SpecialArgs
'''
    Pipe command class
        + Use the output of the left command as input of the right command
'''


class Pipe(Command):
    """
        Constructor
        @:param left_command(COMMAND) is the left command of the pipe
        @:param right_command(COMMAND) is the right command of the pipe
    """
    def __init__(self, left_command, right_command):
        super().__init__()
        self.left_command = left_command
        self.right_command = right_command

    '''
        Evaluate the command lines
            + Execute the left command
            + Removed the newline character at the end of the
              output of the left command if any
            + Pass the output of the left command as input to the right command
            + Execute the right command
            + Set the output of the Pipe command to be the output of the
              right command
    '''
    def eval(self):
        # Execute the left command
        self.left_command.eval()
        left_output = SpecialArgs()
        left_output.parse_args_pipe(self.left_command.output)
        # Pass the output of the left command as input to the right command
        if isinstance(self.right_command, Pipe):
            self.right_command.left_command.args.append(left_output)
        else:
            self.right_command.args.append(left_output)
        # print("right_command.args: ", self.right_command.args)
        self.right_command.eval()

        # Set the output of the Pipe command to be
        # the output of the right command
        self.output = self.right_command.output
