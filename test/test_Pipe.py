import os
import unittest
from src.commands.Call import Call
from src.commands.Pipe import Pipe

from antlr.Converter import Converter
from factories.input_factory import input_factory


class TestPipe(unittest.TestCase):
    os.chdir("/")

    def test_pipe1(self):
        """
            Test case 1: echo hello world | echo
        """
        left_command = Call("echo", ["hello", "world"], None, None)
        right_command = Call("echo", [], None, None)
        pipe = Pipe(left_command, right_command)
        pipe.eval()
        self.assertEqual(pipe.output.popleft().strip(), "hello world")

    def test_pipe2(self):
        """
            Test case 2: cat /comp0010/test/dir2/uniq_testing_case.txt
                        | sort | uniq
        """
        pipe_left_command = Call("cat",
                                 ["/comp0010/test/dir2/uniq_testing_case.txt"],
                                 None,
                                 None)
        middle_command = Call("sort", [], None, None)
        right_command = Call("uniq", [], None, None)
        pipe_right_command = Pipe(middle_command, right_command)
        pipe = Pipe(pipe_left_command, pipe_right_command)
        pipe.eval()
        output_lines = [line.strip() for line in pipe.output]
        expected_lines = ['HHHHHH', 'SSSSSs',
                          'false', 'hello',
                          'hhhhhh', 'python',
                          'ssssss', 'true']
        self.assertEqual(output_lines, expected_lines)

    def test_pipe3(self):
        """
            Test case 3: cat /comp0010/test/dir2/uniq_testing_case.txt
                        | unsupported_command
        """
        with self.assertRaises(ValueError):
            pipe_left_command = Call("cat",
                                     ["/comp0010/test/dir2/"
                                      "uniq_testing_case.txt"],
                                     None,
                                     None)
            right_command = Call("unsupported_command", [], None, None)
            pipe = Pipe(pipe_left_command, right_command)
            pipe.eval()

    def test_pipe4(self):
        """
            Test case 4: unsupported_command | sort
        """
        with self.assertRaises(ValueError):
            left_command = Call("unsupported_command", [], None, None)
            right_command = Call("sort", [], None, None)
            pipe = Pipe(left_command, right_command)
            pipe.eval()

    def test_pipe5(self):
        """
            Test case 5: echo hello world | echo
        """
        output = input_factory("echo hello world | echo", Converter())
        self.assertEqual(output.popleft().strip(), "hello world")
