import glob


'''
    SpecialArgs class handles the arguments passing after globbing,
    redirection, and pipe
'''


class SpecialArgs:
    """
    Constructor
        @:param og_args(STRING is the original argument
        @:param parsed_args(LIST) is the list of parsed arguments,
                each element is a string and newline removed if any
    """
    def __init__(self):
        self.og_args = None
        self.parsed_args = []

    '''
        parse the arguments after pipe
            + removed each newline character at the end of
              each line if any to keep consistency
        @:param args(LIST) is the list of arguments passed after pipe
    '''

    def parse_args_pipe(self, args):
        while args:
            arg = args.popleft()
            if arg.endswith('\n'):
                arg = arg[:-1]
            self.parsed_args.append(arg)

    '''
        parse the arguments after redirection
            + removed each newline character at the end of
              each line if any to keep consistency
        @:param input_redir(STRING) is the input redirection filename
    '''
    def parse_args_redirection(self, input_redir):
        with open(input_redir) as f:
            content = f.read()
            lines = content.splitlines()
            self.parsed_args = lines

    '''
        parse the arguments after globbing
        @:param arg(STRING) is the argument to be parsed
        @:return True if the argument can be expand, False otherwise
    '''
    def parse_args_globbing(self, arg):
        self.og_args = arg
        expansion = glob.glob(arg)
        # print(f"expansion:{expansion} of args:{arg}: ")
        if expansion:
            self.parsed_args = expansion
            return True
        return False

    '''
        get the parsed arguments
        @:return parsed_args(LIST) is the list of parsed arguments
    '''
    def get_parsed_args(self):
        # print("parsed_args: ", self.parsed_args)
        return self.parsed_args
