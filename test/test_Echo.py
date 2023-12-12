import unittest
from collections import deque

from src.applications.Echo import Echo


class TestEcho(unittest.TestCase):
    def test_echo1(self):
        """
            Test case 1: echo "hello world"
        """

        echo = Echo(["hello world"], deque())
        echo.exec()
        self.assertEqual(echo.output.popleft().strip(), "hello world")

    def test_echo2(self):
        """
            Test case 2: echo hello world
        """

        echo = Echo(["hello", "world"], deque())
        echo.exec()

        self.assertEqual(echo.output.popleft().strip(), "hello world")

    def test_echo3(self):
        """
            Test case 3: echo "hello world" "hello world"
        """

        echo = Echo(["hello world", "hello world"], deque())
        echo.exec()

        self.assertEqual(echo.output.popleft().strip(),
                         "hello world hello world")

    def test_echo4(self):
        """
            Test case 4: echo
        """

        echo = Echo([], deque())
        echo.exec()
        self.assertFalse(echo.output)

    def test_echo5(self):
        """
            Test case 5: echo "" "hello world"
        """

        echo = Echo(["", "hello world"], deque())
        echo.exec()
        self.assertEqual(echo.output.popleft().strip(),
                         "hello world")
