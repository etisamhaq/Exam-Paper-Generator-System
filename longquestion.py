from subjective import *
class LongQuestion(Subjective):
    def __init__(self,file):
        super().__init__(file,5)

    def __str__(self):
        return f'{super().__str__()}\n{"_____________________________"}\n{"_____________________________"}\n{"_____________________________"}\n{"_____________________________"}\n{"_____________________________"}'
