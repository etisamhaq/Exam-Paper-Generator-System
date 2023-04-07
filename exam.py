from mcq import *
from crossmatch import *
from fill_in_the_blank import *
from shortquestion import *
from longquestion import *

class Exam(Mcq,CrossMatch,Fill_In_The_Blanks,ShortQuestion,LongQuestion):

    def __init__(self,title):
        self.title = title
        self.count_mcq = int(input("Enter count of MCQ questions (1-6):"))
        self.count_blanks = int(input("Enter count of fill in the blanks count questions (1-6):"))
        self.count_crossmatch = int(input("Enter count of statements in crossmatch question(1-6):"))
        self.count_shortquestions = int(input("Enter count of short questions:"))
        self.count_longquestions = int(input("Enter count of long questions:"))
        self.list_mcqs = []
        self.cross_match = []
        self.fill_blanks = []
        self.short = []
        self.long = []

        with open("mcq.txt","r") as f1:
            for i in range(self.count_mcq):
                self.mcqs = Mcq(f1)
                self.list_mcqs.append(self.mcqs)

        with open("crossmatch.txt","r") as f2:
            #for i in range(self._count_crossmatch):
            self.crossmatch = CrossMatch(f2,self.count_crossmatch)
            #self._cross_match.append(self._crossmatch)

        with open("fill_in_the_blanks.txt","r") as f3:
            for i in range(self.count_blanks):
                self.blanks = Fill_In_The_Blanks(f3)
                self.fill_blanks.append(self.blanks)

        with open("short.txt","r") as f4:
            for i in range(self.count_shortquestions):
                self.blanks = ShortQuestion(f4)
                self.short.append(self.blanks)

        with open("long.txt","r") as f5:
            for i in range(self.count_longquestions):
                self.blanks = LongQuestion(f5)
                self.long.append(self.blanks)

    def __str__(self):
        string = self.title
        string += "\n*** Section M C Q ***"

        for i in self.list_mcqs:
            
            string += "\n" + str(i)

        string += "\n" + str(self.crossmatch)
        string += "\n*** Fill in the blanks ***\n"
        for i in self.fill_blanks:
            string += "\n" + str(i)

        string += "\n*** Section Short Question(s) ***\n"
        for i in self.short:
            string += "\n" + str(i)

        string += "\n*** Section Long Question(s) ***\n"
        for i in self.long:
            string += "\n" + str(i)

        return string


a = Exam("Exam Paper")
print(a)




