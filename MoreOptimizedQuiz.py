questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("="*50)
    print(question)
    for option in options[questions_num]:#PARA MA-CLASSIFY AS INDEX AND MAGSTART SA 0, NILAGAY NATIN SA BRACKET UNG QUESTIONS_NUM
        print(option)
        
    guess = input("Enter Answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print ("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is: {answers[questions_num]}")

    questions_num += 1 #INCREMENT BY 1 YUNG "+="

print("="*50) #"=" MULTIPLIED. PARA KUNG ILAN YUNG MAPRINT
print("\t\tRESULTS")
print("="*50)

print("ANSWERS: ", end="")
for answer in answers: #FOR EVERY ANSWER[WHICH IS UNG LIST(START FROM 0)] IN ANSWERS 
    print(answer, end=" ")
print()

print("GUESSES: ", end="")
for guess in guesses: #FOR EVERY GUESS IN GUESSES[WHICH IS UNG LIST(START FROM 0)] GUESSES
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100) #LEN IS THE LENGTH OF THE QUESTIONS. WHICH IS 5
print(f"Your total score is: {score}% ")
