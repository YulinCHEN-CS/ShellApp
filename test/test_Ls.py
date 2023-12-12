import os
import unittest
from collections import deque

from src.applications.Ls import Ls
from src.antlr.Converter import Converter
from src.factories.input_factory import input_factory


class TestLs(unittest.TestCase):
    TESTDIR = "/comp0010/test/dir1"
    HIDDENDIR1 = "/comp0010/test/dir1/hidden_dir1"
    NONEXISTENT = "/non_existent"
    os.chdir("/")  # Reset the current working directory

    def test_ls1(self):
        """
            Test case 1: ls /comp0010/test/dir1
        """

        ls = Ls([self.TESTDIR], deque())
        ls.exec()
        output_lines = [line.strip() for line in ls.output]
        expected_lines = [
            "hidden_dir1",
            "hidden_dir2"
        ]

        self.assertEqual(set(output_lines), set(expected_lines))

    def test_ls2(self):
        """
            Test case 2: ls /comp0010/test/dir1/*
                Explanation: The reason why we need to use input_factory() is
                because we handled the globbing pattern(*) before we pass the
                arguments to the command. Therefore, we need to use
                input_factory() to handle the globbing pattern(*)
        """

        output_lines = input_factory(f"ls {self.TESTDIR}/*", Converter())
        expected_lines = {
            "/comp0010/test/dir1/hidden_dir1",
            "/comp0010/test/dir1/hidden_dir2"
        }
        output_set = {line.strip() for line in output_lines}

        self.assertEqual(set(output_set), set(expected_lines))

    def test_ls3(self):
        """
            Test case 3: ls /comp0010/test/dir1/hidden_dir1
        """

        ls = Ls([self.HIDDENDIR1], deque())
        ls.exec()
        output_lines = [line.strip() for line in ls.output]
        expected_lines = [
            "file1.txt",
            "file2.txt"
        ]

        self.assertEqual(set(output_lines), set(expected_lines))

    def test_ls4(self):
        """
            Test case 4: ls /comp0010/test/dir1/hidden_dir1/*.txt
        """

        output_lines = input_factory(f"ls {self.HIDDENDIR1}/*.txt",
                                     Converter()
                                     )
        expected_lines = [
            "/comp0010/test/dir1/hidden_dir1/file1.txt",
            "/comp0010/test/dir1/hidden_dir1/file2.txt"
        ]
        output_set = [line.strip() for line in output_lines]

        self.assertEqual(set(output_set), set(expected_lines))

    def test_ls5(self):
        """
            Test case 5: ls /non_existent
        """

        with self.assertRaises(FileNotFoundError):
            ls = Ls([self.NONEXISTENT], deque())
            ls.exec()
