class Teacher():

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list 
        self.score = 0

    def next_question(self):
        text = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer
        self.question_number += 1
        question = input(f"Q{self.question_number}. {text} (t/f)\n").lower()
        while question != "true" and question != "false" and question != "t" and question != "f":
            question = input(f"Q{self.question_number}. {text} (t/f)\n").lower()
        if question == "t":
            question = "true" 
        elif question == "f":
            question = "false"
        self.check_question(question, answer)

    def still_question(self):
        if self.question_number >= len(self.question_list):
            return False
        return True
    
    def check_question(self, check, answer):
        if check.lower() == answer.lower():
            print("You got it correct!")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer is {answer}...\n")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
