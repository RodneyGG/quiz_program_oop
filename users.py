import os 
import json

#make a class for the users
class Users:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password    
        self.email = email
        
        
    #register the info to the text file
    def register(self, filename='users/users.txt'):
        user_info = {
            "username": self.username,
            "password": self.password,
            "email": self.email 
        }
        
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():#skip empty lines
                    user = json.loads(line)
                    if user["username"] == self.username:
                        print(f"{self.username} already exist. Please Try Again <3")
                        return
                    
        #store the information here
        with open(filename, "a") as file:
            file.write(json.dumps(user_info) + "\n")#Pinapahirapan ko lang sarili ko eh
            os.system('cls')
            print(f"You have successfully registered\nUsername:{self.username}\
                \nPlease don't forget your password")   
        
        

    #validates the user        
    @staticmethod
    def log_in(username, password, filename='users/users.txt'):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():#skip empty lines
                    user = json.loads(line)
                    if user["username"] == username:
                        if user["password"] == password:
                            os.system('cls')
                            print(f"Login successful! Welcome, {username}.")
                            return Users(username, password, user["email"])
                        else:
                            os.system("cls")
                            print("Incorrect password.")
                            return None
        os.system("cls")
        print("Username not found.")
        return None          
    