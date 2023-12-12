# Generated from src/antlr/ShellGrammar.g4
# ANTLR 4.13.1
from antlr4 import Parser, ATNDeserializer, DFA, PredictionContextCache, \
    TokenStream, ParserATNSimulator, ParserRuleContext, ParseTreeVisitor, \
    RecognitionException, Token, ATN, NoViableAltException
import sys
from typing import TextIO
# if sys.version_info[1] > 5:
# 	from typing import TextIO
# else:
# 	from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 10, 129, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2,
        7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10,
        7, 10, 2, 11, 7, 11, 1, 0, 1, 0, 1, 0, 5, 0, 28,
        8, 0, 10, 0, 12, 0, 31, 9, 0, 1, 1, 1, 1, 3,
        1, 35, 8, 1, 1, 2, 3, 2, 38, 8, 2, 1, 2, 1, 2, 3,
        2, 42, 8, 2, 5, 2, 44, 8, 2, 10, 2, 12, 2,
        47, 9, 2, 1, 2, 1, 2, 1, 2, 3, 2, 52, 8, 2, 5, 2,
        54, 8, 2, 10, 2, 12, 2, 57, 9, 2, 1, 3, 1, 3, 1,
        3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 3, 3, 67, 8,
        3, 1, 4, 1, 4, 3, 4, 71, 8, 4, 1, 4, 3, 4, 74,
        8, 4, 4, 4, 76, 8, 4, 11, 4, 12, 4, 77, 1, 5,
        1, 5, 3, 5, 82, 8, 5, 1, 6, 1, 6, 3, 6, 86, 8,
        6, 1, 6, 1, 6, 1, 7, 1, 7, 3, 7, 92, 8, 7, 1, 7,
        1, 7, 1, 8, 1, 8, 1, 8, 3, 8, 99, 8, 8, 1, 9, 1,
        9, 5, 9, 103, 8, 9, 10, 9, 12, 9, 106, 9, 9,
        1, 9, 1, 9, 1, 10, 1, 10, 5, 10, 112, 8, 10, 10,
        10, 12, 10, 115, 9, 10, 1, 10, 1, 10, 1,
        11, 1, 11, 1, 11, 5, 11, 122, 8, 11, 10, 11,
        12, 11, 125, 9, 11, 1, 11, 1, 11, 1, 11, 0,
        0, 12, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
        22, 0, 3, 2, 0, 1, 1, 9, 9, 2, 0, 3, 3, 9, 9,
        2, 0, 2, 2, 9, 9, 136, 0, 24, 1, 0, 0, 0, 2,
        34, 1, 0, 0, 0, 4, 37, 1, 0, 0, 0, 6, 66, 1, 0,
        0, 0, 8, 75, 1, 0, 0, 0, 10, 81, 1, 0, 0, 0,
        12, 83, 1, 0, 0, 0, 14, 89, 1, 0, 0, 0, 16, 98,
        1, 0, 0, 0, 18, 100, 1, 0, 0, 0, 20, 109, 1,
        0, 0, 0, 22, 118, 1, 0, 0, 0, 24, 29, 3, 2, 1,
        0, 25, 26, 5, 6, 0, 0, 26, 28, 3, 2, 1, 0,
        27, 25, 1, 0, 0, 0, 28, 31, 1, 0, 0, 0, 29, 27,
        1, 0, 0, 0, 29, 30, 1, 0, 0, 0, 30, 1, 1, 0,
        0, 0, 31, 29, 1, 0, 0, 0, 32, 35, 3, 6, 3, 0, 33,
        35, 3, 4, 2, 0, 34, 32, 1, 0, 0, 0, 34, 33,
        1, 0, 0, 0, 35, 3, 1, 0, 0, 0, 36, 38, 5, 10, 0,
        0, 37, 36, 1, 0, 0, 0, 37, 38, 1, 0, 0, 0, 38,
        45, 1, 0, 0, 0, 39, 41, 3, 10, 5, 0, 40, 42,
        5, 10, 0, 0, 41, 40, 1, 0, 0, 0, 41, 42, 1, 0,
        0, 0, 42, 44, 1, 0, 0, 0, 43, 39, 1, 0, 0, 0,
        44, 47, 1, 0, 0, 0, 45, 43, 1, 0, 0, 0, 45, 46,
        1, 0, 0, 0, 46, 48, 1, 0, 0, 0, 47, 45, 1,
        0, 0, 0, 48, 55, 3, 8, 4, 0, 49, 51, 3, 10,
        5, 0, 50, 52, 5, 10, 0, 0, 51, 50, 1, 0, 0, 0,
        51, 52, 1, 0, 0, 0, 52, 54, 1, 0, 0, 0, 53,
        49, 1, 0, 0, 0, 54, 57, 1, 0, 0, 0, 55, 53, 1,
        0, 0, 0, 55, 56, 1, 0, 0, 0, 56, 5, 1, 0, 0,
        0, 57, 55, 1, 0, 0, 0, 58, 59, 3, 4, 2, 0, 59,
        60, 5, 8, 0, 0, 60, 61, 3, 6, 3, 0, 61, 67, 1,
        0, 0, 0, 62, 63, 3, 4, 2, 0, 63, 64, 5, 8, 0,
        0, 64, 65, 3, 4, 2, 0, 65, 67, 1, 0, 0, 0, 66,
        58, 1, 0, 0, 0, 66, 62, 1, 0, 0, 0, 67, 7, 1,
        0, 0, 0, 68, 71, 3, 16, 8, 0, 69, 71, 5, 7, 0,
        0, 70, 68, 1, 0, 0, 0, 70, 69, 1, 0, 0, 0, 71,
        73, 1, 0, 0, 0, 72, 74, 5, 10, 0, 0, 73, 72,
        1, 0, 0, 0, 73, 74, 1, 0, 0, 0, 74, 76, 1, 0,
        0, 0, 75, 70, 1, 0, 0, 0, 76, 77, 1, 0, 0, 0,
        77, 75, 1, 0, 0, 0, 77, 78, 1, 0, 0, 0, 78, 9,
        1, 0, 0, 0, 79, 82, 3, 12, 6, 0, 80, 82, 3,
        14, 7, 0, 81, 79, 1, 0, 0, 0, 81, 80, 1, 0, 0,
        0, 82, 11, 1, 0, 0, 0, 83, 85, 5, 4, 0, 0, 84,
        86, 5, 10, 0, 0, 85, 84, 1, 0, 0, 0, 85, 86,
        1, 0, 0, 0, 86, 87, 1, 0, 0, 0, 87, 88, 3, 8,
        4, 0, 88, 13, 1, 0, 0, 0, 89, 91, 5, 5, 0, 0,
        90, 92, 5, 10, 0, 0, 91, 90, 1, 0, 0, 0, 91,
        92, 1, 0, 0, 0, 92, 93, 1, 0, 0, 0, 93, 94, 3,
        8, 4, 0, 94, 15, 1, 0, 0, 0, 95, 99, 3, 18,
        9, 0, 96, 99, 3, 22, 11, 0, 97, 99, 3, 20, 10,
        0, 98, 95, 1, 0, 0, 0, 98, 96, 1, 0, 0, 0, 98,
        97, 1, 0, 0, 0, 99, 17, 1, 0, 0, 0, 100, 104,
        5, 1, 0, 0, 101, 103, 8, 0, 0, 0, 102, 101,
        1, 0, 0, 0, 103, 106, 1, 0, 0, 0, 104, 102,
        1, 0, 0, 0, 104, 105, 1, 0, 0, 0, 105, 107,
        1, 0, 0, 0, 106, 104, 1, 0, 0, 0, 107, 108,
        5, 1, 0, 0, 108, 19, 1, 0, 0, 0, 109, 113, 5,
        3, 0, 0, 110, 112, 8, 1, 0, 0, 111, 110, 1,
        0, 0, 0, 112, 115, 1, 0, 0, 0, 113, 111, 1, 0,
        0, 0, 113, 114, 1, 0, 0, 0, 114, 116, 1,
        0, 0, 0, 115, 113, 1, 0, 0, 0, 116, 117, 5, 3,
        0, 0, 117, 21, 1, 0, 0, 0, 118, 123, 5, 2,
        0, 0, 119, 122, 3, 20, 10, 0, 120, 122, 8, 2,
        0, 0, 121, 119, 1, 0, 0, 0, 121, 120, 1,
        0, 0, 0, 122, 125, 1, 0, 0, 0, 123, 121, 1,
        0, 0, 0, 123, 124, 1, 0, 0, 0, 124, 126, 1,
        0, 0, 0, 125, 123, 1, 0, 0, 0, 126, 127, 5, 2,
        0, 0, 127, 23, 1, 0, 0, 0, 19, 29, 34, 37,
        41, 45, 51, 55, 66, 70, 73, 77, 81, 85, 91,
        98, 104, 113, 121, 123
    ]


