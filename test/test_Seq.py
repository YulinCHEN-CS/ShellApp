import unittest

from src.commands.Call import Call
from src.commands.Pipe import Pipe
from src.commands.Seq import Seq

from antlr.Converter import Converter
from factories.input_factory import input_factory


class TestSeq(unittest.TestCase):

    def test_seq1(self):
        """
            Test case 1:
                echo hello world ; echo user
        """
        left_command = Call("echo", ["hello", "world"], None, None)
        right_command = Call("echo", ["user"], None, None)
        seq = Seq([left_command, right_command])
        seq.eval()
        # remove newline characters
        output_lines = [
            line.strip() for line in seq.output if line.strip() != ""
        ]
        self.assertEqual(output_lines, ["hello world", "user"])

    def test_seq2(self):
        """
            Test case 2:
                echo hello world; echo user;
                uniq -i /comp0010/test/dir2/uniq_testing_case.txt
        """
        left_command = Call("echo", ["hello", "world"], None, None)
        middle_command = Call("echo", ["user"], None, None)
        right_command = Call(
            "uniq",
            ["-i", "/comp0010/test/dir2/uniq_testing_case.txt"],
            None,
            None
        )
        seq = Seq([left_command, middle_command, right_command])
        seq.eval()
        output_lines = [
            line.strip() for line in seq.output if line.strip() != ""
        ]
        expected_lines = [
            'hello world', 'user', 'HELLO', 'HHHHHH', 'SSSSSS',
            'HHHHHH', 'PYTHON', 'TRUE', 'FALSE', 'SSSSSS', 'HHHHHH'
        ]
        self.assertEqual(output_lines, expected_lines)

    def test_seq3(self):
        """
            Test case 3:
                cat /comp0010/test/dir2/uniq_testing_case.txt | sort | uniq ;
                echo "end of seq"
        """
        pipe_left_command = Call(
            "cat",
            ["/comp0010/test/dir2/uniq_testing_case.txt"],
            None,
            None
        )
        middle_command = Call("sort", [], None, None)
        right_command = Call("uniq", [], None, None)
        pipe_right_command = Pipe(middle_command, right_command)
        seq_left_command = Pipe(pipe_left_command, pipe_right_command)
        seq_right_command = Call("echo", ["end of seq"], None, None)
        seq = Seq([seq_left_command, seq_right_command])
        seq.eval()
        output_lines = [
            line.strip() for line in seq.output if line.strip() != ""
        ]
        expected_lines = [
            'HHHHHH', 'SSSSSs', 'false', 'hello',
            'hhhhhh', 'python', 'ssssss', 'true', 'end of seq'
        ]
        self.assertEqual(output_lines, expected_lines)

    def test_seq4(self):
        """
            Test case 4:
                cat /comp0010/test/dir2/uniq_testing_case.txt ;
                unsupported_command
        """
        with self.assertRaises(ValueError):
            seq_left_command = Call(
                "cat",
                ["/comp0010/test/dir2/uniq_testing_case.txt"],
                None,
                None
            )
            right_command = Call("unsupported_command", [], None, None)
            seq = Seq([seq_left_command, right_command])
            seq.eval()

    def test_seq5(self):
        """
            Test case 5:
                unsupported_command ; sort
        """
        with self.assertRaises(ValueError):
            left_command = Call("unsupported_command", [], None, None)
            right_command = Call("sort", [], None, None)
            seq = Seq([left_command, right_command])
            seq.eval()

    def test_seq6(self):
        """
            Test case 6:
                echo hello world ; echo user
        """
        output = input_factory("echo hello world ; echo user", Converter())
        output_lines = [
            line.strip() for line in output if line.strip() != ""
        ]
        self.assertEqual(output_lines, ["hello world", "user"])
