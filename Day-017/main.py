"""

Creating a question bank for the quiz game. The question bank is a list of dictionaries, where each dictionary represents a question and its corresponding answer. 
Each dictionary contains two keys: "question" and "answer". The "question" key holds the text of the question, while the "answer" key holds the correct answer to that question.

"""
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# The next_question method in QuizBrain should return the user's answer

questions = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)#Here a new instance of the Question class is created using the question text and answer from the question_data. This instance is then appended to the questions list, which will hold all the questions for the quiz game.
    questions.append(new_question)  

#print(questions[0].text)  # This will print the text of the first question in the questions list.

quiz = QuizBrain(questions)
while quiz.still_has_questions():
    user_answer = quiz.next_question()
    is_correct = quiz.check_answer(user_answer, quiz.question_list[quiz.question_number - 1].answer)
    if is_correct:
        print("You got it right!")
    else:
        print("That's wrong.")
print(f"Your final score is: {quiz.score}/{len(questions)}")



