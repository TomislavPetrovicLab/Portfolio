# Python quiz game

# 1. Declare all the necessary collections and variables
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the Solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

# To display each question:
for question in questions:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is: {answers[question_num]}")
    question_num += 1

# now display all the results
print("- - - - - - - - - - - - - - - -")
print("            RESULT             ")
print("- - - - - - - - - - - - - - - -")

print("Correct Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = score / len(questions) * 100
print(f"Your score is: {score}%")