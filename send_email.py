import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from users import Users
from quiz_taker import QuizTaker
from quiz_generator import QuizGenerator
import time
import os

#make a class for sending email
class SendEmail(Users, QuizTaker, QuizGenerator):
    def __init__(self, username, password, email, filename="", filepath="", score=0, quiz_log="", total=0):
        Users.__init__(self, username, password, email)
        QuizTaker.__init__(self, score, quiz_log, total)
        self.filename = filename
        self.filepath = filepath
        #self.score = score
        #self.quiz_log = quiz_log
        #self.total = total
        
        
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
                server.sendmail(sender_email, self.email, msg.as_string())
            os.system('cls')
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
            f"{quiz}\n"
            
        )

        msg.attach(MIMEText(body, "plain"))
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, self.email, msg.as_string())
            os.system('cls')
            print("Email sent successfully!")
        except Exception as error:
            print(f"Failed to send email: {error}")