import unittest

from antlr.Converter import Converter
from factories.input_factory import input_factory


class TestGlob(unittest.TestCase):
    def test_glob1(self):
        """
            Test case 1: ls /comp0010/test/dir1/*
        """
        output = input_factory("ls /comp0010/test/dir1/*", Converter())
        expected_lines = [
            "/comp0010/test/dir1/hidden_dir1",
            "/comp0010/test/dir1/hidden_dir2"
        ]
        output_lines = [line.strip() for line in output]
        self.assertEqual(set(output_lines), set(expected_lines))

    def test_glob2(self):
        """
            Test case 2: echo non_existent/*
        """
        output = input_factory("echo non_existent/*", Converter())
        self.assertEqual(output.popleft().strip(), "non_existent/*")

    def test_glob3(self):
        """
            Test case 3: ls /comp0010/test/dir1/hidden_dir1/*.txt
        """
        output = input_factory("ls /comp0010/test/dir1/hidden_dir1/*.txt",
                               Converter()
                               )
        expected_lines = [
            "/comp0010/test/dir1/hidden_dir1/file1.txt",
            "/comp0010/test/dir1/hidden_dir1/file2.txt"
        ]
        output_lines = [line.strip() for line in output]
        self.assertEqual(set(output_lines), set(expected_lines))

    def test_glob4(self):
        """
            Test case 4: ls /comp0010/test/dir2/grep?
        """
        output = input_factory("ls /comp0010/test/dir2/grep?", Converter())
        expected_lines = [
            "/comp0010/test/dir2/grep_testing_case.txt",
            "/comp0010/test/dir2/grep_testing_case2.txt"
        ]
        output_lines = [line.strip() for line in output]
        self.assertEqual(set(output_lines), set(expected_lines))

    def test_glob5(self):
        """
            Test case 5: ls /comp0010/test/*/*.txt
        """
        output = input_factory("ls /comp0010/test/*/*.txt", Converter())
        expected_lines = [
            "/comp0010/test/dir2/grep_testing_case2.txt",
            "/comp0010/test/dir2/uniq_testing_case.txt",
            "/comp0010/test/dir2/emptyfile_testing_case.txt",
            "/comp0010/test/dir2/redir_testing_in_case.txt",
            "/comp0010/test/dir2/head_tail_testing_case.txt",
            "/comp0010/test/dir2/sort_testing_case.txt",
            "/comp0010/test/dir2/grep_testing_case.txt",
            "/comp0010/test/dir2/redir_testing_out_case.txt"
        ]
        output_lines = [line.strip() for line in output]
        self.assertEqual(set(output_lines), set(expected_lines))

    def test_glob6(self):
        """
            Test case 6: echo /comp0010/test/dir1/hidden_dir1/*.unknown
        """
        output = input_factory(
            "echo /comp0010/test/dir1/hidden_dir1/*.unknown",
            Converter()
            )
        self.assertEqual(output.popleft().strip(),
                         "/comp0010/test/dir1/hidden_dir1/*.unknown"
                         )
