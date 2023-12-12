import unittest

from src.commands.Call import Call


class TestCall(unittest.TestCase):
    def test_call1(self):
        """
            Test case 1: echo hello world
        """

        call = Call("echo", ["hello", "world"], None, None)
        call.eval()
        self.assertEqual(call.output.popleft().strip(), "hello world")

    def test_call2(self):
        """
           Test case 2: find /comp0010/test/dir1 -name '*.py'
        """

        call = Call("find", ["/comp0010/test/dir1", "-name", "*.py"],
                    None, None)
        call.eval()
        output_lines = [line.strip() for line in call.output]
        expected_lines = [
            "/comp0010/test/dir1/hidden_dir2/file1.py",
            "/comp0010/test/dir1/hidden_dir2/file2.py"
        ]
        self.assertEqual(output_lines, expected_lines)

    def test_call3(self):
        """
            Test case 3: ls /comp0010/test/dir1
        """

        call = Call("ls", ["/comp0010/test/dir1"], None, None)
        call.eval()
        output_lines = [line.strip() for line in call.output]
        expected_lines = [
            "hidden_dir1",
            "hidden_dir2"
        ]
        self.assertEqual(set(output_lines), set(expected_lines))

    def test_call4(self):
        """
            Test case 4: cat non_existent
        """

        with self.assertRaises(FileNotFoundError):
            call = Call("cat", ["non_existent"], None, None)
            call.eval()

    def test_call5(self):
        """
            Test case 5: find . -name '*.txt' '*.py'
        """

        with self.assertRaises(ValueError):
            call = Call("find", [".", "-name", "*.txt", "*.py"], None, None)
            call.eval()

    def test_call6(self):
        """
            Test case 6: unsupported_application "hello"
        """
        with self.assertRaises(ValueError):
            call = Call("unsupported_application", ["hello"], None, None)
            call.eval()
