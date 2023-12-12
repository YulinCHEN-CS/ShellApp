from factories.SpecialArgs import SpecialArgs
from .Application import Application


class Echo(Application):
    """
        echo application outputs teh arguments inputed
        example:
            echo "hello world"
            echo hello
    """
    def exec(self):
        output = []
        for arg in self.args:
            if isinstance(arg, SpecialArgs):
                # if len(arg.get_parsed_args()) > 0:
                for parsed_arg in arg.get_parsed_args():
                    output.append(parsed_arg)
            else:
                if arg != "":
                    output.extend(arg.splitlines())
        if len(output) > 0:
            self.output.append(" ".join(output))
