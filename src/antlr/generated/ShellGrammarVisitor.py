# Generated from src/antlr/ShellGrammar.g4
# ANTLR 4.13.1
from antlr4 import ParseTreeVisitor
from .ShellGrammarParser import ShellGrammarParser


# This class defines a complete generic visitor for
# a parse tree produced by ShellGrammarParser.

class ShellGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShellGrammarParser#command.
    def visitCommand(self, ctx: ShellGrammarParser.CommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#subCommand.
    def visitSubCommand(self, ctx: ShellGrammarParser.SubCommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#call.
    def visitCall(self, ctx: ShellGrammarParser.CallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#pipe.
    def visitPipe(self, ctx: ShellGrammarParser.PipeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#arg.
    def visitArg(self, ctx: ShellGrammarParser.ArgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#redirection.
    def visitRedirection(self, ctx: ShellGrammarParser.RedirectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#left_redirection.
    def visitLeft_redirection(
            self,
            ctx: ShellGrammarParser.Left_redirectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#right_redirection.
    def visitRight_redirection(
            self,
            ctx: ShellGrammarParser.Right_redirectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#quoted.
    def visitQuoted(self, ctx: ShellGrammarParser.QuotedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#single_quoted.
    def visitSingle_quoted(self, ctx: ShellGrammarParser.Single_quotedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#back_quoted.
    def visitBack_quoted(self, ctx: ShellGrammarParser.Back_quotedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShellGrammarParser#double_quoted.
    def visitDouble_quoted(self, ctx: ShellGrammarParser.Double_quotedContext):
        return self.visitChildren(ctx)


del ShellGrammarParser
