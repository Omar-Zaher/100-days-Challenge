from question_model import Questions
from data import question_data
from quiz_brain import Brain

question_bank = []

for i in question_data:
    question = Questions(i["text"],i["answer"])
    question_bank.append(question)
    
brain = Brain(question_bank)

while brain.is_there_more_questions():
    
    brain.question()
    
print (f"Your Final Score: {brain.correct_answers}/12")
    
