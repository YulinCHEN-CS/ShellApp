import os
import unittest

from src.commands.Call import Call
from antlr.Converter import Converter
from factories.input_factory import input_factory


class TestUnsafeCall(unittest.TestCase):
    ROOTDIR = "/"
    HOMEDIR = "/comp0010"
    os.chdir("/")  # Reset the current working directory

    def test_unsafe_cat1(self):
        """
            Test case 1:
                _cat
        """
        call = Call("_cat", [], None, None)
        call.eval()
        self.assertFalse(call.output)

    def test_unsafe_cat2(self):
        """
            Test case 2:
                _cat non_exist.txt
        """
        call = Call("_cat", ['non_exist.txt'], None, None)
        call.eval()
        self.assertEqual(call.output.popleft().strip(),
                         "Error: File not found: non_exist.txt")

    def test_unsafe_cat3(self):
        """
            Test case 3:
            _cat /comp0010/test/dir2/emptyfile_testing_case.txt non_exist.txt
        """
        call = Call(
                    "_cat",
                    ['/comp0010/test/dir2/emptyfile_testing_case.txt',
                     'non_exist.txt'],
                    None,
                    None
        )
        call.eval()
        self.assertEqual(call.output.popleft().strip(),
                         "Error: File not found: non_exist.txt")

    def test_unsafe_cat4(self):
        """
            Test case 4:
                _cat /comp0010/test/dir2/emptyfile_testing_case.txt
        """
        call = Call(
                    "_cat",
                    ['/comp0010/test/dir2/emptyfile_testing_case.txt'],
                    None,
                    None
        )
        call.eval()
        self.assertFalse(call.output)

    def test_unsafe_cd1(self):
        """
            Test case 1:
                cd /comp0010
        """

        call = Call("_cd", [self.HOMEDIR], None, None)
        call.eval()
        self.assertEqual(os.getcwd(), self.HOMEDIR)
        os.chdir("/")  # Reset the current working directory

    def test_unsafe_cd2(self):
        """
            Test case 2:
                _cd non-existent-directory
        """

        call = Call("_cd", ["non-existent-directory"], None, None)
        call.eval()

        self.assertEqual(
            call.output.popleft().strip(),
            "Error: Directory not found"
        )
        os.chdir("/")  # Reset the current working directory

    def test_unsafe_cd3(self):
        """
            Test case 3:
                _cd more than one directory
        """

        call = Call("_cd", ["more", "than", "one", "directory"], None, None)
        call.eval()

        self.assertEqual(
            call.output.popleft().strip(),
            "Error: cd requires exactly one argument"
        )
        os.chdir("/")  # Reset the current working directory

    def test_unsafe_echo1(self):
        """
            Test case 1:
                _echo "hello world"
        """

        call = Call("_echo", ["hello world"], None, None)
        call.eval()

        self.assertEqual(
            call.output.popleft().strip(), "hello world"
        )

    def test_unsafe_echo2(self):
        """
            Test case 2:
                _echo hello world
        """

        call = Call("_echo", ["hello", "world"], None, None)
        call.eval()

        self.assertEqual(
            call.output.popleft().strip(), "hello world")

    def test_unsafe_find1(self):
        """
           Test case 2:
               find /comp0010/test/dir1 -name '*.py'
        """

        TESTDIR = "/comp0010/test/dir1"
        call = Call("_find", [TESTDIR, "-name", "*.py"], None, None)
        call.eval()
        output_lines = [line.strip() for line in call.output]
        expected_lines = [
            "/comp0010/test/dir1/hidden_dir2/file1.py",
            "/comp0010/test/dir1/hidden_dir2/file2.py"
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_unsafe_find2(self):
        """
            Test case 3:
                find non_existent -name '*.txt'
        """

        TESTDIR = "non_existent"
        call = Call("_find", [TESTDIR, "-name", "*.txt"], None, None)
        call.eval()

        self.assertEqual(call.output.popleft().strip(),
                         "Error: Directory not found: non_existent")

    def test_unsafe_find3(self):
        """
            Test case 4:
                find . -name '*.txt' '*.py'
        """

        call = Call("_find",
                    [".", "-name", "*.txt", "*.py"],
                    None,
                    None)
        call.eval()

        self.assertEqual(call.output.popleft().strip(),
                         "Error: Usage: find [PATH] -name 'PATTERN'")

    def test_unsafe_head1(self):
        """
            Test case 1:
                _head -n 5 /comp0010/test/dir2/head_tail_testing_case.txt
        """

        TESTDIR = "/comp0010/test/dir2/head_tail_testing_case.txt"
        call = Call("_head", ["-n", "5", TESTDIR], None, None)
        call.eval()
        # Strip each line in the deque
        output_lines = [line.strip() for line in call.output]
        expected_lines = [
            "Line 1: The quick brown fox jumps over the lazy dog.",
            "Line 2: Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Line 3: Sed do eiusmod tempor incididunt "
            "ut labore et dolore magna aliqua.",
            "Line 4: Ut enim ad minim veniam, quis nostrud "
            "exercitation ullamco laboris.",
            "Line 5: Nisi ut aliquip ex ea commodo consequat."
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_unsafe_head2(self):
        """
            Test case 2:
                _head -n /comp0010/test/dir2/head_tail_testing_case.txt
        """

        TESTDIR = "/comp0010/test/dir2/head_tail_testing_case.txt"
        call = Call("_head", ["-n", TESTDIR], None, None)
        call.eval()

        self.assertEqual(
            call.output.popleft().strip(),
            "Error: Incorrect number of command line arguments or flags"
        )

    def test_unsafe_head3(self):
        """
            Test case 2:
                _head -n 5 non_existent.txt
        """

        TESTDIR = "non_existent.txt"
        call = Call("_head", ["-n", "5", TESTDIR], None, None)
        call.eval()

        self.assertEqual(call.output.popleft().strip(),
                         "Error: File not found: non_existent.txt")

    def test_unsafe_ls1(self):
        """
           Test case 1:
               ls /comp0010/test/dir1
        """

        TESTDIR = "/comp0010/test/dir1"
        call = Call("_ls", [TESTDIR], None, None)
        call.eval()
        output_lines = [line.strip() for line in call.output]
        expected_lines = [
            "hidden_dir1",
            "hidden_dir2"
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_unsafe_ls2(self):
        """
           Test case 2:
               ls /comp0010/test/dir1/*
        """

        TESTDIR = "/comp0010/test/dir1"
        output_lines = input_factory(f"_ls {TESTDIR}/*", Converter())
        expected_lines = {
            "/comp0010/test/dir1/hidden_dir1",
            "/comp0010/test/dir1/hidden_dir2"
        }
        output_set = {line.strip() for line in output_lines}

        self.assertEqual(output_set, expected_lines)

    def test_unsafe_ls3(self):
        """
           Test case 3:
               ls non-exist-directory
        """

        TESTDIR = "non-exist-directory"
        call = Call("_ls", [TESTDIR], None, None)
        call.eval()

        self.assertEqual(call.output.popleft().strip(),
                         "Error: Directory not found: non-exist-directory")

    def test_unsafe_pwd(self):
        """
            Test case 1:
                _pwd
        """

        call = Call("_pwd", [], None, None)
        call.eval()

        self.assertEqual(call.output.popleft().strip(), os.getcwd())

    def test_unsafe_tail1(self):
        """
            Test case 1:
                tail -n 5 /comp0010/test/dir2/head_tail_testing_case.txt
        """

        TESTDIR = "/comp0010/test/dir2/head_tail_testing_case.txt"
        call = Call("_tail", ["-n", "5", TESTDIR], None, None)
        call.eval()
        output_lines = [line.strip()
                        for line in call.output
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
            "diam libero molestie quam, in imperdiet tortor magna id neque."
        ]

        self.assertEqual(output_lines, expected_lines)

    def test_unsafe_tail2(self):
        """
            Test case 2:
                _tail -n /comp0010/test/dir2/head_tail_testing_case.txt
        """

        TESTDIR = "/comp0010/test/dir2/head_tail_testing_case.txt"
        call = Call("_tail", ["-n", TESTDIR], None, None)
        call.eval()

        self.assertEqual(
            call.output.popleft().strip(),
            "Error: Incorrect number of command line arguments or flags"
        )

    def test_unsafe_tail3(self):
        """
            Test case 3:
                _tail -n 5 non_existent.txt
        """

        TESTDIR = "non_existent.txt"
        call = Call("_tail", ["-n", "5", TESTDIR], None, None)
        call.eval()

        self.assertEqual(
            call.output.popleft().strip(),
            "Error: File not found: non_existent.txt"
        )

    def test_unsafe_sort1(self):
        """
            Test case 1:
                _sort /comp0010/test/dir2/sort_testing_case.txt
        """

        TESTDIR = "/comp0010/test/dir2/sort_testing_case.txt"
        call = Call("_sort", [TESTDIR], None, None)
        call.eval()
        output_lines = [line.strip() for line in call.output]
        expected_lines = ['abjrknerjkln', 'bf3ijf4', 'pkeml4m', 'zeiorjeo']

        self.assertEqual(output_lines, expected_lines)

    def test_unsafe_sort2(self):
        """
            Test case 2:
                _sort -r /comp0010/test/dir2/sort_testing_case.txt
        """

        TESTDIR = "/comp0010/test/dir2/sort_testing_case.txt"
        call = Call("_sort", ["-r", TESTDIR], None, None)
        call.eval()
        output_lines = [line.strip() for line in call.output]
        expected_lines = ['zeiorjeo', 'pkeml4m', 'bf3ijf4', 'abjrknerjkln']

        self.assertEqual(output_lines, expected_lines)

    def test_unsafe_sort3(self):
        """
            Test case 3:
                _sort -r non-exist.txt
        """

        TESTDIR = "non-exist.txt"
        call = Call("_sort", ["-r", TESTDIR],
                    None, None)
        call.eval()

        self.assertEqual(call.output.popleft().strip(),
                         "Error: File not found")

    def test_unsafe_sort4(self):
        """
            Test case 4:
                _sort -n -r non-exist.txt
        """

        TESTDIR = "non-exist.txt"
        call = Call("_sort", ["-n", "-r", TESTDIR],
                    None, None)
        call.eval()

        self.assertEqual(call.output.popleft().strip(),
                         "Error: Incorrect number of "
                         "command line arguments or flags")

    def test_unsafe_sort5(self):
        """
            Test case 5:
                _sort non-exist.txt non-exist.txt
        """

        TESTDIR = "non-exist.txt"
        call = Call("_sort", [TESTDIR, TESTDIR], None, None)
        call.eval()

        self.assertEqual(
            call.output.popleft().strip(),
            "Error: Incorrect number of command line arguments or flags"
        )

    def test_unsafe_uniq1(self):
        """
            Test case 1:
                _uniq /comp0010/test/dir2/uniq_testing_case.txt
        """

        TESTDIR = "/comp0010/test/dir2/uniq_testing_case.txt"
        call = Call("_uniq", [TESTDIR],
                    None, None)
        call.eval()
        output_lines = [line.strip() for line in call.output]
        expected_lines = ['hello', 'hhhhhh',
                          'ssssss', 'SSSSSs',
                          'hhhhhh', 'python',
                          'true', 'false',
                          'ssssss', 'HHHHHH']
        self.assertEqual(output_lines, expected_lines)

    def test_unsafe_uniq2(self):
        """
            Test case 2:
                _uniq -i /comp0010/test/dir2/uniq_testing_case.txt
        """

        TESTDIR = "/comp0010/test/dir2/uniq_testing_case.txt"
        call = Call("_uniq", ["-i", TESTDIR], None, None)
        call.eval()
        output_lines = [line.strip() for line in call.output]
        expected_lines = ['HELLO', 'HHHHHH', 'SSSSSS', 'HHHHHH',
                          'PYTHON', 'TRUE', 'FALSE', 'SSSSSS', 'HHHHHH']

        self.assertEqual(output_lines, expected_lines)

    def test_unsafe_uniq3(self):
        """
            Test case 3:
                _uniq -d /comp0010/test/dir2/uniq_testing_case.txt
        """

        TESTDIR = "/comp0010/test/dir2/uniq_testing_case.txt"
        call = Call("_uniq", ["-d", TESTDIR], None, None)
        call.eval()

        self.assertEqual(call.output.popleft().strip(),
                         "Error: File not found: -d")

    def test_unsafe_uniq4(self):
        """
            Test case 4:
                _uniq -i non-exist.txt
        """

        TESTDIR = "non-exist.txt"
        call = Call("_uniq", ["-i", TESTDIR], None, None)
        call.eval()

        self.assertEqual(
            call.output.popleft().strip(),
            "Error: File not found: non-exist.txt"
        )
