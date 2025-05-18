from quiz_program_logic import Users,  Filename, QuizGenerator, QuizTaker, SendEmail
import os

#initialize the objects    
filename = Filename()
quiz_taker = QuizTaker()

def main():
    main_quiz_program = True
    
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
                    os.system('cls')
                    print(f"You are currently logged in as {username}\n")
                    user_choice = input(f"What do you want to do?\nOnly Type the number\
                        \n1.Take Quiz\n2.Make Quiz\n3.Log out\n").strip()
                    if user_choice == "1":
                        #quiz taker
                        os.system('cls')
                        quiz_taker.select_file()
                        quiz_taker.load_questions()
                        quiz_taker.ask_questions()
                        send_email = SendEmail()
                        send_email.send_quiz()
                    elif user_choice == "2":
                        os.system('cls')
                        quiz_generator = QuizGenerator()
                        quiz_generator.select_file()
                        quiz_generator_loop = True
                        while quiz_generator_loop:
                            what_to_do = input("Please only Type the number\n1.View Question\
                                \n2.Add Question\n3.Remove Question\n4.Exit")
                            if what_to_do == "1":
                                os.system('cls')
                                quiz_generator.view_questions()
                            elif what_to_do == "2":
                                os.system('cls')
                                quiz_generator.question_saver()
                            elif what_to_do == "3":
                                os.system('cls')
                                quiz_generator.delete_question()
                            elif what_to_do == "4":
                                os.system('cls')
                                quiz_generator_loop = False
                            else:
                                os.system('cls')
                                print("Invalid Input Try Again")
                                
                    elif user_choice == "3":
                        #logout para maangas
                        logged_in = False
                    
                    
        elif choice == "3":
            main_quiz_program = False
        
        else:
            print("Invalid Input Try Again")

main()