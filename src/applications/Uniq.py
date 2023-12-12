from .Application import Application
from itertools import groupby


class Uniq(Application):
    """
        uniq application outputs the unique lines in a file/stdin
        example:
            uniq uniq_testing.txt
            uniq -i uniq_testing.txt
            uniq < uniq_testing.txt
    """
    def exec(self):
        if len(self.args) == 0:
            raise ValueError("uniq requires at least one argument")
        else:
            uniq_content = []
            ignore_case = False

            if self.args[0] == '-i':
                ignore_case = True
                self.args.pop(0)
            file = self.args[0]

            try:
                lines = self._read_lines(file)
                for line in lines:
                    line = line.strip()
                    if line == '':
                        continue
                    if ignore_case:
                        line = line.upper()
                    uniq_content.append(line)
            except Exception:
                raise FileNotFoundError(f"File not found: {file}")

            uniq_content = self.deduplicate_adjacent_lines(uniq_content)
            self.output.extend([line + '\n' for line in uniq_content])

    def deduplicate_adjacent_lines(self, lines):
        deduplicated_lines = [key for key, _ in groupby(lines)]
        return deduplicated_lines
