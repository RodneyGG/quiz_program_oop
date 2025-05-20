# Quiz Maker and Taker Program

## Overview
This program is designed using Object-Oriented Programming (OOP) principles to create a robust and modular quiz application. It allows users to create, manage, and take quizzes, and includes features such as user registration, quiz generation, quiz participation, and emailing of quiz results. The program is intended to be user-friendly and efficient for both quiz creators and participants.

## Features
1. **User Authentication**:
   - Register new users with a username, password, and email.
   - Log in with existing credentials.

2. **Quiz Creation**:
   - Create new quiz files for different topics.
   - Add, view, and delete questions in a quiz.
   - Each question includes multiple-choice options and a correct answer.

3. **Quiz Taking**:
   - Select a quiz to take from available topics.
   - Questions and choices are randomized for fairness.
   - Immediate feedback on answers and a final score report.

4. **Email Integration**:
   - Send quiz results to the user's email after completion.
   - Email the entire quiz to a user for review.

5. **File Management**:
   - Questions are stored in text files with JSON formatting.
   - Users are stored in a separate text file with JSON formatting.

## Installation
1. **Prerequisites**:
   - Python 3.x installed on your system.
   - Required Python libraries: `smtplib`, `email`, `json`, `os`, `random`, `time`.

2. **Setup**:
   - Clone or download the repository.
   ```bash
    git clone https://github.com/RodneyGG/quiz_program_oop.git
    cd quiz_program_oop 
   ```
   - Ensure all files (`main_quiz_program.py`, `users.py`, `quiz_generator.py`, `quiz_taker.py`, `send_email.py`, `filename.py`) are in the same directory.
   - Create the following folders in the same directory:
     - `questions/` (for storing quiz files).
     - `users/` (for storing user data).

3. **Running the Program**:
   - Execute the `main_quiz_program.py` file:
     ```bash
     python main_quiz_program.py
     ```

## Usage
1. **Registration**:
   - New users must register by providing a username, password, and email.

2. **Logging In**:
   - Registered users can log in using their credentials.

3. **Quiz Maker**:
   - After logging in, users can create new quizzes or modify existing ones.
   - Options include adding, viewing, or deleting questions, and emailing the quiz.

4. **Quiz Taker**:
   - Users can select a quiz to take.
   - The program will present questions randomly and provide a score at the end.
   - Results can be emailed to the user.

## File Structure
- `main_quiz_program.py`: Main program entry point.
- `users.py`: Handles user registration and authentication.
- `quiz_generator.py`: Manages quiz creation and modification.
- `quiz_taker.py`: Handles quiz taking and scoring.
- `send_email.py`: Manages sending emails with quiz results or content.
- `filename.py`: Utility class for file operations.
- `questions/`: Directory for storing quiz files.
- `users/`: Directory for storing user data.

## Example Quiz File
Quiz files are stored in the `questions/` directory with names like `math_questions.txt`. Each line in the file is a JSON object representing a question:
```json
{"question": "3 + 3", "choices": ["3", "5", "6", "9"], "answer": "choice_3"}