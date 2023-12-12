from applications.Application import Application

'''
    cat application read all contents of a file and add them to self.output
    example:
        cat requirements.txt
'''


class Cat(Application):
    def exec(self):
        for a in self.args:
            try:
                lines = self._read_lines(a)
                for line in lines:
                    self.output.append(line + '\n')
            except Exception:
                raise FileNotFoundError(f"File not found: {a}")
        # print(self.output)
