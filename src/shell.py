# Import ANTLR runtime and generated parser/lexer classes here
import os
import sys
import readline

from factories.input_factory import input_factory
from antlr.Converter import Converter


'''
    Main shell class that runs the shell
'''


class Shell:

    """
        Set up command history file to support up/down arrow key
    """
    def setup_readline(self):
        # Set up command history file
        history_file = 'comp0010-shell-python-p46/history_file.txt'
        try:
            readline.read_history_file(history_file)
            readline.set_history_length(1000)
        except FileNotFoundError:
            pass

    # def process_command(self, command):
    #     """Process a shell command and return the output with a newline."""
    #     output = input_factory(command, Converter())
    #     if output and not output[-1].endswith('\n'):
    #         output[-1] += '\n'  # Ensure last output line ends with a newline
    #     return output
    #
    # def eval(self, command, out):
    #     """Evaluate a shell command and store the output in a deque."""
    #     shell = Shell()
    #     result = shell.process_command(command)
    #     while result:
    #         out.append(result.popleft())

    """
        Run the shell and print output
    """
    def run(self):
        args_num = len(sys.argv) - 1
        if args_num > 0:
            if args_num != 2:
                raise ValueError("wrong number of command line arguments")
            if sys.argv[1] != "-c":
                raise ValueError(f"unexpected command line argument "
                                 f"{sys.argv[1]}")
            output = input_factory(sys.argv[2], Converter())
            while output:
                print(output.popleft(), end="")
        else:
            self.setup_readline()
            while True:
                try:
                    input_str = input(os.getcwd() + " > ")
                    output = input_factory(input_str, Converter())
                    while output:
                        print(output.popleft(), end="")
                except (EOFError, KeyboardInterrupt):
                    break


if __name__ == '__main__':
    shell = Shell()
    shell.run()
