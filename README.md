# gcse-python-task3
OCR Computer Science GCSE Programming Task CA. Developed in Python.

Task:

Fergus is creating a quiz that tests students’ knowledge topics*, such as:
- History
- Music
- Computer Science.

Students must register before they can take the quiz, choosing a unique username and a password for the account. The username and password are saved into an external file. They must then enter the following details about themselves:

- Name
- Age
- Year Group

A student can choose which topic they want to answer a series of questions on. The student can then choose a difficulty rating on ‘Easy’, ‘Medium’ or ‘Hard’. Each question will have a set of possible answers that the user can choose from. The number of answers the students chooses from changes based on the difficulty of the quiz. The user must select an answer to a question before the next question is displayed.

At the end of the quiz, the game will output the number of questions they got correct and a grade depending on the percentage of questions the user has got correct. You must create a suitable grade system, and the percentages needed to achieve each grade. There must be at least four possible grades.

The program stores information about every quiz each student has taken, including the topic, score and difficulty rating.

Analyse the requirements for this system and design, develop, tests and evaluate a program that:

1. creates a unique username for each user. The username is made up from the first 3 letters of their name and their age. E.g. Gemma Smith, age 17 would have a username of ‘Gem17’. It then asks the user to enter a password for their account.
2. stores the username and password of the user, the details about each user, and the topic, score and difficulty rating of all quizzes each student has taken. These do not have to be stored in the same file.
3. allows a user to select a topic and difficulty rating (Easy, Medium or Hard) and asks five questions on that topic:
4. a. ‘Easy’ mode has a choice of two answers for each question
5. b. ‘Medium’ mode has a choice of three answers for each question
6. c. ‘Hard’ mode has a choice of four answers for each question.
7. loads the questions and answers from a file stored externally to the game.
8. displays the user’s score, percentage and grade achieved for that quiz.
9. gives Fergus the option to generate and output the following reports:
10. a. a report that allows Fergus to choose a username, and outputs all of the quizzes that they have taken, and the grade for each of those quizzes.
11. b. a report that outputs for a selected topic and difficulty: the average score achieved, the highest score achieved, and the user details of the person that achieved the highest score.

NOTE FOR CANDIDATES:
*The system only needs to be tested using two topics. 
