from abc import *

class Question(ABC):
    q_no = 1

    def __init__(self,file,marks=1):
        self.q_no = Question.q_no
        Question.q_no += 1
        self.discription = file.readline()
        self.marks  = marks




    @abstractmethod
    def __str__(self):
        return f'Question No.:{self.q_no}\t{self.discription}\t(Marks:{self.marks})\n'
