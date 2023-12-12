import unittest

from antlr4 import InputStream, CommonTokenStream, ParseTreeVisitor

from antlr.generated.ShellGrammarLexer import ShellGrammarLexer
from antlr.generated.ShellGrammarParser import ShellGrammarParser
from antlr.generated.ShellGrammarVisitor import ShellGrammarVisitor


class TestParser(unittest.TestCase):

    def test_antlr1(self):
        """
            Test case 1:
                echo hello world hello｜ uniq -i > output.txt
        """
        input_str = "echo hello world ｜ uniq -i > output.txt"
        input_stream = InputStream(input_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)
        tree = parser.command()
        # General Visitor, return None as default
        empty_cmd = tree.accept(ShellGrammarVisitor())
        self.assertIsNotNone(tree)
        self.assertEqual(
            tree.toStringTree(recog=parser),
            "(command (subCommand (call "
            "(arg echo   hello   world   ｜   uniq   -i  ) "
            "(redirection (right_redirection >   (arg output.txt))))))"
        )
        self.assertFalse(empty_cmd)

    def test_antlr2(self):
        """
            Test case 2:
                ;;||
        """

        with self.assertRaises(Exception):
            input_str = ";;||"
            input_stream = InputStream(input_str)
            lexer = ShellGrammarLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = ShellGrammarParser(stream)
            tree = parser.command()
            self.assertFalse(tree)

    def test_antlr3(self):
        """
            Test case 3:
                echo hello world ; echo 'user' < intput.txt
        """
        input_str = "echo hello world ; echo 'user' < input.txt"
        input_stream = InputStream(input_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)
        tree = parser.command()
        # General Visitor, return None as default
        empty_cmd = tree.accept(ShellGrammarVisitor())
        self.assertFalse(empty_cmd)
        self.assertEqual(
            tree.toStringTree(recog=parser),
            "(command (subCommand (call (arg echo   hello   world  ))) ; "
            "(subCommand (call   (arg echo   "
            "(quoted (single_quoted ' user '))  ) "
            "(redirection (left_redirection <   (arg input.txt))))))"
        )

    def test_antlr4(self):
        """
            Test case 4:
                cat `ls *.txt` | echo
        """
        input_str = "cat `ls *.txt` | echo "
        input_stream = InputStream(input_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)
        tree = parser.command()
        # General Visitor, return None as default
        empty_cmd = tree.accept(ShellGrammarVisitor())
        self.assertFalse(empty_cmd)
        self.assertEqual(
            tree.toStringTree(recog=parser),
            "(command (subCommand (pipe (call (arg cat   "
            "(quoted (back_quoted ` ls   *.txt `))  )) | "
            "(call   (arg echo  )))))"
        )

    def test_Antlr5(self):
        """
            Test case 5:
                ls | echo
        """
        input_str = "ls | echo"
        input_stream = InputStream(input_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)
        tree = parser.command()
        # General Visitor, return None as default
        empty_cmd = tree.accept(ShellGrammarVisitor())
        self.assertIsNotNone(tree)
        self.assertEqual(
            tree.toStringTree(recog=parser),
            "(command (subCommand (pipe (call (arg ls  )) "
            "| (call   (arg echo)))))"
        )
        self.assertFalse(empty_cmd)

    def test_Antlr6(self):
        """
        Test case for double-quoted strings:
            echo "double quoted string"
        """
        input_str = 'echo "double quoted string"'
        input_stream = InputStream(input_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)
        tree = parser.command()
        # General Visitor, return None as default
        empty_cmd = tree.accept(ShellGrammarVisitor())
        self.assertIsNotNone(tree)
        self.assertEqual(
            tree.toStringTree(recog=parser),
            "(command (subCommand (call (arg echo   "
            "(quoted (double_quoted \" double   quoted   string \"))))))"
        )
        self.assertFalse(empty_cmd)

    def parse_command(self, command_str):
        # Utility method to parse a command string
        lexer = ShellGrammarLexer(InputStream(command_str))
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)
        return parser.command()

    def test_Antlr7(self):
        """
            Testing for subCommand
        """
        command_str = "echo hello; ls -l"
        command_context = self.parse_command(command_str)

        # Test without index
        subcommands_all = command_context.subCommand()
        self.assertEqual(len(subcommands_all), 2)

        # Test with index
        first_subcommand = command_context.subCommand(0).getText()
        self.assertEqual(first_subcommand, "echo hello")

        second_subcommand = subcommands_all[1].getText().strip()
        self.assertEqual(second_subcommand, "ls -l")

    def test_Antlr8(self):
        """
            Testing for semiCommand with visitCommand
        """
        command_str = "command1; command2; command3"
        command_context = self.parse_command(command_str)

        # Test without index
        semi_tokens_all = command_context.SEMI()
        self.assertEqual(len(semi_tokens_all), 2)

        # Test with index
        # Assuming the first SEMI token is at a specific index
        first_semi_token = command_context.SEMI(0)
        second_semi_token = command_context.SEMI(1)

        self.assertIsNotNone(first_semi_token)
        self.assertIsNotNone(second_semi_token)

    def test_Antlr9(self):
        """
            Testing for semiCommand without visitCommand
        """
        command_str = "command1; command2; command3"
        command_context = self.parse_command(command_str)

        visitor = ParseTreeVisitor()

        # The visitor does not have visitCommand,
        # so visitChildren should be called
        result = command_context.accept(visitor)
        self.assertIsNone(result)

    def test_Antlr10(self):
        """
            Testing for pipe in subCommand
        """
        command_str = "cat file.txt | grep 'test'"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        subCommand_context = tree.subCommand(0)

        # Test the pipe method
        pipe_context = subCommand_context.pipe()
        self.assertIsNotNone(pipe_context)

    def test_Antlr11(self):
        """
            Testing for call in subCommand
        """
        command_str = "echo 'Hello World'"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        subCommand_context = tree.subCommand(0)

        # Test the call method
        call_context = subCommand_context.call()
        self.assertIsNotNone(call_context)

    def test_Antlr12(self):
        """
            Testing for arg in call
        """
        command_str = "echo 'Hello World'"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        call_context = tree.subCommand(0).call()

        # Test the arg method
        arg_context = call_context.arg()
        self.assertIsNotNone(arg_context)

    def test_Antlr13(self):
        """
            Testing for ws in call
        """
        command_str = "echo    'Hello World'"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        call_context = tree.subCommand(0).call()

        # Test WS without index
        ws_tokens_all = call_context.WS()
        self.assertIsNotNone(ws_tokens_all)

        # # Test WS with index
        first_ws_token = call_context.WS(0)
        self.assertIsNone(first_ws_token)

    def test_Antlr14(self):
        """
            Testing for redirection in call
        """
        command_str = "echo 'Hello World' > output.txt 2> error.txt"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        call_context = tree.subCommand(0).call()

        # Test redirection without index
        redirections_all = call_context.redirection()
        self.assertEqual(len(redirections_all), 2)

        # Test redirection with index
        first_redirection = call_context.redirection(0)
        second_redirection = call_context.redirection(1)
        self.assertIsNotNone(first_redirection)
        self.assertIsNotNone(second_redirection)

    def test_Antlr15(self):
        """
            Testing call with and withoutindex
        """
        command_str = "echo 'Hello' | grep 'World'"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        pipe_context = tree.subCommand(0).pipe()

        # Test call without index
        calls_all = pipe_context.call()
        self.assertTrue(len(calls_all) >= 1)

        # Test call with index
        first_call = pipe_context.call(0)
        self.assertIsNotNone(first_call)

    def test_Antlr16(self):
        """
            Testing pipe token
        """
        command_str = "command1 | command2"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        pipe_context = tree.subCommand(0).pipe()

        # Test PIPE token retrieval
        pipe_token = pipe_context.PIPE()
        self.assertIsNotNone(pipe_token)

    def test_Antlr17(self):
        """
            Testing pipe method
        """
        command_str = "command1 | command2 | command3"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        pipe_context = tree.subCommand(0).pipe()

        # Test pipe method
        nested_pipe_context = pipe_context.pipe()
        self.assertIsNotNone(nested_pipe_context)

    def get_quoted_context(self, command_str):
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        return tree.subCommand(0).call().arg().quoted()

    def test_Antlr18(self):
        """
            Testing single quoted
        """
        quoted_contexts = self.get_quoted_context("echo 'Hello World'")
        for quoted_context in quoted_contexts:
            self.assertIsNotNone(quoted_context.single_quoted())

    def test_Antlr19(self):
        """
            Testing double quoted
        """
        quoted_contexts = self.get_quoted_context('echo "Hello World"')
        for quoted_context in quoted_contexts:
            self.assertIsNotNone(quoted_context.double_quoted())

    def test_Antlr20(self):
        """
            Testing back quoted
        """
        quoted_contexts = self.get_quoted_context("echo `ls -l`")
        for quoted_context in quoted_contexts:
            self.assertIsNotNone(quoted_context.back_quoted())

    def test_Antlr21(self):
        """
            Testing accept method with visitQuoted
        """
        command_str = "echo 'Hello World'"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        quoted_context = tree.subCommand(0).call().arg().quoted()[0]

        # Create a visitor and dynamically add a visitQuoted method
        visitor = ParseTreeVisitor()
        visitor.visitQuoted = lambda x: "Visited"
        result = quoted_context.accept(visitor)

        self.assertEqual(result, "Visited")

    def test_Antlr22(self):
        """
            Testing accept method without visitQuoted
        """
        command_str = "echo 'Hello World'"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        quoted_context = tree.subCommand(0).call().arg().quoted()[0]

        # Use a plain visitor without visitQuoted method
        visitor = ParseTreeVisitor()
        result = quoted_context.accept(visitor)

        self.assertIsNone(result)

    def get_right_redirection_context(self, command_str):
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        return tree.subCommand(0).call().redirection(0).right_redirection()

    def test_Antlr23(self):
        """
            Testing right redirection
        """
        right_redirection_context = \
            self.get_right_redirection_context("echo > output.txt")
        in_token = right_redirection_context.IN()
        self.assertIsNotNone(in_token)

    def test_Antlr24(self):
        """
            Testing arg method for right redirection
        """
        right_redirection_context = \
            self.get_right_redirection_context("echo > output.txt")
        arg_context = right_redirection_context.arg()
        self.assertIsNotNone(arg_context)

    def test_Antlr25(self):
        """
            Testing WS token for Right_redirection
        """
        right_redirection_context = \
            self.get_right_redirection_context("echo  >  output.txt")
        ws_token = right_redirection_context.WS()
        self.assertIsNotNone(ws_token)

    def test_Antlr26(self):
        """
            Testing accept method with visitRight redirection
        """
        right_redirection_context = \
            self.get_right_redirection_context("echo > output.txt")

        # Dynamically add visitRight_redirection to the visitor
        visitor = ParseTreeVisitor()
        visitor.visitRight_redirection = lambda x: "Visited Right Redirection"
        result = right_redirection_context.accept(visitor)

        self.assertEqual(result, "Visited Right Redirection")

    def test_Antlr27(self):
        """
            Testing accept method without visitRight redirection
        """
        right_redirection_context = \
            self.get_right_redirection_context("echo > output.txt")

        # Use a plain visitor without visitRight_redirection method
        visitor = ParseTreeVisitor()
        result = right_redirection_context.accept(visitor)

        # Assuming visitChildren returns None by default
        self.assertIsNone(result)

    def get_single_quoted_context(self, command_str):
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        return tree.subCommand(0).call().arg().quoted(0).single_quoted()

    def test_Antlr28(self):
        """
            Testing single quoted tokens without index
        """
        single_quoted_context = \
            self.get_single_quoted_context("echo 'Hello World'")
        single_quote_tokens = single_quoted_context.SINGLE_QUOTE()
        self.assertEqual(len(single_quote_tokens), 2)
        # Expecting 2 SINGLE_QUOTE tokens

    def test_Antlr29(self):
        """
            Testing single quoted tokens with index
        """
        single_quoted_context = \
            self.get_single_quoted_context("echo 'Hello World'")
        first_single_quote_token = single_quoted_context.SINGLE_QUOTE(0)
        second_single_quote_token = single_quoted_context.SINGLE_QUOTE(1)
        self.assertIsNotNone(first_single_quote_token)
        self.assertIsNotNone(second_single_quote_token)

    def get_back_quoted_context(self, command_str):
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        return tree.subCommand(0).call().arg().quoted(0).back_quoted()

    def test_Antlr30(self):
        """
            Testing back quote tokens without index
        """
        back_quoted_context = \
            self.get_back_quoted_context("echo `ls -l`")
        back_quote_tokens = back_quoted_context.BACK_QUOTE()
        self.assertEqual(len(back_quote_tokens), 2)
        # Expecting 2 BACK_QUOTE tokens

    def test_Antlr31(self):
        """
            Testing back quote tokens with index
        """
        back_quoted_context = \
            self.get_back_quoted_context("echo `ls -l`")
        first_back_quote_token = back_quoted_context.BACK_QUOTE(0)
        second_back_quote_token = back_quoted_context.BACK_QUOTE(1)
        self.assertIsNotNone(first_back_quote_token)
        self.assertIsNotNone(second_back_quote_token)

    def test_Antlr32(self):
        """
            Testing accept method with visitBack quoted
        """
        back_quoted_context = \
            self.get_back_quoted_context("echo `ls -l`")

        # Dynamically add visitBack_quoted to the visitor
        visitor = ParseTreeVisitor()
        visitor.visitBack_quoted = lambda x: "Visited Back Quoted"
        result = back_quoted_context.accept(visitor)

        self.assertEqual(result, "Visited Back Quoted")

    def test_Antlr33(self):
        """
            Testing accept method without visitBack quoted
        """
        back_quoted_context = \
            self.get_back_quoted_context("echo `ls -l`")

        # Use a plain visitor without visitBack_quoted method
        visitor = ParseTreeVisitor()
        result = back_quoted_context.accept(visitor)

        # Assuming visitChildren returns None by default
        self.assertIsNone(result)

    def get_double_quoted_context(self, command_str):
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        return tree.subCommand(0).call().arg().quoted(0).double_quoted()

    def test_Antlr34(self):
        """
            Testing double quote tokens without index
        """
        double_quoted_context = \
            self.get_double_quoted_context('echo "Hello World"')
        double_quote_tokens = double_quoted_context.DOUBLE_QUOTE()
        self.assertEqual(len(double_quote_tokens), 2)
        # Expecting 2 DOUBLE_QUOTE tokens

    def test_Antlr35(self):
        """
            Testing double quote tokens with index
        """
        double_quoted_context = \
            self.get_double_quoted_context('echo "Hello World"')
        first_double_quote_token = double_quoted_context.DOUBLE_QUOTE(0)
        second_double_quote_token = double_quoted_context.DOUBLE_QUOTE(1)
        self.assertIsNotNone(first_double_quote_token)
        self.assertIsNotNone(second_double_quote_token)

    def test_Antlr36(self):
        """
            Testing back quoted within double quote
        """
        double_quoted_context = \
            self.get_double_quoted_context('echo "Hello `ls -l` World"')
        back_quoted_contexts = double_quoted_context.back_quoted()
        self.assertTrue(len(back_quoted_contexts) >= 1)
        # Expecting at least 1 back_quoted context

    def test_Antlr37(self):
        """
            Testing accept method with visitDouble quoted
        """
        double_quoted_context = \
            self.get_double_quoted_context('echo "Hello World"')

        # Dynamically add visitDouble_quoted to the visitor
        visitor = ParseTreeVisitor()
        visitor.visitDouble_quoted = lambda x: "Visited Double Quoted"
        result = double_quoted_context.accept(visitor)

        self.assertEqual(result, "Visited Double Quoted")

    def test_Antlr38(self):
        """
            Testing accept method without visitDouble quoted
        """
        double_quoted_context = \
            self.get_double_quoted_context('echo "Hello World"')

        # Use a plain visitor without visitDouble_quoted method
        visitor = ParseTreeVisitor()
        result = double_quoted_context.accept(visitor)

        # Assuming visitChildren returns None by default
        self.assertIsNone(result)

    def get_arg_context(self, command_str):
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        return tree.subCommand(0).call().arg()

    def test_Antlr39(self):
        """
            Testing unquoted tokens without index
        """
        arg_context = self.get_arg_context("echo Hello World")
        unquoted_tokens = arg_context.UNQUOTED()
        self.assertTrue(len(unquoted_tokens) >= 2)
        # Expecting at least 2 UNQUOTED tokens

    def test_Antlr40(self):
        """
            Testing unquoted tokens with index
        """
        arg_context = self.get_arg_context("echo Hello World")
        first_unquoted_token = arg_context.UNQUOTED(0)
        self.assertIsNotNone(first_unquoted_token)

    def test_Antlr41(self):
        """
            Testing ws tokens without index
        """
        arg_context = self.get_arg_context("echo   Hello   World")
        ws_tokens = arg_context.WS()
        self.assertTrue(len(ws_tokens) >= 2)
        # Expecting at least 2 WS tokens

    def test_Antlr42(self):
        """
            Testing ws tokens with index
        """
        arg_context = self.get_arg_context("echo   Hello   World")
        first_ws_token = arg_context.WS(0)
        self.assertIsNotNone(first_ws_token)

    def test_Antlr43(self):
        """
            Testing call with leading whitespace
        """
        command_str = "  echo Hello World"
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        call_context = parser.call()
        # Check if the first token is WS
        self.assertEqual(call_context.start.type, ShellGrammarParser.WS)

    def test_Antlr45(self):
        """
            Testing call with trailing whitespace
        """
        command_str = "echo Hello World  "
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        call_context = parser.call()
        self.assertEqual(call_context.stop.type, ShellGrammarParser.WS)

    def get_redirection_context(self, command_str):
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        return tree.subCommand(0).call().redirection(0)

    def test_Antlr46(self):
        """
            Testing accept method with visitRedirection
        """
        redirection_context = \
            self.get_redirection_context("echo Hello > output.txt")

        # Dynamically add visitRedirection to the visitor
        visitor = ParseTreeVisitor()
        visitor.visitRedirection = lambda x: "Visited Redirection"
        result = redirection_context.accept(visitor)

        self.assertEqual(result, "Visited Redirection")

    def test_Antlr47(self):
        """
            Testing accept method without visitRedirection
        """
        redirection_context = \
            self.get_redirection_context("echo Hello > output.txt")

        # Use a plain visitor without visitRedirection method
        visitor = ParseTreeVisitor()
        result = redirection_context.accept(visitor)

        # Assuming visitChildren returns None by default
        self.assertIsNone(result)

    def get_left_redirection_context(self, command_str):
        input_stream = InputStream(command_str)
        lexer = ShellGrammarLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(stream)

        tree = parser.command()
        return tree.subCommand(0).call().redirection(0).left_redirection()

    def test_Antlr48(self):
        """
            Testing left redirection
        """
        left_redirection_context = \
            self.get_left_redirection_context("echo < input.txt")
        out_token = left_redirection_context.OUT()
        self.assertIsNotNone(out_token)

    def test_Antlr49(self):
        """
            Testing arg method for left redirection
        """
        left_redirection_context = \
            self.get_left_redirection_context("echo < input.txt")
        arg_context = left_redirection_context.arg()
        self.assertIsNotNone(arg_context)

    def test_Antlr50(self):
        """
            Testing WS token for left redirection
        """
        left_redirection_context = \
            self.get_left_redirection_context("echo <  input.txt")
        ws_token = left_redirection_context.WS()
        self.assertIsNotNone(ws_token)

    def test_Antlr51(self):
        """
            Testing accept method with visitLeft redirection
        """
        left_redirection_context = \
            self.get_left_redirection_context("echo < input.txt")

        # Dynamically add visitLeft_redirection to the visitor
        visitor = ParseTreeVisitor()
        visitor.visitLeft_redirection = lambda x: "Visited Left Redirection"
        result = left_redirection_context.accept(visitor)

        self.assertEqual(result, "Visited Left Redirection")

    def test_Antlr52(self):
        """
            Testing accept method without visitLeft redirection
        """
        left_redirection_context = \
            self.get_left_redirection_context("echo < input.txt")

        # Use a plain visitor without visitLeft_redirection method
        visitor = ParseTreeVisitor()
        result = left_redirection_context.accept(visitor)

        # Assuming visitChildren returns None by default
        self.assertIsNone(result)
