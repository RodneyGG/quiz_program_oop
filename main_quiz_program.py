#initialize the objects 
from users import Users
from quiz_generator import QuizGenerator
from quiz_taker import QuizTaker
from send_email import SendEmail
import os

"""def main():
    main_quiz_program = True
    os.system('cls')
    while main_quiz_program: 
        choice = input("TYPE ONLY THE NUMBER:\n1.Register\n2.Sign In\n3.Exit\n").strip()
        if choice == "1":
            os.system('cls')
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            email = input("Enter email: ").strip()
            users = Users(username, password, email)
            users.register()

        elif choice == "2":
            os.system('cls')
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            logged_user = Users.log_in(username, password)

            if logged_user: 
                #run the quiztaker or quizmaker
                logged_in = True
                while logged_in:    
                    user_choice = input(f"What do you want to do?\nOnly Type the number\
                        \n1.Take Quiz\n2.Make Quiz\n3.Log out\n").strip()
                    if user_choice == "1":
                        #quiz taker
                        quiz_taker = QuizTaker()
                        os.system('cls')
                        
                    elif user_choice == "2":
                        os.system('cls')
                        quiz_generator = QuizGenerator()
                        quiz_generator.select_file()
                        quiz_generator_loop = True
                        
                        while quiz_generator_loop:
                            what_to_do = input("Please only Type the number\n1.View Question\
                                \n2.Add Question\n3.Remove Question\n4.Email the questions\n5.Exit\n")
                            if what_to_do == "1":
                                os.system('cls')
                                view_question = quiz_generator.view_questions()
                                print(view_question)
                                
                            elif what_to_do == "2":
                                os.system('cls')
                                quiz_generator.question_saver()
                                
                            elif what_to_do == "3":
                                os.system('cls')
                                quiz_generator.delete_question()
                                
                            elif what_to_do == "4":
                                send_email = SendEmail(logged_user.username, logged_user.password, logged_user.email\
                                    , quiz_generator.filename, quiz_generator.filepath)
                                send_email.send_quiz()
                                
                            elif what_to_do == "5":
                                os.system('cls')
                                quiz_generator_loop = False
                                
                            else:
                                os.system('cls')
                                print("Invalid Input Try Again")
                                
                    elif user_choice == "3":
                        #logout para maangas
                        logged_in = False
                        os.system('cls')            
        elif choice == "3":
            main_quiz_program = False
        else:
            print("Invalid Input Try Again")

if __name__ == "__main__":
    main()"""
    
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
            self.clear_screen()
            print(f"Welcome, {self.current_user.username}!")
            print("What do you want to do?\n1. Take Quiz\n2. Make Quiz\n3. Log out")
            choice = input().strip()
            
            if choice == "1":
                self.take_quiz()
            elif choice == "2":
                self.make_quiz()
            elif choice == "3":
                self.current_user = None
                break
            else:
                print("Invalid Input")
            
    def take_quiz(self):
        self.clear_screen()
        self.quiz_taker.test_select_file()
        self.quiz_taker.load_questions()
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
            self.clear_screen()
            print("Please only Type the number")
            print("1. View Question")
            print("2. Add Question")
            print("3. Remove Question")
            print("4. Email the questions")
            print("5. Exit")
            choice = input().strip()
            
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