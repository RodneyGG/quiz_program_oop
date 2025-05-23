import json
import os

#Make a class for picking of the file
class Filename:
    def __init__(self, filename="", filepath=""):
        self.folder = 'questions/'
        self.filename = filename
        self.filepath = filepath
    
    #select the file
    def select_file(self):
        while True:
            choice = input("Do you want to:\n1. Open an existing file\n2. Create a new file\nEnter 1 or 2: ").strip()
            if choice == "1":
                os.system('cls')
                result = self.test_select_file()
                os.system('cls')
                topic = self.filename.replace("_questions.txt", "")
                print(f"You are currently in {topic}")
                if result:
                    return result
            elif choice == "2":
                os.system('cls')
                #Ask the user what subject or topic the question will he or she be making
                topic = input("Enter the Subject or Topic of the question: ").strip().lower()
                filename = f"{topic}_questions.txt"
                os.system('cls')
                #check if filename is already exists
                while True:
                    try:
                        filepath = self.folder + filename
                        open(filepath, "x").close()
                        break
                    except FileExistsError:
                        print(f"The file {filename} already exists.\n")
                        new_filename = input("Please enter a new filename: ").strip()
                        filename = new_filename + "_questions.txt"
                        filepath = self.folder + filename
                        os.system('cls')
                self.filename = filename
                self.filepath = filepath
                return self.filepath, self.filename 
            else:
                print("Invalid choice, please enter 1 or 2 only.\n")
            os.system('cls')
                
    def test_select_file(self):
        self.list_quiz_files()
        while True:
            topic_name = input("Enter the filename to open (e.g., math): ").strip()
            filename = topic_name + "_questions.txt"
            filepath = self.folder + filename
            if os.path.exists(filepath):
                self.filename = filename
                self.filepath = filepath
                return self.filepath, self.filename  
            else:
                os.system('cls')
                print(f"The file {topic_name} doesn't exist. Please try again.\n")
                self.list_quiz_files()
    #view the questions
    def view_questions(self):
        topic = self.filename.replace("_questions.txt", "")
        quiz = [f"These are the questions inside {topic}\n"]
    
        with open(self.filepath, "r", encoding="utf-8") as file:
            
            for line_number, line in enumerate(file, 1): 
                line = line.strip()
                if line: 
                    data = json.loads(line)
                    
                    question_text = f"Question {line_number}: {data['question']}"
                    quiz.append(question_text)

                    for index, choice in enumerate(data["choices"], 1):
                        choice_text = f"  choice_{index}: {choice}"
                        quiz.append(choice_text)

                    answer_text = f"Answer: {data['answer']}"
                    quiz.append(answer_text)

                    separator = "-" * 30
                    quiz.append(separator)
    
        return "\n".join(quiz)
    
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

    #list all the files that ends with _questions.txt
    def list_quiz_files(self):
        print("Available Quiz Files:")
        for file in os.listdir(self.folder):
            if file.endswith("_questions.txt"):
                topic = file.replace("_questions.txt", "")
                print(f"{topic}")
        print("-" * 30)