import os
import unittest
from collections import deque

from src.applications.Head import Head


class TestHead(unittest.TestCase):
    TESTDIR = "/comp0010/test/dir2/head_tail_testing_case.txt"
    NONEXISTENT = "non_existent.txt"
    EMPTYFILE = "/comp0010/test/dir2/emptyfile_testing_case.txt"
    os.chdir("/")  # Reset the current working directory

    def test_head1(self):
        """
            Test case 1:
                head /comp0010/test/dir2/head_tail_testing_case.txt
        """

        head = Head([self.TESTDIR], deque())
        head.exec()
        # Strip each line in the deque
        output_lines = [line.strip() for line in head.output]
        expected_lines = [
            "Line 1: The quick brown fox jumps over the lazy dog.",
            "Line 2: Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Line 3: Sed do eiusmod tempor incididunt ut labore "
            "et dolore magna aliqua.",
            "Line 4: Ut enim ad minim veniam, quis nostrud "
            "exercitation ullamco laboris.",
            "Line 5: Nisi ut aliquip ex ea commodo consequat.",
            "Line 6: Duis aute irure dolor in "
            "reprehenderit in voluptate velit.",
            "Line 7: Esse cillum dolore eu fugiat nulla pariatur.",
            "Line 8: Excepteur sint occaecat cupidatat non proident.",
            "Line 9: Sunt in culpa qui officia "
            "deserunt mollit anim id est laborum.",
            "Line 10: Curabitur pretium tincidunt lacus, "
            "at viverra est semper sed."
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_head2(self):
        """
            Test case 2:
                head -n 5 /comp0010/test/dir2/head_tail_testing_case.txt
        """

        head = Head(["-n", "5", self.TESTDIR], deque())
        head.exec()
        # Strip each line in the deque
        output_lines = [line.strip() for line in head.output]
        expected_lines = [
            "Line 1: The quick brown fox jumps over the lazy dog.",
            "Line 2: Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Line 3: Sed do eiusmod tempor incididunt ut labore "
            "et dolore magna aliqua.",
            "Line 4: Ut enim ad minim veniam, quis nostrud "
            "exercitation ullamco laboris.",
            "Line 5: Nisi ut aliquip ex ea commodo consequat."
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_head3(self):
        """
            Test case 3:
            head -n 5 /comp0010/test/dir2/head_tail_testing_case.txt
                    /comp0010/test/dir2/head_tail_testing_case.txt
        """
        head = Head(["-n", "5", self.TESTDIR, self.TESTDIR], deque())
        head.exec()
        # Strip each line in the deque
        output_lines = [line.strip() for line in head.output]
        expected_lines = [
            "Line 1: The quick brown fox jumps over the lazy dog.",
            "Line 2: Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Line 3: Sed do eiusmod tempor incididunt "
            "ut labore et dolore magna aliqua.",
            "Line 4: Ut enim ad minim veniam, quis "
            "nostrud exercitation ullamco laboris.",
            "Line 5: Nisi ut aliquip ex ea commodo consequat.",
            "Line 1: The quick brown fox jumps over the lazy dog.",
            "Line 2: Lorem ipsum dolor sit amet, "
            "consectetur adipiscing elit.",
            "Line 3: Sed do eiusmod tempor incididunt "
            "ut labore et dolore magna aliqua.",
            "Line 4: Ut enim ad minim veniam, "
            "quis nostrud exercitation ullamco laboris.",
            "Line 5: Nisi ut aliquip ex ea commodo consequat."
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_head4(self):
        """
            Test case 4:
                head -n 0 /comp0010/test/dir2/head_tail_testing_case.txt
        """
        head = Head(["-n", "0", self.TESTDIR], deque())
        head.exec()

        self.assertFalse(head.output)

    def test_head5(self):
        """
            Test case 5:
                head non_existent.txt
        """
        with self.assertRaises(FileNotFoundError):
            head = Head([self.NONEXISTENT], deque())
            head.exec()

    def test_head6(self):
        """
            Test case 6:
                head -n 5 non_existent.txt
        """
        with self.assertRaises(FileNotFoundError):
            head = Head(["-n", "5", self.NONEXISTENT], deque())
            head.exec()

    def test_head7(self):
        """
            Test case 7:
                head /comp0010/test/dir2/emptyfile_testing_case.txt
        """
        head = Head([self.EMPTYFILE], deque())
        head.exec()

        self.assertFalse(head.output)

    def test_head8(self):
        """
            Test case 8:
                head -n -5 /comp0010/test/dir2/head_tail_testing_case.txt
        """
        with self.assertRaises(ValueError):
            head = Head(["-n", "-5", self.TESTDIR], deque())
            head.exec()

    def test_head9(self):
        """
            Test case 9:
                head -e 5 /comp0010/test/dir2/head_tail_testing_case.txt
        """
        with self.assertRaises(ValueError):
            head = Head(["-e", "5", self.TESTDIR], deque())
            head.exec()
