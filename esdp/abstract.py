from abc import ABC, abstractmethod
class Rcpit(ABC):
    @abstractmethod
    def student_details(self):
        pass
    @abstractmethod
    def student_assignment(self):
        pass

    @abstractmethod
    def student_marks(self):
        pass

class Data(Rcpit):
    def student_details(self):
        print("Students Details")

    def student_assignment(self):
        print("student_assignment")

    def student_marks(self):
        print("student_marks")  

    


d=Data()
d.student_details()
d.student_assignment()
d.student_marks()
