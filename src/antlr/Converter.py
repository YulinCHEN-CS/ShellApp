from factories.input_factory import input_factory
from antlr.generated.ShellGrammarParser import ShellGrammarParser
from antlr.generated.ShellGrammarVisitor import ShellGrammarVisitor
from commands.Call import Call
from commands.Pipe import Pipe
from commands.Seq import Seq
from factories.SpecialArgs import SpecialArgs

'''
    self-defined visitor class inherited from ShellGrammarVisitor
    Detailed patterns regards to Call, Pipe and Seq
    are defined in ShellGrammmar.g4
'''


class Converter(ShellGrammarVisitor):
    def __init__(self):
        super().__init__()

    '''
        visit single quoted string
            + remove the single quotes
        @:return string processed
    '''
    def visitSingle_quoted(
            self,
            ctx: ShellGrammarParser.Single_quotedContext
    ):
        return ctx.getText()[1:-1]

    '''
        visit back quoted string
            + execute the command inside the back quotes and replace
            + remove the back quotes
        @:return string processed
    '''
    def visitBack_quoted(
            self,
            ctx: ShellGrammarParser.Back_quotedContext
    ):
        input_command = ""
        for child in ctx.children[1:-1]:
            input_command += child.getText()
        output = input_factory(input_command, Converter())
        if len(output) == 0:
            return ""
        output[-1] = output[-1].rstrip('\n')
        output_str = ''.join(map(str, output))
        return output_str

    '''
        visit double quoted string
            + remove the double quotes
            + visit the back quoted string and process
        @:return string processed
    '''
    def visitDouble_quoted(
            self,
            ctx: ShellGrammarParser.Double_quotedContext
    ):
        result = ""
        for child in ctx.children:
            if isinstance(child, ShellGrammarParser.Back_quotedContext):
                result += self.visit(child)
            else:
                result += child.getText()
        return result[1:-1]

    '''
        visit left redirection (<)
        @:return visiting the argument part (input filename)
    '''
    def visitLeft_redirection(
            self,
            ctx: ShellGrammarParser.Left_redirectionContext
    ):
        return self.visit(ctx.arg())

    '''
        visit right redirection (>)
        @:return visiting the argument part (output filename)
    '''
    def visitRight_redirection(
            self,
            ctx: ShellGrammarParser.Right_redirectionContext
    ):
        return self.visit(ctx.arg())

    '''
        visit redirection
        @:return flag('>' or '<') and redirection filename
    '''
    def visitRedirection(
            self,
            ctx: ShellGrammarParser.RedirectionContext
    ):
        flag, content = None, None
        if ctx.left_redirection():
            flag = "<"
            content = self.visit(ctx.left_redirection())
        if ctx.right_redirection():
            flag = ">"
            content = self.visit(ctx.right_redirection())
        return flag, ''.join(map(str, content))

    '''
        visit argument
            + skip whitespace
            + do the globbing (The glob terms are connected by '\n' to
              maintain the consistency of the args,
              since pipe returns a string containing outputs from left command,
              including '\n')
            + visit quoted string and process
        @:return list of arguments
    '''
    def visitArg(
            self,
            ctx: ShellGrammarParser.ArgContext
    ):
        arg = ""
        args = []
        for child in ctx.children:
            if isinstance(child, ShellGrammarParser.QuotedContext):
                arg_text = self.visit(child)
            else:
                arg_text = child.getText()
                if " " in arg_text:
                    args.extend(arg.splitlines())
                    arg = ""
                    continue
            # Check for globbing patterns
            if '*' in arg_text or '?' in arg_text:
                # print(f"Globbing pattern found:", arg_text, end="")
                # If the globbing pattern is valid, add a Globbing object
                glob = SpecialArgs()
                arg_text = arg_text.replace('?', '*')
                if glob.parse_args_globbing(arg_text):
                    args.append(glob)
                    continue
            arg += arg_text
        if arg != "":
            args.extend(arg.splitlines())
        # print(args)
        return args

    '''
        visit call
            + visit argument
            + visit redirection
        @:exception if multiple redirections used
        @:return Call object
    '''
    def visitCall(
            self,
            ctx: ShellGrammarParser.CallContext
    ):
        appName = None
        args_excl_appName = None
        input_redir = None
        output_redir = None
        for child in ctx.children:
            if isinstance(child, ShellGrammarParser.ArgContext):
                args = self.visit(child)
                appName = args[0]
                args_excl_appName = args[1:]
            elif isinstance(child, ShellGrammarParser.RedirectionContext):
                flag, content = self.visit(child)
                if flag == "<":
                    if input_redir:
                        raise ValueError("Multiple < redirections")
                    input_redir = content
                else:
                    if output_redir:
                        raise ValueError("Multiple > redirections")
                    output_redir = content
        return Call(appName, args_excl_appName, input_redir, output_redir)

    '''
        visit pipe
            + visit left command
            + visit right command
        @:return Pipe object
    '''
    def visitPipe(
            self,
            ctx: ShellGrammarParser.PipeContext
    ):
        left_command = self.visit(ctx.children[0])
        right_command = self.visit(ctx.children[2])
        return Pipe(left_command, right_command)

    '''
    visit subcommand
        + visit call
        + visit pipe
    @:return Seq object
    '''
    def visitCommand(
            self,
            ctx: ShellGrammarParser.CommandContext
    ):
        commands = []
        for child in ctx.children:
            if isinstance(child, ShellGrammarParser.SubCommandContext):
                commands.append(self.visit(child))
        return Seq(commands)
