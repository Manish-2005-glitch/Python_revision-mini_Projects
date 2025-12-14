questions = (("Which planet is known as the “Red Planet”?"),
("Who wrote the famous play Romeo and Juliet?"),
("What is the chemical symbol for Gold?"),
("Which is the largest ocean on Earth?"))

options =(("A. Venus","B. Saturn","C. Mars","D. Jupiter"),
("A. Charles Dickens","B. William Shakespeare","C. Mark Twain","D. Jane Austen"),
("A. Au","B. Ag","C. Go","D. Gd"),
("A. Atlantic Ocean","B. Indian Ocean","C. Pacific Ocean","D. Arctic Ocean"))

answers = ("C","B","A","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("enter the correct option: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("correct!")
    else:
        print("incorrect!")
        print(f"the correct answer is {answers[question_num]}")


    question_num +=1

print("answers:", end=" ")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses:", end=" ")
for guess in guesses:
    print(guess, end = " ")
print()
