import fnmatch
import os
from .Application import Application
from factories.SpecialArgs import SpecialArgs


class Find(Application):
    def exec(self):
        """
            find application finds the files that match the pattern
            Example:
                find . -name '*.txt'
                find src -name '*.py'
                find non_existent -name '*.txt'

            Cases:  # with and without directory
                1) ['-name', '*.txt']
                2) ['comp0010', '-name', '*.txt']
        """

        # Default values
        directory = '.'  # Start search in the current directory
        pattern = None  # Pattern to match

        if len(self.args) == 2 and self.args[0] == '-name':
            pattern = self.args[-1].og_args \
                if isinstance(self.args[-1], SpecialArgs) else self.args[-1]
            pattern = pattern.strip("'\"")

        elif len(self.args) == 3 and self.args[1] == '-name':
            directory = self.args[0]

            if not os.path.isdir(directory):
                raise FileNotFoundError(f"Directory not found: {directory}")

            pattern = self.args[-1].og_args \
                if isinstance(self.args[-1], SpecialArgs) else self.args[-1]

        else:
            raise ValueError("Usage: find [PATH] -name 'PATTERN'")

        # Walk through the directory and match files
        for root, dirs, files in os.walk(directory):
            for filename in fnmatch.filter(files, pattern):
                # Construct the relative path
                relative_path = os.path.relpath(
                    os.path.join(root, filename), start=directory)
                self.output.append(directory + "/" + relative_path + "\n")
