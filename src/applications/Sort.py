from .Application import Application


class Sort(Application):
    """
        Sorts application sorts the contents of a file/stdin line
        by line and prints the result to stdout.
        example:
            sort sort_testing.txt
            sort -r sort_testing.txt
            sort < sort_testing.txt
    """

    def exec(self):
        reverse = False
        file_name = ''
        if len(self.args) == 1:
            file_name = self.args[0]
        elif len(self.args) == 2 and self.args[0] == '-r':
            reverse = True
            file_name = self.args[1]
        else:
            raise ValueError("Incorrect number of "
                             "command line arguments or flags")
        try:
            lines = self._read_lines(file_name)
        except Exception:
            raise FileNotFoundError("File not found")
        sorted_lines = sorted(lines, reverse=reverse)
        for line in sorted_lines:
            self.output.append(line + '\n')
