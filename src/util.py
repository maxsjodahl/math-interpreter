import re

##### ERROR #####


class CustomError(Exception):
    def __init__(self, message, pos):
        super().__init__(message)
        self.pos = pos


##### ERROR TEXT #####


class ErrorText:
    def __init__(self, text):
        self.lines = re.split("\n", text)

    def makeErrorText(self, pos):
        err = [f"line: {pos.row + 1} | ", f"{self.lines[pos.row]}"]
        s = list("\n")
        for i in range(len(err[0])):
            s.append(" ")
        for i in range(len(self.lines[pos.row])):
            if i < pos.column:
                s.append(" ")
            else:
                s.append("^")
        if pos.column >= len(self.lines[pos.row]):
            s.append("^")

        return "".join(err) + "".join(s)
