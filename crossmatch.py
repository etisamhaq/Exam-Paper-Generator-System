from objective import *

class CrossMatch(Objective):

    def __init__(self,file,count):
        super().__init__(file)
        self._string = ""
        for i in range(count*2):
            self._string += file.readline().strip()
            if (i+1) % 2 == 0:
                self._string += "\n"
            else:
                self._string += "**"


    def __str__(self):
        return f"{super().__str__()}\n{self._string}"
