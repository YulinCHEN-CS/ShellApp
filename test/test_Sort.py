import unittest
from src.applications.Sort import Sort
from collections import deque


class TestSort(unittest.TestCase):
    def test_sort1(self):
        """
            Test case 1: sort /comp0010/test/dir2/sort_testing_case.txt
        """
        sort = Sort(['/comp0010/test/dir2/sort_testing_case.txt'], deque())
        sort.exec()
        output_lines = [line.strip() for line in sort.output]
        expected_lines = ['abjrknerjkln', 'bf3ijf4', 'pkeml4m', 'zeiorjeo']
        self.assertEqual(output_lines, expected_lines)

    def test_sort2(self):
        """
            Test case 2: sort -r /comp0010/test/dir2/sort_testing_case.txt
        """
        sort = Sort(['-r',
                     '/comp0010/test/dir2/sort_testing_case.txt'],
                    deque())
        sort.exec()
        output_lines = [line.strip() for line in sort.output]
        expected_lines = ['zeiorjeo', 'pkeml4m', 'bf3ijf4', 'abjrknerjkln']
        self.assertEqual(output_lines, expected_lines)

    def test_sort3(self):
        """
            Test case 3: sort /comp0010/test/dir2/non-exist.txt
        """
        sort = Sort(['/comp0010/test/dir2/non-exist.txt'], deque())
        with self.assertRaises(FileNotFoundError):
            sort.exec()

    def test_sort4(self):
        """
            Test case 4: sort -r test/dir2/non-exist.txt
        """
        sort = Sort(['-r', 'test/dir2/non-exist.txt'], deque())
        with self.assertRaises(FileNotFoundError):
            sort.exec()

    def test_sort5(self):
        """
            Test case 5: sort -r /comp0010/test/dir2/sort_testing_case.txt
            /comp0010/test/dir2/sort_testing_case.txt
        """
        sort = Sort(['-r',
                     '/comp0010/test/dir2/sort_testing_case.txt',
                     '/comp0010/test/dir2/sort_testing_case.txt'], deque())
        with self.assertRaises(ValueError):
            sort.exec()

    def test_sort6(self):
        """
            Test case 6: sort /comp0010/test/dir2/sort_testing_case.txt -r
        """
        sort = Sort(['test/dir2/non-exist.txt', '-r'], deque())
        with self.assertRaises(ValueError):
            sort.exec()
