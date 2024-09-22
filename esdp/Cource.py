from abc import ABC, abstractmethod
class Cource:
    def __init__(self,title,duration,price):
        self.title=title
        self.duration=duration
        self.price=price
    
    @abstractmethod
    def enroll(self):
        pass
    def get_details(self):
        pass

class ProgrammingCource(Cource):
    programming_language=" "
    instructor=" "
    @abstractmethod
    def get_details(self):
        pass
    