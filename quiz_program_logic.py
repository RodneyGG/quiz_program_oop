import os 
import json
import random
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart




#make a class for the users
class Users:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        
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
                self.list_quiz_files()
                topic_name = input("Enter the filename to open (e.g., math): ").strip()
                filename = topic_name + "_questions.txt"
                filepath = self.folder + filename
                if os.path.exists(filepath):
                    self.filename = filename
                    self.filepath = filepath
                    return filepath  
                else:
                    print(f"The file {filename} doesn't exist. Please try again.\n")
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
                    print("-" * 30)
    
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
        self.view_questions(self.filepath)
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
                

#make a class for asking question
class QuizTaker(Filename):
    def __init__(self, score=0, quiz_log="", total=0):
        super().__init__()
        self.score = score
        self.quiz_log = quiz_log
        self.total = total
        
    def load_questions(self):
        questions = []
        with open(self.filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    questions.append(json.loads(line))
        return questions
    
    def ask_questions(self):
        #It will then start a quiz and set the score to 0.
        score = 0
        quiz_log = ""
        
        #load the questions
        questions = self.load_questions()  
            
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
        total = len(question) 
        self.total = total
        return self.score, self.quiz_log, self.total
    
        
#make a class for sending email
class SendEmail(Users,Filename, QuizTaker):
    def __init__(self):
        super().__init__()
        
    def send_result(self):
        topic = self.filename.replace("_questions.txt", "")
        sender_email = "quizmakeroop@gmail.com"
        app_password = "toae vefn frlq balq"
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = self.email
        msg["Subject"] = f"Quiz Results for {self.username} - {topic.title()}"
        
        body = (
            f"Hi {self.username},\n\n"
            f"Here are your results for the topic: {topic.title()}\n"
            f"Date: {date}\n"
            f"Score: {self.score}/{self.total}\n\n"
            f"--- Quiz Review ---\n\n{self.quiz_log}"
        )

        msg.attach(MIMEText(body, "plain"))
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, email, msg.as_string())
            print("Email sent successfully!")
        except Exception as error:
            print(f"Failed to send email: {error}")
            
    def send_quiz(self):
        topic = self.filename.replace("_questions.txt", "")
        sender_email = "quizmakeroop@gmail.com"
        app_password = "toae vefn frlq balq"
        quiz = self.view_questions()
        
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = self.email
        msg["Subject"] = f"Question for Quiz - {topic.title()}"
        
        body = (
            f"Hi {self.username},\n\n"
            f"Here are the questions for the Quiz: {topic.title()}\n"
            f"{quiz}\n"
            
        )

        msg.attach(MIMEText(body, "plain"))
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, email, msg.as_string())
            print("Email sent successfully!")
        except Exception as error:
            print(f"Failed to send email: {error}")