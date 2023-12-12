import os
import unittest
from collections import deque

from src.applications.Pwd import Pwd


class TestPwd(unittest.TestCase):

    def test_pwd(self):
        """
            Test case 1: pwd
        """
        pwd = Pwd([], deque())
        pwd.exec()

        self.assertEqual(pwd.output.popleft().strip(), os.getcwd().strip())
