from factories.SpecialArgs import SpecialArgs
from .Application import Application
import os


class Ls(Application):
    """
        ls application lists all the files in the current directory
        example:
            ls
            ls src
    """

    def exec(self):
        path = self.args[0] if self.args else '.'
        try:
            # When the input is a directory
            entries = os.listdir(path)
            for entry in sorted(entries):  # Sort the list of entries
                self.output.append(entry + "\n")
        except Exception:
            if isinstance(path, SpecialArgs):
                lines = path.get_parsed_args()
                for line in lines:
                    self.output.append(line + "\n")
            else:
                raise FileNotFoundError(f"Directory not found: {path}")
