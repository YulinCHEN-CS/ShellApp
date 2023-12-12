import unittest
from src.applications.Cat import Cat
from collections import deque


class TestCat(unittest.TestCase):
    def test_cat1(self):
        """
            Test case 1: cat
        """
        cat = Cat([], deque())
        cat.exec()
        self.assertFalse(cat.output)

    def test_cat2(self):
        """
            Test case 2: cat non_exist.txt
        """
        cat = Cat(['non_exist.txt'], deque())
        with self.assertRaises(FileNotFoundError):
            cat.exec()

    def test_cat3(self):
        """
            Test case 3: cat /comp0010/test/dir2/emptyfile_testing_case.txt
                         non_exist.txt
        """
        cat = Cat(['/comp0010/test/dir2/emptyfile_testing_case.txt',
                   'non_exist.txt'], deque())
        with self.assertRaises(FileNotFoundError):
            cat.exec()

    def test_cat4(self):
        """
            Test case 4: cat /comp0010/test/dir2/emptyfile_testing_case.txt
        """
        cat = Cat(['/comp0010/test/dir2/emptyfile_testing_case.txt'], deque())
        cat.exec()
        self.assertFalse(cat.output)

    def test_cat5(self):
        """
            Test case 5: cat /comp0010/test/dir2/sort_testing_case.txt
        """
        cat = Cat(['/comp0010/test/dir2/sort_testing_case.txt'], deque())
        cat.exec()
        output_lines = [line.strip() for line in cat.output]
        expected_lines = ['zeiorjeo', 'abjrknerjkln', 'pkeml4m', 'bf3ijf4']
        self.assertEqual(output_lines, expected_lines)

    def test_cat6(self):
        """
            Test case 6: cat /comp0010/test/dir2/grep_testing_case.txt
                         /comp0010/test/dir2/sort_testing_case.txt
        """
        cat = Cat(['/comp0010/test/dir2/grep_testing_case.txt',
                   '/comp0010/test/dir2/sort_testing_case.txt'], deque())
        cat.exec()
        output_lines = [line.strip() for line in cat.output]
        expected_lines = ['AAA BBB AAA', 'zeiorjeo',
                          'abjrknerjkln', 'pkeml4m',
                          'bf3ijf4']
        self.assertEqual(output_lines, expected_lines)
