from filename import Filename
import random
import json
import os
                    
#make a class for asking question
class QuizTaker(Filename):
    def __init__(self, score=0, quiz_log="", total=0):
        super().__init__()
        self.score = score
        self.quiz_log = quiz_log
        self.total = total
        self.current_filepath = ""
    
    #store the selected filepath
    def select_file(self):
        self.current_filepath = super().select_file()  
        return self.current_filepath
        
    def load_questions(self):
        questions = []
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        questions.append(json.loads(line))
        except FileNotFoundError:
            return questions
        return questions
    
    def ask_questions(self):
        #It will then start a quiz and set the score to 0.
        score = 0
        quiz_log = ""
        
        while True:
            #load the questions
            questions = self.load_questions()

            if not questions:
                os.system('cls')
                print("No questions available. Cannot start the test.")
                return None
            
            #the program will randomize the order of the question
            random.shuffle(questions)
            
            for item, question in enumerate(questions, 1):
                print(f"\nQ{item}: {question['question']}")
                
                #the program will randomize the choices
                original_choices = question["choices"]
                shuffle_choices = original_choices[:]      
                random.shuffle(shuffle_choices)

                labeled_choices = {
                    label: choice for label, choice in zip(["A", "B", "C", "D"], shuffle_choices)
                }

                # Display choices
                for label, choice in labeled_choices.items():
                    print(f"    {label}. {choice}")
                    
                answer = input("Your answer (A/B/C/D): ").strip().upper()
                while answer not in labeled_choices:
                    answer = input("Invalid. Enter A, B, C, or D: ").strip().upper()
                    
                correct_index = int(question["answer"].split("_")[1]) - 1
                correct_choice = original_choices[correct_index]

                user_choice = labeled_choices[answer]
                
                if user_choice == correct_choice:
                    print(" Correct!")
                    #Plus 1 every correct answer
                    score += 1
                else:
                    print(f" Incorrect. Correct answer: {correct_choice}")
                    
                quiz_log += f"Q{item}: {question['question']}\n"
                for label, choice in labeled_choices.items():
                    is_correct = "" 
                    if choice == correct_choice:
                        is_correct += "✅"
                    quiz_log += f"    {label}. {choice}{is_correct}\n"
                
                quiz_log += f"Your answer: {answer}. {user_choice}\n\n"
                
            
            self.score = score
            self.quiz_log = quiz_log
            total = len(questions) 
            self.total = total
            return self.score, self.quiz_log, self.total
