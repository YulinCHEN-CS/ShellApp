from antlr4 import InputStream, CommonTokenStream
from antlr.generated.ShellGrammarLexer import ShellGrammarLexer
from antlr.generated.ShellGrammarParser import ShellGrammarParser

"""
    This factory takes in a string and a visitor instance
    and returns the output of the command
    @:param input_str(STRING): The input string
    @:param visitor(SHELLGRAMMARVISITOR): The visitor instance
    @:return output(DEQUEUE): The output of the command
    @:raise Exception: catch the exception from eval() method of the command
"""


def input_factory(input_str, visitor):
    input_stream = InputStream(input_str)
    lexer = ShellGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ShellGrammarParser(stream)
    tree = parser.command()

    # convert the parse tree to a command using Converter()
    command = tree.accept(visitor)
    # try:
    command.eval()
    # except Exception as e:
    #     print(f"Error: {e}")
    return command.output
