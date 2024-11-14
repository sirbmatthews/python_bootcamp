class QuizBrain():
    
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0
        
    def next_question(self):
        '''
            Prints the question and prompts the user for an answer.
        '''
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {current_question.q_text} (True/False)?: ').capitalize()
        self.check_answer(answer, current_question.q_answer)
    
    def check_answer(self, user_answer, correct_answer):
        '''
            Checks the answer, prints whether it is right or wrong, the correct answer and the current score.
        '''
        if user_answer == correct_answer:
            self.score += 1
            print('You got it right!')
        else: 
            print('You got it wrong!')
            
        print(f'The correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.score}/{self.question_number}.\n')
    
    def still_has_questions(self):
        '''
            Return true if the quiz still contains more questions and false if there are no further questions your honour.
        '''
        return self.question_number < len(self.questions_list)
    
    def final_score(self):
        '''
            Prints the final score of the Quiz
        '''
        print('You\'ve completed the quiz.')
        print(f'Your final score was {self.score}/{self.question_number}')