class Brain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.correct_answers = 0
        
    def is_there_more_questions(self):
        return self.q_number < len(self.q_list)
            
    def question(self):
        question = self.q_list[self.q_number].text
        answer = self.q_list[self.q_number].answer
        self.q_number += 1
        while True:
            user_answer = input(f"Q{self.q_number}: {question} (True or False) : ").lower()
            if user_answer not in ["true","false"]:
                print("Please type either True or False!\n")
                continue
            break
        
        self.check_answer(user_answer, answer)
        
    def check_answer(self, user_answer, answer):
        if user_answer == answer.lower():
            print("That was Correct!\n")
            self.correct_answers += 1
        else:
            print(f"Nope! The correct answer was {answer}\n")
        
        
            