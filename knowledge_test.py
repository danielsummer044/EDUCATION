class Question():
	def __init__(self, question, answer1, answer2, answer3, answer4, correct):
		self.question = question
		self.answer1 = answer1
		self.answer2 = answer2
		self.answer3 = answer3
		self.answer4 = answer4
		self.correct = correct

	def __str__(self):
		return self.question + '\n' + self.answer1 + '\n' + self.answer2 + '\n' + self.answer3 + '\n' + self.answer4


# ------------------------

"""
question = Question('Де знаходиться Україна ?', '1 - Європа', '2 - Америка', '3 - Азія', '4 - Африка', '1')
print(question)

answer = input('Ваша відповідь: ')

if answer == question.correct:
	print('yes')
else:
	print('no')
"""

# TODO:
def read_from_file(filename):
	list_of_Question = []
	with open(filename) as f:
		# read 6 lines from file
		question = Question(line1, line2, line3, line4, line5, line6)
		list_of_Question.append(question)
    return list_of_Question


for question in read_from_file('questions.txt'):
	print(question)

	answer = input('Ваша відповідь: ')

	if answer == question.correct:
		print('yes')
	else:
		print('no')