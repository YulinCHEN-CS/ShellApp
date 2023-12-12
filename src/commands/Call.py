from .Command import Command
from factories.application_factory import application_factory
from factories.SpecialArgs import SpecialArgs

'''
    Call command class call all the applications including decorators
    The specific application is determined by the application_factory method
'''


class Call(Command):

    """
        Constructor
        @:param app(STRING) is application name entered by user
        (different from the class name, class name has first letter
        capitalized)
        @:param args(LIST) is the list of arguments passed to the application
        @:param input_redir(STRING) is the input redirection filename
        @:param output_redir(STRING) is the output redirection filename
    """

    def __init__(self, app, args, input_redir, output_redir):
        super().__init__()
        self.args = args
        self.app = app
        self.input_redir = input_redir
        self.output_redir = output_redir
        self.unsafe = False

    '''
        Evaluate the command lines
            + Do the redirection if needed
            + Call the application and grab the output
    '''
    # evaluate running results
    def eval(self):
        # Debugging: Print the apps and the type of apps
        # print("Type of self.app:", self.app)
        if self.input_redir:
            try:
                input_redir = SpecialArgs()
                input_redir.parse_args_redirection(self.input_redir)
                self.args.append(input_redir)
            except Exception:
                raise FileNotFoundError(
                    f"Error: File not found: {self.input_redir}"
                )

        if self.app.startswith("_"):
            self.unsafe = True
            self.app = self.app[1:]

        self.app = application_factory(self.app, self.args, self.output)
        # print("Type of self.app:", type(self.app))
        # print(f"slef.app: {self.app}, self.args: {self.args}")
        try:
            self.app.exec()
        except Exception as e:
            if self.unsafe:
                self.output.append(f"Error: {e}")
            else:
                raise e

        if len(self.app.output) > 0:
            if self.output_redir:
                with open(self.output_redir, "w") as f:
                    self.app.output[-1] = self.app.output[-1].rstrip('\n')
                    while self.app.output:
                        f.write(self.app.output.popleft())
                return
            if not self.app.output[-1].endswith("\n"):
                self.app.output.append("\n")
            self.output = self.app.output
