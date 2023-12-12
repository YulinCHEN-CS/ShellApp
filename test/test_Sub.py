import unittest

from antlr.Converter import Converter
from factories.input_factory import input_factory


class TestSub(unittest.TestCase):
    def test_sub1(self):
        """
            Test case 1:
                echo `echo hello`
        """
        output = input_factory("echo `echo hello`", Converter())
        self.assertEqual(output.popleft().strip(), "hello")

    def test_sub2(self):
        """
            Test case 2:
                echo "hello `echo user`"
        """
        output = input_factory("echo \"hello `echo user`\"",
                               Converter())
        self.assertEqual(output.popleft().strip(), "hello user")

    def test_sub3(self):
        """
            Test case 3:
                `echo ls` /comp0010/test/dir1/hidden_dir1
        """
        output = input_factory("`echo ls` /comp0010/test/dir1/hidden_dir1",
                               Converter())
        expected_lines = [
            "file1.txt",
            "file2.txt"
        ]
        output_lines = [line.strip() for line in output]
        self.assertEqual(set(output_lines), set(expected_lines))

    def test_sub4(self):
        """
            Test case 4:
                echo `unsupported_application /comp0010`
        """
        with self.assertRaises(ValueError):
            input_factory(
                "echo `unsupported_application /comp0010`",
                Converter()
            )

    def test_sub5(self):
        """
            Test case 5:
                echo "`echo hello` world" '`echo single quote`'
        """
        output = input_factory(
            "echo \"`echo hello` world\" \'`echo single quote`\'",
            Converter()
        )
        self.assertEqual(output.popleft().strip(),
                         "hello world `echo single quote`")

    def test_sub6(self):
        """
            Test case 6: echo
                "`echo hello` `echo world`"
        """
        output = input_factory(
            "echo \"`echo hello` `echo world`\"",
            Converter()
        )
        self.assertEqual(output.popleft().strip(), "hello world")

    def test_sub7(self):
        """
            Test case 7:
                echo `cd /comp0010`
        """
        output = input_factory(
            "echo `cd /comp0010`",
            Converter()
        )
        self.assertFalse(output)
