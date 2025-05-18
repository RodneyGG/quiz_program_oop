from quiz_program_logic import Users,  Filename, QuizGenerator, QuizTaker, SendEmail
import os

#initialize the objects    
filename = Filename()
quiz_generator = QuizGenerator()
quiz_taker = QuizTaker()
#send_email = SendEmail()



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
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            logged_user = Users.log_in(username, password)

            if logged_user: 
                #run the quiztaker or quizmaker
                pass
            
        elif choice == "3":
            main_quiz_program = False
        
        else:
            print("Invalid Input Try Again")

main()