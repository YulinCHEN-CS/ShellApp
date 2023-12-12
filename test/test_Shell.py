import os
import unittest
import subprocess
from collections import deque

from antlr.Converter import Converter
from applications.Application import Application
from commands.Command import Command
from factories.input_factory import input_factory


class TestShell(unittest.TestCase):
    def test_shell(self):
        """
            Test the shell's basic functionality
        """
        os.chdir("/")
        cmdline = ['python', '/comp0010/src/shell.py',
                   '-c', 'echo hello world']
        output = subprocess.run(cmdline, capture_output=True, text=True)
        self.assertEqual(output.stdout, "hello world\n")
        self.assertEqual(len(output.stdout), 12)

    def test_general1(self):
        """
            Test complex commands echo aaa > "
                                  "hidden_dir1/file2.txt; cat "
                                  "hidden_dir1/file1.txt hidden_dir1/"
                                  "file2.txt | uniq -i
        """
        os.chdir("/comp0010/test/dir1")
        output_lines = input_factory("echo aaa > "
                                     "hidden_dir1/file2.txt; cat "
                                     "hidden_dir1/file1.txt hidden_dir1/"
                                     "file2.txt | uniq -i",
                                     Converter()
                                     )
        expected_lines = {
            "AAA",
            "BBB",
            "AAA"
        }
        output_set = {line.strip() for line in output_lines}

        self.assertEqual(set(output_set), set(expected_lines))

    def test_general2(self):
        """
            Test complex commands:
            cat /comp0010/test/dir2/uniq_testing_case.txt
             | sort | uniq
        """
        os.chdir("/comp0010/test/dir2")
        output_lines = input_factory("cat uniq_testing_case.txt"
                                     " | sort | uniq",
                                     Converter()
                                     )
        output_lines = [line.strip() for line in output_lines]
        expected_lines = ['HHHHHH', 'SSSSSs',
                          'false', 'hello',
                          'hhhhhh', 'python',
                          'ssssss', 'true']

        self.assertEqual(output_lines, expected_lines)

    def test_abstract_command(self):
        """
            Test abstract command
        """

        class TempCommand(Command):
            def __init__(self):
                super().__init__()

            def eval(self):
                super().eval()

        command = TempCommand()
        # with self.assertRaises(TypeError):
        command.eval()
        self.assertIsInstance(command, Command)
        self.assertIsInstance(command.output, deque)
        self.assertFalse(command.output)

    def test_abstract_application(self):
        """
            Test abstract application
        """

        class TempApplication(Application):
            def __init__(self, args, output):
                super().__init__(args, output)

            def exec(self):
                super().exec()

        application = TempApplication([], deque())
        application.exec()
        self.assertIsInstance(application, Application)
        self.assertIsInstance(application.output, deque)
        self.assertFalse(application.output)
