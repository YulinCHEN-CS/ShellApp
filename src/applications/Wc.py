from .Application import Application


class Wc(Application):
    """
        Wc application counts the number of lines, words, and characters
        in a file
        example:
            wc src/commands/Command.py
            wc src/commands/Command.py src/commands/CommandFactory.py
    """
    def exec(self):
        line_only = '-l' in self.args
        if line_only:
            # Remove '-l' from arguments
            self.args.remove('-l')

        # Flatten and split the arguments if they are
        # the result of command substitution
        flattened_args = []
        for arg in self.args:
            flattened_args.extend(arg.split())

        for filename in flattened_args:
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    lines = content.splitlines()

                    line_count = len(lines)

                    if line_only:
                        self.output.append(f"{line_count} {filename}\n")
                    else:
                        words = content.split()
                        characters = len(content)

                        word_count = len(words)
                        character_count = characters

                        self.output.append(f"{line_count} {word_count} "
                                           f"{character_count} {filename}\n")
            except FileNotFoundError:
                print(f"File not found: {filename}")
            except Exception as e:
                print(f"Error reading file {filename}: {str(e)}")
