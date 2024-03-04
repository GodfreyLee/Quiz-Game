class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer):
        print(self.question_list[self.question_number].answer)
        if user_answer == self.question_list[self.question_number].answer:
            self.score += 1
            print(f"Your score is {self.score}")
            self.question_number += 1
        else:
            print("Bug")
    def next_question(self):
        print(self.question_list[self.question_number].text)
        return input("Is this correct? Type True or False")

