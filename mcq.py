from objective import *
class Mcq(Objective):
    def __init__(self,file):
        super().__init__(file)
        self.choice1 = file.readline()
        self.choice2 = file.readline()
        self.choice3 = file.readline()
        self.choice4 = file.readline()

    def __str__(self):
        return f'{super().__str__()}\na:{self.choice1}\nb:{self.choice2}\nc:{self.choice3}\nd:{self.choice4}\n{"Enter Your Choice: "}'
