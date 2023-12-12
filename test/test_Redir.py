import os
import unittest

from src.commands.Call import Call
from antlr.Converter import Converter
from factories.input_factory import input_factory


class TestRedir(unittest.TestCase):
    TESTDIR_IN = "/comp0010/test/dir2/redir_testing_in_case.txt"
    TESTDIR_OUT = "/comp0010/test/dir2/redir_testing_out_case.txt"
    NONEXISTENT = "/comp0010/test/dir2/non_existent.txt"
    os.chdir("/")  # Reset the current working directory

    def test_redir1(self):
        """
            Test case 1:
                echo hello world
                > /comp0010/test/dir2/redir_testing_in_case.txt
        """

        call = Call("echo", ["hello", "world"], None, self.TESTDIR_IN)
        call.eval()
        content = open(self.TESTDIR_IN, "r").read()

        self.assertEqual("hello world", content.strip())

    def test_redir2(self):
        """
            Test case 2:
                echo
                < /comp0010/test/dir2/redir_testing_out_case.txt
        """

        call = Call("echo", [], self.TESTDIR_OUT, None)
        call.eval()
        content = open(self.TESTDIR_OUT, "r").read()

        self.assertEqual(call.output.popleft().strip(), content.strip())

    def test_redir3(self):
        """
            Test case 3:
                echo hello world
                < /comp0010/test/dir2/redir_testing_out_case.txt
                > /comp0010/test/dir2/redir_testing_in_case.txt
        """

        call = Call("echo", [], self.TESTDIR_OUT, self.TESTDIR_IN)
        call.eval()
        content_from = open(self.TESTDIR_OUT, "r").read()
        content_to = open(self.TESTDIR_IN, "r").read()

        self.assertEqual(content_from.strip(), content_to.strip())

    def test_redir4(self):
        """
            Test case 4:
                echo hello world
                > /comp0010/test/dir2/redir_testing_in_case.txt
                > /comp0010/test/dir2/redir_testing_out_case.txt
        """

        with self.assertRaises(ValueError):
            input_factory(
                "echo hello world "
                "> /comp0010/test/dir2/redir_testing_in_case.txt "
                "> /comp0010/test/dir2/redir_testing_out_case.txt",
                Converter())

    def test_redir5(self):
        """
            Test case 5:
                echo hello world
                < /comp0010/test/dir2/redir_testing_in_case.txt
                < /comp0010/test/dir2/redir_testing_out_case.txt
        """

        with self.assertRaises(ValueError):
            input_factory(
                "echo hello world "
                "< /comp0010/test/dir2/redir_testing_in_case.txt "
                "< /comp0010/test/dir2/redir_testing_out_case.txt",
                Converter()
            )

    def test_redir6(self):
        """
            Test case 6:
                echo < /comp0010/test/dir2/non_existent.txt
        """

        call = Call("echo", [], self.NONEXISTENT, None)
        with self.assertRaises(FileNotFoundError):
            call.eval()

    def test_redir7(self):
        """
            Test case 6:
                echo hello world > /comp0010/test/dir2/non_existent.txt
        """

        call = Call("echo", ["hello", "world"], None, self.NONEXISTENT)
        call.eval()
        content = open(self.NONEXISTENT, "r").read()
        self.assertEqual("hello world", content.strip())
        os.remove('/comp0010/test/dir2/non_existent.txt')

    def test_redir8(self):
        """
            Test case 8:
                echo hello world
                > /comp0010/test/dir2/redir_testing_in_case.txt
                > /comp0010/test/dir2/redir_testing_out_case.txt
        """

        with self.assertRaises(ValueError):
            input_factory(
                "echo hello world "
                "> /comp0010/test/dir2/redir_testing_in_case.txt "
                "> /comp0010/test/dir2/redir_testing_out_case.txt",
                Converter()
            )
