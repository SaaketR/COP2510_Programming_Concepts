from lab8_saaket_raman import FillInTheBlank, MultipleChoice

# Class that represents an exam
class Exam:
  # Reads in the exam from the given file
  # File describes the number of questions and, for each question, the type,
  # text, number of points, correct answer, and choices (for multiple choice
  # questions)
  def __init__(self, filename):
    with open(filename) as file:
      num_questions = int(file.readline())
      self.questions = []
      self.maxscore = 0
      qchoices = []
      for q in range(num_questions):
        qtype = file.readline().rstrip()
        qtext = file.readline().rstrip()
        qscore = int(file.readline())
        ans = file.readline().rstrip()
        if qtype == 'multiple choice':
          num_choices = int(file.readline())
          qchoices.clear()
          for c in range(num_choices):
            qchoices.append(file.readline().rstrip())
          self.questions.append(MultipleChoice(qtext, qscore, qchoices, ans))
        elif qtype == 'fill-in-the-blank':
          self.questions.append(FillInTheBlank(qtext, qscore, ans))
        else:
          raise Exception('Exam file not in correct format')
        self.maxscore += self.questions[-1].get_points()
  # Returns the sum of the points for all questions on the exam
  def get_max_score(self):
    return self.maxscore

  # Prints out the exam questions, prompts the user for answers, and returns
  # the user's score
  def take(self):
    print('Answer the following questions.')
    score = 0
    for i in range(len(self.questions)):
      print(f'\n{i+1}.  {self.questions[i]}')
      score += self.questions[i].score(input())
    return score

if __name__ == '__main__':
  examfile = input('Enter the file containing the exam: ')
  exam = Exam(examfile)
  points = exam.take()
  print(f'You scored {points} / {exam.get_max_score()} on the exam')
