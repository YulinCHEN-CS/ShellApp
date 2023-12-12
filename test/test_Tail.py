import os
import unittest

from collections import deque
from src.applications.Tail import Tail


class TestTail(unittest.TestCase):

    TESTDIR = "/comp0010/test/dir2/head_tail_testing_case.txt"
    NONEXISTENT = "non_existent.txt"
    EMPTYFILE = "/comp0010/test/dir2/emptyfile_testing_case.txt"
    os.chdir("/")  # Reset the current working directory

    def test_tail1(self):
        """
            Test case 1:
                tail /comp0010/test/dir2/head_tail_testing_case.txt
        """

        tail = Tail([self.TESTDIR], deque())
        tail.exec()
        output_lines = [line.strip() for line in tail.output
                        if line.strip() != '']
        expected_lines = [
            "Line 11: Aliquam erat volutpat. Aliquam euismod massa est, "
            "sed fermentum nunc scelerisque vitae.",
            "Line 12: Nulla ultrices elit sed ante consectetur, "
            "sed lacinia nisl pretium.",
            "Line 13: Donec ultricies, libero ut ultricies vehicula, "
            "sem risus aliquam tellus, nec molestie nisi urna sit amet mi.",
            "Line 14: Sed non leo euismod, aliquet magna quis, lacinia nisi.",
            "Line 15: Donec euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 16: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 17: Donec euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 18: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 19: Donec euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 20: Sed euismod, nunc id aliquam ultrices,"
            " diam libero molestie quam, in imperdiet tortor magna id neque."
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_tail2(self):
        """
            Test case 2:
                tail -n 5 /comp0010/test/dir2/head_tail_testing_case.txt
        """

        tail = Tail(["-n", "5", self.TESTDIR], deque())
        tail.exec()
        output_lines = [line.strip() for line in tail.output
                        if line.strip() != '']
        expected_lines = [
            "Line 16: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 17: Donec euismod, nunc id aliquam ultrices,"
            " diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 18: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 19: Donec euismod, nunc id aliquam ultrices,"
            " diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 20: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque."
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_tail3(self):
        """
            Test case 3:
                tail -n 5 /comp0010/test/dir2/head_tail_testing_case.txt
                        /comp0010/test/dir2/head_tail_testing_case.txt
        """

        tail = Tail(["-n", "5", self.TESTDIR, self.TESTDIR], deque())
        tail.exec()
        output_lines = [line.strip() for line in tail.output
                        if line.strip() != '']
        expected_lines = [
            "Line 16: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 17: Donec euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 18: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 19: Donec euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 20: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 16: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 17: Donec euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 18: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 19: Donec euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque.",
            "Line 20: Sed euismod, nunc id aliquam ultrices, "
            "diam libero molestie quam, in imperdiet tortor magna id neque."
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_tail4(self):
        """
            Test case 4:
                tail -n 0 /comp0010/test/dir2/head_tail_testing_case.txt
        """

        tail = Tail(["-n", "0", self.TESTDIR], deque())
        tail.exec()

        self.assertFalse(tail.output)

    def test_tail5(self):
        """
            Test case 5:
                tail /comp0010/test/dir2/emptyfile_testing_case.txt
        """

        tail = Tail([self.EMPTYFILE], deque())
        tail.exec()

        self.assertFalse(tail.output)

    def test_tail6(self):
        """
            Test case 6:
                tail -n -5 /comp0010/test/dir2/head_tail_testing_case.txt
        """

        with self.assertRaises(ValueError):
            tail = Tail(["-n", "-5", self.TESTDIR], deque())
            tail.exec()

    def test_tail7(self):
        """
            Test case 7:
                tail non_existent.txt
        """

        with self.assertRaises(FileNotFoundError):
            tail = Tail([self.NONEXISTENT], deque())
            tail.exec()

    def test_tail8(self):
        """
            Test case 8:
                tail -n 5 non_existent.txt
        """

        with self.assertRaises(FileNotFoundError):
            tail = Tail(["-n", "5", self.NONEXISTENT], deque())
            tail.exec()

    def test_tail9(self):
        """
            Test case 9:
                tail -e 5 /comp0010/test/dir2/head_tail_testing_case.txt
        """

        with self.assertRaises(ValueError):
            tail = Tail(["-e", "5", self.TESTDIR], deque())
            tail.exec()
