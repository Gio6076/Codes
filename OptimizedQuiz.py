def numtwo(): return ("\nA.) Atlantic Ocean\nB.) Indian Ocean\nC.) Arctic Ocean\nD.) Pacific Ocean")
def numthree(): return ("\nA.) Venus\nB.) Mars\nC.) Jupiter\nD.) Saturn")
def numfour(): return ("\nA.) Charles Dickens\nB.) William Shakespeare\nC.) J.K Rowling\nD.) Mark Twain")
def numfive(): return ("\nA.) 5\nB.) 6\nC.) 7\nD.) 8")
score = 0
while True:
    name = input("What is your name: ").strip()
    if name.isalpha(): print(f"Hello! {name}, I Welcome you to My Second Program")
    else: 
        print("Please Enter A Valid Name.")
        continue
    age = int(input("Please Enter Age: "))
    if age >= 18: print(f"{age} huh... Please Proceed.")
    else:
        print(f"{age} is too young... Access Denied.")
        continue
    ent = input(f"\nWELCOME TO MY MY SHORT QUIZ! ARE YOU READY {name}? [Y/N]").strip().upper()
    if ent == "Y":
        print("\nA.) Madrid\nB.) Rome\nC.) Paris\nD.) Berlin")
        one = input("What is the Capital of France? ").strip().upper()
        if one == "C": 
            print("Correct.\n", numtwo())
            score += 1
        else: print("Wrong.\n", numtwo())
        two = input("What is the largest ocean on Earth? ").strip().upper()
        if two == "D":
            print("Correct.\n", numthree())
            score += 1
        else: print("Wrong.\n", numthree())
        three = input("Which planet is known as the Red Planet? ").strip().upper()
        if three == "B":
            print("Correct.\n", numfour())
            score += 1
        else: print("Wrong.\n", numfour())
        four = input("Who wrote the play 'Romeo and Juliet'? ").strip().upper()
        if four == "B":
            print("Correct.\n", numfive())
            score += 1
        else: print("Wrong.\n", numfive())
        five = input("How many continents are there? ").strip().upper()
        if five == "C":
            score += 1
            print("Correct.\nYour Total Score is", score, "Thank you for answering my Quiz. GoodBye.")
            break
        else:
            print("Wrong\nYour Total Score is", score, "Thank you for answering my Quiz. GoodBye.")
            break
    else:
        print("Goodbye.")
        break
