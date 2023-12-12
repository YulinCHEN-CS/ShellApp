from .Application import Application


class Head(Application):
    """
        head application read head n lines of a file
        Example:
            head requirements.txt
            head -n 2 requirements.txt
    """
    def exec(self):
        # Set default number of lines
        num_lines = 10
        file_paths = []

        # Handle arguments
        if len(self.args) == 1:
            file_paths.append(self.args[0])
        elif (len(self.args) >= 3 and self.args[0] == "-n" and
              int(self.args[1]) >= 0):
            num_lines = int(self.args[1])
            file_paths = self.args[2:]
        else:
            raise ValueError("Incorrect number of command line "
                             "arguments or flags")

        # Read the file and output the specified number of lines
        for file in file_paths:
            try:
                lines = self._read_lines(file)
                for i, line in enumerate(lines):
                    if i < num_lines:
                        self.output.append(line + '\n')
                    else:
                        break
            except Exception:
                raise FileNotFoundError(f"File not found: {file}")
