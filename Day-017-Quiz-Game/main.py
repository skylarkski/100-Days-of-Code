from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

# since question data is a list of dictionary objects, we can tap into the i index and key of dictionary
# to get the right new_q
for i in range(len(question_data)):
    new_q = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.quiz_score}/{len(question_bank)}")