from subjective import *
class ShortQuestion(Subjective):
    def __init__(self,file):
        super().__init__(file,2)

    def __str__(self):
        return f'{super().__str__()}\n{"_____________________________"}\n{"_____________________________"}'