class ShellGrammarParser(Parser):
    grammarFileName = "ShellGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'''", "'\"'", "'`'", "'<'", "'>'", "';'",
                    "<INVALID>", "'|'"]

    symbolicNames = ["<INVALID>", "SINGLE_QUOTE", "DOUBLE_QUOTE", "BACK_QUOTE",
                     "OUT", "IN", "SEMI", "UNQUOTED", "PIPE", "NEW_LINE",
                     "WS"]

    RULE_command = 0
    RULE_subCommand = 1
    RULE_call = 2
    RULE_pipe = 3
    RULE_arg = 4
    RULE_redirection = 5
    RULE_left_redirection = 6
    RULE_right_redirection = 7
    RULE_quoted = 8
    RULE_single_quoted = 9
    RULE_back_quoted = 10
    RULE_double_quoted = 11

    ruleNames = ["command", "subCommand", "call", "pipe", "arg", "redirection",
                 "left_redirection", "right_redirection", "quoted",
                 "single_quoted", "back_quoted", "double_quoted"]

    EOF = Token.EOF
    SINGLE_QUOTE = 1
    DOUBLE_QUOTE = 2
    BACK_QUOTE = 3
    OUT = 4
    IN = 5
    SEMI = 6
    UNQUOTED = 7
    PIPE = 8
    NEW_LINE = 9
    WS = 10

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(
                self,
                parser,
                parent: ParserRuleContext = None,
                invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subCommand(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(
                    ShellGrammarParser.SubCommandContext
                )
            else:
                return self.getTypedRuleContext(
                    ShellGrammarParser.SubCommandContext,
                    i
                )

        def SEMI(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.SEMI)
            else:
                return self.getToken(ShellGrammarParser.SEMI, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_command

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCommand"):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)

    def command(self):

        localctx = ShellGrammarParser.CommandContext(
            self,
            self._ctx,
            self.state
        )
        self.enterRule(localctx, 0, self.RULE_command)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.subCommand()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 6:
                self.state = 25
                self.match(ShellGrammarParser.SEMI)
                self.state = 26
                self.subCommand()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(
                self,
                parser,
                parent: ParserRuleContext = None,
                invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipe(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.PipeContext,
                0
            )

        def call(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.CallContext,
                0
            )

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_subCommand

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSubCommand"):
                return visitor.visitSubCommand(self)
            else:
                return visitor.visitChildren(self)

    def subCommand(self):

        localctx = ShellGrammarParser.SubCommandContext(
            self,
            self._ctx,
            self.state
        )
        self.enterRule(localctx, 2, self.RULE_subCommand)
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(
                self._input, 1, self._ctx
            )
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.pipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.call()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(
                self,
                parser,
                parent: ParserRuleContext = None,
                invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.ArgContext,
                0
            )

        def WS(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WS)
            else:
                return self.getToken(ShellGrammarParser.WS, i)

        def redirection(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(
                    ShellGrammarParser.RedirectionContext
                )
            else:
                return self.getTypedRuleContext(
                    ShellGrammarParser.RedirectionContext,
                    i
                )

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_call

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCall"):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)

    def call(self):

        localctx = ShellGrammarParser.CallContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 4, self.RULE_call)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 10:
                self.state = 36
                self.match(ShellGrammarParser.WS)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4 or _la == 5:
                self.state = 39
                self.redirection()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 10:
                    self.state = 40
                    self.match(ShellGrammarParser.WS)

                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.arg()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 4 or _la == 5:
                self.state = 49
                self.redirection()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 10:
                    self.state = 50
                    self.match(ShellGrammarParser.WS)

                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(
                self,
                parser,
                parent: ParserRuleContext = None,
                invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(
                    ShellGrammarParser.CallContext
                )
            else:
                return self.getTypedRuleContext(
                    ShellGrammarParser.CallContext,
                    i
                )

        def PIPE(self):
            return self.getToken(ShellGrammarParser.PIPE, 0)

        def pipe(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.PipeContext,
                0
            )

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_pipe

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPipe"):
                return visitor.visitPipe(self)
            else:
                return visitor.visitChildren(self)

    def pipe(self):

        localctx = ShellGrammarParser.PipeContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 6, self.RULE_pipe)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 7, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.call()
                self.state = 59
                self.match(ShellGrammarParser.PIPE)
                self.state = 60
                self.pipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.call()
                self.state = 63
                self.match(ShellGrammarParser.PIPE)
                self.state = 64
                self.call()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self,
                     parser,
                     parent: ParserRuleContext = None,
                     invokingState: int = -1
                     ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(
                    ShellGrammarParser.QuotedContext
                )
            else:
                return self.getTypedRuleContext(
                    ShellGrammarParser.QuotedContext, i
                )

        def UNQUOTED(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.UNQUOTED)
            else:
                return self.getToken(ShellGrammarParser.UNQUOTED, i)

        def WS(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WS)
            else:
                return self.getToken(ShellGrammarParser.WS, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_arg

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArg"):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)

    def arg(self):

        localctx = ShellGrammarParser.ArgContext(
            self,
            self._ctx,
            self.state
        )
        self.enterRule(localctx, 8, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 70
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3]:
                        self.state = 68
                        self.quoted()
                        pass
                    elif token in [7]:
                        self.state = 69
                        self.match(ShellGrammarParser.UNQUOTED)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 73
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(
                        self._input, 9, self._ctx
                    )
                    if la_ == 1:
                        self.state = 72
                        self.match(ShellGrammarParser.WS)
                else:
                    raise NoViableAltException(self)
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 10, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self,
                     parser,
                     parent: ParserRuleContext = None,
                     invokingState: int = -1
                     ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_redirection(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.Left_redirectionContext,
                0
            )

        def right_redirection(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.Right_redirectionContext,
                0
            )

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_redirection

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRedirection"):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)

    def redirection(self):

        localctx = ShellGrammarParser.RedirectionContext(
            self,
            self._ctx,
            self.state
        )
        self.enterRule(localctx, 10, self.RULE_redirection)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.left_redirection()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.right_redirection()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Left_redirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser,
                     parent: ParserRuleContext = None,
                     invokingState: int = -1
                     ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUT(self):
            return self.getToken(ShellGrammarParser.OUT, 0)

        def arg(self):
            return self.getTypedRuleContext(ShellGrammarParser.ArgContext, 0)

        def WS(self):
            return self.getToken(ShellGrammarParser.WS, 0)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_left_redirection

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLeft_redirection"):
                return visitor.visitLeft_redirection(self)
            else:
                return visitor.visitChildren(self)

    def left_redirection(self):

        localctx = ShellGrammarParser.Left_redirectionContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 12, self.RULE_left_redirection)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ShellGrammarParser.OUT)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 10:
                self.state = 84
                self.match(ShellGrammarParser.WS)

            self.state = 87
            self.arg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Right_redirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self,
                     parser,
                     parent: ParserRuleContext = None,
                     invokingState: int = -1
                     ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(ShellGrammarParser.IN, 0)

        def arg(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.ArgContext,
                0
            )

        def WS(self):
            return self.getToken(ShellGrammarParser.WS, 0)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_right_redirection

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRight_redirection"):
                return visitor.visitRight_redirection(self)
            else:
                return visitor.visitChildren(self)

    def right_redirection(self):

        localctx = ShellGrammarParser.Right_redirectionContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 14, self.RULE_right_redirection)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ShellGrammarParser.IN)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 10:
                self.state = 90
                self.match(ShellGrammarParser.WS)

            self.state = 93
            self.arg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self,
                     parser,
                     parent: ParserRuleContext = None,
                     invokingState: int = -1
                     ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_quoted(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.Single_quotedContext,
                0
            )

        def double_quoted(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.Double_quotedContext,
                0
            )

        def back_quoted(self):
            return self.getTypedRuleContext(
                ShellGrammarParser.Back_quotedContext,
                0
            )

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_quoted

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitQuoted"):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)

    def quoted(self):

        localctx = ShellGrammarParser.QuotedContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 16, self.RULE_quoted)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.single_quoted()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.double_quoted()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.back_quoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Single_quotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self,
                     parser,
                     parent: ParserRuleContext = None,
                     invokingState: int = -1
                     ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTE(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.SINGLE_QUOTE)
            else:
                return self.getToken(ShellGrammarParser.SINGLE_QUOTE, i)

        def NEW_LINE(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.NEW_LINE)
            else:
                return self.getToken(ShellGrammarParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_single_quoted

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSingle_quoted"):
                return visitor.visitSingle_quoted(self)
            else:
                return visitor.visitChildren(self)

    def single_quoted(self):

        localctx = ShellGrammarParser.Single_quotedContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 18, self.RULE_single_quoted)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ShellGrammarParser.SINGLE_QUOTE)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1532) != 0:
                self.state = 101
                _la = self._input.LA(1)
                if _la <= 0 or _la == 1 or _la == 9:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(ShellGrammarParser.SINGLE_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Back_quotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self,
                     parser,
                     parent: ParserRuleContext = None,
                     invokingState: int = -1
                     ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACK_QUOTE(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.BACK_QUOTE)
            else:
                return self.getToken(ShellGrammarParser.BACK_QUOTE, i)

        def NEW_LINE(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.NEW_LINE)
            else:
                return self.getToken(ShellGrammarParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_back_quoted

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBack_quoted"):
                return visitor.visitBack_quoted(self)
            else:
                return visitor.visitChildren(self)

    def back_quoted(self):

        localctx = ShellGrammarParser.Back_quotedContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 20, self.RULE_back_quoted)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ShellGrammarParser.BACK_QUOTE)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1526) != 0:
                self.state = 110
                _la = self._input.LA(1)
                if _la <= 0 or _la == 3 or _la == 9:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(ShellGrammarParser.BACK_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Double_quotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(
                self, parser, parent: ParserRuleContext = None,
                invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_QUOTE(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.DOUBLE_QUOTE)
            else:
                return self.getToken(ShellGrammarParser.DOUBLE_QUOTE, i)

        def back_quoted(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(
                    ShellGrammarParser.Back_quotedContext
                )
            else:
                return self.getTypedRuleContext(
                    ShellGrammarParser.Back_quotedContext,
                    i
                )

        def NEW_LINE(self, i: int = None):
            if i is None:
                return self.getTokens(ShellGrammarParser.NEW_LINE)
            else:
                return self.getToken(ShellGrammarParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_double_quoted

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDouble_quoted"):
                return visitor.visitDouble_quoted(self)
            else:
                return visitor.visitChildren(self)

    def double_quoted(self):

        localctx = ShellGrammarParser.Double_quotedContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 22, self.RULE_double_quoted)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(ShellGrammarParser.DOUBLE_QUOTE)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1530) != 0:
                self.state = 121
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(
                    self._input, 17, self._ctx
                )
                if la_ == 1:
                    self.state = 119
                    self.back_quoted()
                    pass

                elif la_ == 2:
                    self.state = 120
                    _la = self._input.LA(1)
                    if _la <= 0 or _la == 2 or _la == 9:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass

                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(ShellGrammarParser.DOUBLE_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
