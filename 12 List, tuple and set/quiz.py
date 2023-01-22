
questions = ["1. What is the longest river in the world?",
             "2. When was the first Harry Potter book published?",
             "3. Which country won the first Football World Cup in 1930?",
             "4. In which city were the 2000 Summer Olympics held?",
             "5. Who was the first woman to win a Nobel Prize?",
             "6. Which Friends character's famous pickup line is “How you doin'?",
             "7. In The Lion King, who is Simba's uncle?",
             "8. Which chemical element has Ag as a symbol?",
             "9. What is the highest mountain in Japan?",
             "10. Which fruit is at the top of the Wimbledon gentlemen’s singles trophy?"
             ]
options = [['A. Amazon River', 'B. Nile', 'C. Yellow River', 'D. Congo River'],
           ['A. 1997', 'B. 1999', 'C. 2001', 'D. 2003'],
           ['A. Brazil', 'B. Portugal', 'C. Italy', 'D. Uruguay'],
           ['A. London', 'B. Paris', 'C. Barcelona', 'D. Sydney'],
           ['A. Mother Teresa', 'B. Marie Curie', 'C. Jane Adams', 'D. Alva Myrdal'],
           ['A. Joey', 'B. Ross', 'C. Chandler', 'D. Mike'],
           ['A. Mufasa', 'B. Scar', 'C. Timon', 'D. Zazu'],
           ['A. Gold', 'B. Silver', 'C. Iron', 'D. Carbon'],
           ['A. Mount Tate', 'B. Mount Kita', 'C. Mount Fuji', 'D. Mount Yari'],
           ['A. Strawberry', 'B. Pineapple', 'C. Mango', 'D. Apple']
           ]

answers = ['B', 'A', 'D', 'D', 'B', 'A', 'B', 'B', 'C', 'B']

my_answers = []

score = 0

op_num = 0

print('-'*130)


while True:
    flag = input("Do you want to play Quiz? (Y/N): ")
    print('-'*130)
    if flag.lower() == 'y':
        for ques in questions:          # showing questions
            print(ques)         
            print()

            for s in options[op_num]:   # showing options
                print(s)
            print()

            while True:
                my_option = input("Choose your option : ")       # taking user option
                if my_option.upper() not in ['A','B','C','D']:  # checking valid options given by user or not
                    print("Please Select Valid Option(A/B/C/D): ")
                    continue
                else:
                    if my_option.upper() != answers[op_num]:    # checking user answer with right answer
                        print("Wrong Answer : Bad luck!")
                        print(f"Right Asnwer is Option '{answers[op_num]}'")
                    else:
                        print("Correct Answer!")
                        score += 1                              # increasing scores if user gives right answer 
                        my_answers.append(my_option.upper())
                    break

            print()
            op_num += 1

        # ------------ Score Evaluation --------------- #

        print()
        print('------------------ Results-------------------')
        print()

        print(f"You have given total of {score} correct answers out of {len(answers)}")

        score = int((score / len(questions))*100)
        print(f"Your Score is {score}%")
        print()

    elif flag.lower() == 'n':
        print("Try next time")

    else:
        print("You Selected Invalid Option. Please Select Valid Options(Y/N): ")
        continue
    break


