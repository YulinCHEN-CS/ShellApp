import os
import unittest
from collections import deque

from src.applications.Grep import Grep


class TestGrep(unittest.TestCase):
    TESTDIR = "/comp0010/test/dir2"
    NONEXISTENT = "non_existent.txt"
    os.chdir("/")  # Reset the current working directory

    def test_Grep1(self):
        """
            Test case 1:
                grep AAA
        """

        grep = Grep(["AAA"], deque())
        with self.assertRaises(ValueError):
            grep.exec()

    def test_Grep2(self):
        """
            Test case 2:
                grep AAA /comp0010/test/dir2/grep_testing_case.txt
        """

        grep = Grep(
            ["AAA", self.TESTDIR + "/grep_testing_case.txt"],
            deque()
        )
        grep.exec()

        self.assertEqual(grep.output.popleft().strip(), "AAA BBB AAA")

    def test_Grep3(self):
        """
            Test case 3:
                grep AAA /comp0010/test/dir2/grep_testing_case.txt
                /comp0010/test/dir2/grep_testing_case2.txt
        """
        grep = Grep(
            [
                "AAA", self.TESTDIR + "/grep_testing_case.txt",
                self.TESTDIR + "/grep_testing_case2.txt"
             ],
            deque()
        )
        grep.exec()
        output_lines = [line.strip() for line in grep.output]
        expected_lines = [
            "/comp0010/test/dir2/grep_testing_case.txt:AAA BBB AAA"
        ]

        self.assertEqual(set(output_lines), set(expected_lines))

    def test_Grep4(self):
        """
            Test case 4:
            grep ZZZZZ /comp0010/test/dir2/grep_testing_case.txt
                /comp0010/test/dir2/grep_testing_case2.txt
        """

        grep = Grep(
            [
                "ZZZZZ", self.TESTDIR + "/grep_testing_case.txt",
                self.TESTDIR + "/grep_testing_case2.txt"
            ],
            deque()
        )
        with self.assertRaises(ValueError):
            grep.exec()

    def test_Grep6(self):
        """
            Test case 6:
                grep AAA /comp0010/test/dir2/grep_testing_case.txt
                /comp0010/test/dir2/grep_testing_case2.txt
                /comp0010/test/dir2/grep_testing_case.txt
        """

        grep = Grep(
            [
                "AAA", self.TESTDIR + "/grep_testing_case.txt",
                self.TESTDIR + "/grep_testing_case2.txt",
                self.TESTDIR + "/grep_testing_case.txt"
            ],
            deque()
        )
        grep.exec()
        output_lines = [line.strip() for line in grep.output]
        expected_lines = [
            "/comp0010/test/dir2/grep_testing_case.txt:AAA BBB AAA",
            "/comp0010/test/dir2/grep_testing_case.txt:AAA BBB AAA"
        ]

        self.assertEqual(set(output_lines), set(expected_lines))

    def test_Grep7(self):
        """
            Test case 7:
                grep AAA /non_existent.txt
                /comp0010/test/dir2/grep_testing_case.txt
        """

        grep = Grep(
            [
                "AAA", self.NONEXISTENT,
                self.TESTDIR + "/grep_testing_case.txt"
            ],
            deque()
        )
        with self.assertRaises(FileNotFoundError):
            grep.exec()
