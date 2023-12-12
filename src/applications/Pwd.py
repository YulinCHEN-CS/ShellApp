from .Application import Application
import os


class Pwd(Application):
    """
        pwd application prints the present working directory
        example:
            pwd
    """
    def exec(self):
        self.output.append(os.getcwd() + "\n")
