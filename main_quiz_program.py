#initialize the objects 
from users import Users
from quiz_generator import QuizGenerator
from quiz_taker import QuizTaker
from send_email import SendEmail
import os

def main():
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
                        quiz_taker.test_select_file()
                        quiz_taker.load_questions()
                        score, quiz_log, total = quiz_taker.ask_questions()
                        send_email = SendEmail(logged_user.username, logged_user.password, logged_user.email\
                            ,quiz_taker.filename, quiz_taker.filepath, score, quiz_log, total)
                        send_email.send_result()#hayup na yan mali lang natawag
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
    main()