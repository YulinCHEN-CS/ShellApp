from .Application import Application
import re


class Cut(Application):
    """
        cut application outputs the correspond bytes of each line in a file
        example:
            cut -b 1,5- file.txt
            cut -b 1-3,5-7 < file.txt
            cut -b 1-3,5-7 file.txt > output.txt
            cut -b 1-3,5-7 file1.txt file2.txt
    """

    def is_valid_format(self, arg):
        pattern = re.compile(r'\d-\d|-\d|\d-|\d')
        return bool(pattern.match(arg))

    def parse_args(self):
        try:
            byte_nums_str = []
            if self.args[0] == '-b':
                byte_nums_str = self.args[1].split(',')
            for byte_num_str in byte_nums_str:
                if not self.is_valid_format(byte_num_str):
                    raise ValueError()
            return byte_nums_str, self.args[2]
        except Exception:
            raise ValueError("Usage: cut -b options "
                             "[FILE]...\n(no space in options)")

    def get_bytes(self, line, byte_nums):
        result = ""
        byte_set = set()
        for byte_num in byte_nums:
            if '-' in byte_num:
                start, end = byte_num.split('-')
                start = int(start) if start else 1
                end = int(end) if end else len(line)
                byte_set.update(range(start - 1, end))
            else:
                byte_set.add(int(byte_num) - 1)

        byte_list = sorted(list(byte_set))
        # print(byte_list)
        for byte in byte_list:
            result += line[byte]
        return result if result.endswith('\n') else result + '\n'

    def exec(self):
        byte_nums, file_name = self.parse_args()
        try:
            lines = self._read_lines(file_name)
            for line in lines:
                if line.strip() == '':
                    continue
                self.output.append(self.get_bytes(line, byte_nums))
        except Exception:
            raise FileNotFoundError(f"File not found: {file_name}")
