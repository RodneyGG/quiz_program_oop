from filename import Filename

#make a class for Questions generation
class QuizGenerator(Filename):
    def __init__(self):
        super().__init__()

    #append the question the text file
    def question_saver(self):
        view_question = self.view_questions()
        print(view_question)
        #Ask the user to input a question
        question = input("\nEnter your question: ").strip()
        
        #input choices for A, B, C, D
        choice_1 = input("Enter choice 1: ").strip()
        choice_2 = input("Enter choice 2: ").strip()
        choice_3 = input("Enter choice 3: ").strip()
        choice_4 = input("Enter choice 4: ").strip()
        
        #select what is the correct answer
        correct_answer = ""
        while correct_answer not in ['1', '2', '3', '4']:
            correct_answer = input("Which is the correct answer? (1/2/3/4): \n").lower().strip()
            questions_format = {
                    "question": question,
                    "choices": [choice_1, 
                            choice_2, 
                            choice_3, 
                            choice_4],
                    "answer": f"choice_{correct_answer}"
                                    }
        if self.filepath:
            #the question will append if there is already a question similar
            if not self.is_question_duplicate(self.filepath, question):
                with open(self.filepath, "a", encoding="utf-8") as file:
                    file.write(json.dumps(questions_format) + "\n")
            else:
                print(f"This Question is already in the {self.filename}!\n") 
                
    def delete_question(self):
        view_question = self.view_questions()
        print(view_question)
        
        question_to_delete = input("Enter the exact question(Just The Questions :) ) text to delete:\n").strip()
        
        with open(self.filepath, "r", encoding="utf-8") as file:
            questions = []
            for line in file:
                line = line.strip()
                if line:
                    questions.append(json.loads(line))
            
            found = False
            updated_questions = []
            
            for question in questions:
                if question["question"] == question_to_delete:
                    found = True
                    continue
                updated_questions.append(question)
            
            if not found:
                print(f"The Question was not found in the {self.filename}")
            #goodnight
            with open(self.filepath, "w", encoding='utf-8') as file:
                for questions in updated_questions:
                    file.write(json.dumps(questions) + "\n")
