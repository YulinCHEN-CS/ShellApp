import os
import unittest
from collections import deque

from src.applications.Cd import Cd


class TestCd(unittest.TestCase):
    ROOTDIR = "/"
    HOMEDIR = "/comp0010"
    TESTDIR = "/comp0010/src/applications"
    os.chdir("/")  # Reset the current working directory

    def test_cd1(self):
        """
            Test case 1: cd /comp0010
        """

        cd = Cd([f"{self.HOMEDIR}"], deque())
        cd.exec()

        self.assertEqual(os.getcwd(), self.HOMEDIR)

    def test_cd2(self):
        """
            Test case 2: cd ..
        """

        cd = Cd([".."], deque())
        cd.exec()

        self.assertEqual(os.getcwd(), self.ROOTDIR)

    def test_cd3(self):
        """
            Test case 3: cd comp0010
        """

        cd = Cd(["comp0010"], deque())
        cd.exec()

        self.assertEqual(os.getcwd(), self.HOMEDIR)

    def test_cd4(self):
        """
            Test case 4: cd /comp0010/src/applications
        """

        cd = Cd([self.TESTDIR], deque())
        cd.exec()

        self.assertEqual(os.getcwd(), self.TESTDIR)

    def test_cd5(self):
        """
            Test case 5: cd Cd.py
        """

        with self.assertRaises(NotADirectoryError):
            cd = Cd(["Cd.py"], deque())
            cd.exec()

    def test_cd6(self):
        """
            Test case 6: cd non_existent_directory
        """

        with self.assertRaises(FileNotFoundError):
            cd = Cd(["non_existent_directory"], deque())
            cd.exec()

    def test_cd7(self):
        """
            Test case 7: cd
        """
        with self.assertRaises(ValueError):
            cd = Cd([], deque())
            cd.exec()
