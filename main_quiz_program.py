#initialize the objects 
from users import Users
from quiz_generator import QuizGenerator
from quiz_taker import QuizTaker
from send_email import SendEmail
import os

#convert it to OOP
class QuizApp:
    def __init__(self):
        self.current_user = None
        self.quiz_generator = QuizGenerator()  
        self.quiz_taker = QuizTaker() 

    def clear_screen(self):
        os.system("cls")
        
    def display_main_menu(self):
        print("TYPE ONLY THE NUMBER:\n1. Register\n2. Sign In\n3. Exit")
        choice = input().strip()
        return choice
    
    def handle_registration(self):
        self.clear_screen()
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        email = input("Enter email: ").strip()
        self.clear_screen() 
        user = Users(username, password, email)
        user.register()
        
        
    def handle_login(self):
        self.clear_screen()
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        self.current_user = Users.log_in(username, password)
        if self.current_user:
            self.user_session()
        
    
    def user_session(self):
        while True:
            print(f"Welcome, {self.current_user.username}!")
            print("What do you want to do?")
            print("1. Take Quiz")
            print("2. Make Quiz")
            print("3. Log out")
            choice = input().strip()
            
            if choice == "1":
                self.take_quiz()
            elif choice == "2":
                self.make_quiz()
            elif choice == "3":
                self.current_user = None
                self.clear_screen()
                break
            else:
                print("Invalid Input")
            
    def take_quiz(self):
        self.clear_screen()
        self.quiz_taker.test_select_file()
        self.quiz_taker.load_questions()
        self.clear_screen()
        result = self.quiz_taker.ask_questions()
        if result is not None:
            score, quiz_log, total = result
            send_email = SendEmail(self.current_user.username, self.current_user.password, self.current_user.email\
                    , self.quiz_taker.filename, self.quiz_taker.filepath, score, quiz_log, total)
            send_email.send_result()#hayup na yan mali lang natawag
        
    def make_quiz(self):
        self.clear_screen()
        self.quiz_generator.select_file()
        
        while True:
            print("Please only Type the number")
            print("1. View Question")
            print("2. Add Question")
            print("3. Remove Question")
            print("4. Email the questions")
            print("5. Exit")
            choice = input().strip()
            self.clear_screen()
            
            if choice == "1":
                self.clear_screen()
                view_question = self.quiz_generator.view_questions()
                print(view_question)
                input("Press Enter to continue...")
            elif choice == "2":
                self.clear_screen()
                self.quiz_generator.question_saver()
            elif choice == "3":
                self.clear_screen()
                self.quiz_generator.delete_question()
                self.clear_screen()
            elif choice == "4":
                send_email = SendEmail(
                    self.current_user.username,
                    self.current_user.password,
                    self.current_user.email,
                    self.quiz_generator.filename,
                    self.quiz_generator.filepath
                )
                send_email.send_quiz()
            elif choice == "5":
                break
    def run(self):
        while True:
            choice = self.display_main_menu()
            
            if choice == "1":
                self.clear_screen()
                self.handle_registration()
            elif choice == "2":
                self.handle_login()
            elif choice == "3":
                break
            else:
                print("Invalid Input Try Again")
                
if __name__ == "__main__":
    os.system("cls")
    app = QuizApp()
    app.run()