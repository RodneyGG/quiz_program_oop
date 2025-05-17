import os 
import json

#make a class for the users
class Users:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        
#Make a class for picking of the file
class Filename:
    def __init__(self):
        self.folder = 'questions/'
        self.filename = None
        self.filepath = None
    
    #select the file
    def select_file(self):
        while True:
            choice = input("Do you want to:\n1. Open an existing file\n2. Create a new file\nEnter 1 or 2: ").strip()
            if choice == "1":
                self.list_quiz_files()
                topic_name = input("Enter the filename to open (e.g., math): ").strip()
                filename = topic_name + "_questions.txt"
                filepath = self.folder + filename
                if os.path.exists(filepath):
                    self.view_questions(filepath)
                    self.filename = filename
                    self.filepath
                    return filepath  
                else:
                    print(f"The file {self.filename} doesn't exist. Please try again.\n")
            elif choice == "2":
                #Ask the user what subject or topic the question will he or she be making
                topic = input("Enter the Subject or Topic of the question: ").strip().lower()
                filename = f"{topic}_questions.txt"
                #check if filename is already exists
                while True:
                    try:
                        filepath = self.folder + filename
                        open(filepath, "x").close()
                        break
                    except FileExistsError:
                        print(f"The file '{self.filename}' already exists.\n")
                        new_filename = input("Please enter a new filename: ").strip()
                        filename = new_filename + "_questions.txt"
                        filepath = self.folder + filename
                self.filename = filename
                self.filepath = filepath
                return filepath  
            else:
                print("Invalid choice, please enter 1 or 2 only.\n")
        
    #view the questions
    def view_questions(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            print(f"These are the questions inside {self.filename}")

            for line_number, line in enumerate(file, 1): 
                line = line.strip()
                if line: 
                    data = json.loads(line) 
                    
                    print(f"Question{line_number}:", data["question"])
                    
                    for index, choice in enumerate(data["choices"], 1):
                        print(f"  choice_{index}: {choice}")
                    print("Answer:", data["answer"])
                    print("-" * 40)
    
    def is_question_duplicate(self, filepath, question):
        #Check if the file exists and is not empty
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                #loop the the question to find duplicate
                for line in file:
                    line = line.strip()
                    if line:
                        saved_question = json.loads(line)
                        if saved_question["question"].lower() == question.lower():
                            return True # Duplicate found
                return False#return false when question not found
            
        except (FileNotFoundError, json.JSONDecodeError):
            return False

    def list_quiz_files(self):
        print("Available Quiz Files:")
        for file in os.listdir(self.folder):
            if file.endswith("_questions.txt"):
                topic = file.replace("_questions.txt", "")
                print(f"{topic}")
        print("-" * 30)
        
#make a class for Questions generation
class QuizGenerator(Filename):
    def __init__(self):
        super().__init__()

    def question_saver(self):
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
            if not self.is_question_duplicate(self.filepath, question):
                with open(self.filepath, "a", encoding="utf-8") as file:
                    file.write(json.dumps(questions_format) + "\n")
            else:
                print(f"This Question is already in the {self.filename}!\n") 
                
quiz_generator = QuizGenerator()
quiz_generator.select_file()
quiz_generator.question_saver()
            
#make a class for sending email
#make a class for asking question
