import os
import unittest
from collections import deque

from src.applications.Find import Find


class TestFind(unittest.TestCase):
    TESTDIR = "/comp0010/test/dir1"
    HIDDENDIR1 = "/comp0010/test/dir1/hidden_dir1"
    HIDDENDIR2 = "/comp0010/test/dir1/hidden_dir2"
    NONEXISTENT = "/non_existent"
    os.chdir("/")  # Reset the current working directory

    def test_find1(self):
        """
            Test case 1: find . -name '*.txt'
        """
        os.chdir("/comp0010")  # Reset the current working directory

        find = Find([".", "-name", "*.txt"], deque())
        find.exec()
        output_lines = [line.strip() for line in find.output]
        expected_lines = [
            "./requirements.txt",
            "./history_file.txt",
            "./test/dir2/grep_testing_case2.txt",
            "./test/dir2/sort_testing_case.txt",
            "./test/dir2/redir_testing_in_case.txt",
            "./test/dir2/redir_testing_out_case.txt",
            "./test/dir2/grep_testing_case.txt",
            "./test/dir2/head_tail_testing_case.txt",
            "./test/dir2/uniq_testing_case.txt",
            "./test/dir2/emptyfile_testing_case.txt",
            "./test/dir1/hidden_dir1/file2.txt",
            "./test/dir1/hidden_dir1/file1.txt"
        ]

        self.assertEqual(set(output_lines), set(expected_lines))

    def test_find2(self):
        """
            Test case 2: find /comp0010/test/dir1 -name '*.py'
        """

        find = Find([self.TESTDIR, "-name", "*.py"], deque())
        find.exec()
        output_lines = [line.strip() for line in find.output]
        expected_lines = [
            "/comp0010/test/dir1/hidden_dir2/file1.py",
            "/comp0010/test/dir1/hidden_dir2/file2.py"
        ]

        self.assertEqual(set(output_lines), set(expected_lines))

    def test_find3(self):
        """
            Test case 3: find non_existent -name '*.txt'
        """

        with self.assertRaises(FileNotFoundError):
            find = Find([self.NONEXISTENT, "-name", "*.txt"], deque())
            find.exec()

    def test_find4(self):
        """
            Test case 4: find . -name '*.txt' '*.py'
        """

        with self.assertRaises(ValueError):
            find = Find([".", "-name", "*.txt", "*.py"], deque())
            find.exec()

    def test_find5(self):
        """
            Test case 5: find /comp0010/test/dir1/hidden_dir1 -name 'file1.txt'
        """

        find = Find([self.HIDDENDIR1, "-name", "file1.txt"], deque())
        find.exec()

        self.assertEqual(find.output.popleft().strip(),
                         "/comp0010/test/dir1/hidden_dir1/file1.txt"
                         )

    def test_find6(self):
        """
            Test case 6: find /comp0010/test/dir1/hidden_dir1
                         -name 'non_existent.txt'
        """

        find = Find([self.HIDDENDIR1, "-name", "non_existent.txt"], deque())

        self.assertFalse(find.output)

    def test_find7(self):
        """
            Test case 7: find -name *.py
        """
        os.chdir(self.TESTDIR)  # Reset the current working directory
        find = Find(["-name", "*.py"], deque())
        find.exec()
        output_lines = [line.strip() for line in find.output]
        expected_lines = [
            "./hidden_dir2/file1.py",
            "./hidden_dir2/file2.py"
        ]
        self.assertEqual(set(output_lines), set(expected_lines))
