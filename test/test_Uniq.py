import unittest
from collections import deque

from src.applications.Uniq import Uniq


class TestSort(unittest.TestCase):

    def test_uniq1(self):
        """
           Test case 1: uniq
        """
        uniq = Uniq([], deque())
        with self.assertRaises(ValueError):
            uniq.exec()

    def test_uniq2(self):
        """
            Test case 2: uniq /comp0010/test/dir2/emptyfile_testing_case.txt
        """
        uniq = Uniq(['/comp0010/test/dir2/emptyfile_testing_case.txt'],
                    deque())
        uniq.exec()
        self.assertFalse(uniq.output)

    def test_uniq3(self):
        """
            Test case 3: uniq /comp0010/test/dir2/uniq_testing_case.txt
        """
        uniq = Uniq(['/comp0010/test/dir2/uniq_testing_case.txt'], deque())
        uniq.exec()
        output_lines = [line.strip() for line in uniq.output]
        expected_lines = ['hello', 'hhhhhh',
                          'ssssss', 'SSSSSs',
                          'hhhhhh', 'python',
                          'true', 'false',
                          'ssssss', 'HHHHHH']
        self.assertEqual(output_lines, expected_lines)

    def test_uniq4(self):
        """
            Test case 4: uniq -i /comp0010/test/dir2/uniq_testing_case.txt
        """
        uniq = Uniq(['-i', '/comp0010/test/dir2/uniq_testing_case.txt'],
                    deque())
        uniq.exec()
        output_lines = [line.strip() for line in uniq.output]
        expected_lines = ['HELLO', 'HHHHHH',
                          'SSSSSS', 'HHHHHH',
                          'PYTHON', 'TRUE',
                          'FALSE', 'SSSSSS',
                          'HHHHHH']
        self.assertEqual(output_lines, expected_lines)

    def test_uniq5(self):
        """
            Test case 5: uniq -i non-exist.txt
        """
        uniq = Uniq(['-i', 'non-exist.txt'], deque())
        with self.assertRaises(FileNotFoundError):
            uniq.exec()

    def test_uniq6(self):
        """
            Test case 6: uniq -i non-exist.txt
                        /comp0010/test/dir2/uniq_testing_case.txt
        """
        uniq = Uniq(['non-exist.txt',
                     '/comp0010/test/dir2/uniq_testing_case.txt'],
                    deque())
        with self.assertRaises(FileNotFoundError):
            uniq.exec()
