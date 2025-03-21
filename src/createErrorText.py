import re

##### ERROR #####
class CustomError(Exception):
    def __init__(self, message, pos):
        super().__init__(message)
        self.pos = pos

##### ERROR TEXT #####

class ErrorText:
    def __init__(self, text):
        # self.text = text
        self.lines = re.split('\n', text)
    
    # def createLines(self, text):
    #     lines = re.split('\n', text)
    #     # slines = []
    #     # for line in lines:
    #     #     slines.append(line.strip())
    #     # return slines
    #     return lines


    def makeErrorText(self, pos):
        err = [f"line: {pos.row+1} | ",
              f"{self.lines[pos.row]}"]
        s = list("\n")
        for i in range(len(err[0])):
            s.append(" ")
        for i, l in enumerate(self.lines[pos.row]):
            if i < pos.column:
                s.append(" ")
            else:
                s.append("^")
        return "".join(err) + "".join(s)