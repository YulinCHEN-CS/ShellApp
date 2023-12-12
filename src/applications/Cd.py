import os
from .Application import Application


class Cd(Application):
    """
        cd application does the change directory operation
        example:
            cd ..
            cd sys
    """
    def exec(self):
        if len(self.args) != 1:
            raise ValueError("cd requires exactly one argument")
        try:
            os.chdir(self.args[0])
        except FileNotFoundError:
            raise FileNotFoundError("Directory not found")
