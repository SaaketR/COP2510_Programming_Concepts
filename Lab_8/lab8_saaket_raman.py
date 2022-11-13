# The code for this project represents my own, independent work. I have neither given nor received help on this assignment from other students.
# Saaket Raman

class Question:
    def __init__(self, question, points):
        self.__question = question
        self.__points = points
        if self.__points < 0: raise ValueError("Error. Number of points must be non-negative.")
    
    def get_question(self):
        return self.__question
    
    def set_question(self, newQuestion):
        self.__question = newQuestion
    
    def get_points(self):
        return self.__points
    
    def set_points(self, newPoints):
        self.__points = newPoints

    def print_question(self):
        print(f"{self.get_question()}  ({self.get_points()} points)")
    
    def score(answer = ""):
        pass
    
class FillInTheBlank(Question):
    def __init__(self, question, points, answer):
        Question.__init__(self, question, points)
        self.__answer = answer
    
    def score(self, answer = ""):
        if answer == self.__answer: return self.__points
        else: return 0
    
    def get_question(self):
        return self.__questiom
    
    def set_question(self, newQuestion):
        self.__question = newQuestion
    
    def get_points(self):
        return self.__points
    
    def set_points(self, newPoints):
        self.__points = newPoints

    def print_question(self):
        print(f"{self.get_question()}  ({self.get_points()} points)")

class MultipleChoice(Question):
    def __init__(self, question, points, choices, answer):
        Question.__init__(self, question, points)
        self.__choices = choices
        self.__answer = answer
    
