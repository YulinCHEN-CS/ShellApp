import re

from .Application import Application


class Grep(Application):
    """
        Greps application outputs the lines that match the pattern
        example:
            grep "hello" grep_testing.txt
            grep "python" < comp0010/requirements.txt > comp0010/test_redir.txt
    """
    def exec(self):
        if len(self.args) < 2:
            raise ValueError("Wrong number of command line arguments")

        single_file = len(self.args) == 2
        pattern, file_names = self.args[0], self.args[1:]

        pattern_found = False
        for file_name in file_names:
            try:
                lines = self._read_lines(file_name)

                file_pattern_found = False
                for line in lines:
                    if re.search(pattern, line):
                        file_pattern_found = True
                        output_line = line if single_file else \
                            f"{file_name}:{line}"
                        self.output.append(output_line + '\n')

                pattern_found = pattern_found or file_pattern_found
            except FileNotFoundError:
                raise FileNotFoundError(f"File not found: {file_name}")

        if not pattern_found:
            raise ValueError(f"Pattern '{pattern}' not found in "
                             f"file {file_name}")
