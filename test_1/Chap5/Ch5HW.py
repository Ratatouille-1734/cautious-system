import random

def generate_problem():

    operations = ['+', '-', '*', '/']
    op = random.choice(operations)
    
    if op == '+':
        num1 = random.randint(1, 500)
        num2 = random.randint(1, 500)
        correct_answer = num1 + num2
        print(f"\n{num1}")
        print(f"+ {num2}")
        print("-" * 6)
        
    elif op == '-':
        num1 = random.randint(1, 500)
        num2 = random.randint(1, num1)  
        correct_answer = num1 - num2
        print(f"\n{num1}")
        print(f"- {num2}")
        print("-" * 6)
        
    elif op == '*':
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        correct_answer = num1 * num2
        print(f"\n{num1} * {num2}")
        
    elif op == '/':
       
        num2 = random.randint(1, 12)
        quotient = random.randint(1, 12)
        num1 = num2 * quotient
        correct_answer = quotient
        print(f"\n{num1} / {num2}")
        
    return correct_answer

def ask_and_check(correct_answer):

    while True:
        user_input = input("Your answer (or type 'done' to finish): ").strip().lower()
        
        if user_input == 'done':
            return 'done'
        
        try:
            user_answer = float(user_input)
            if user_answer == correct_answer:
                print("Congratulations! That's correct!")
                return True
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.")
                return False
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'done'.")

def main():
    print("==================================")
    print("    WELCOME TO THE MATH QUIZ!     ")
    print("==================================")
    print("Type 'done' at any prompt to exit and see your final score.\n")
    
    total_questions = 0
    correct_answers = 0
    incorrect_answers = 0
    
    while True:
        correct_ans = generate_problem()
        result = ask_and_check(correct_ans)
        
        if result == 'done':
            break
        
        total_questions += 1
        if result:
            correct_answers += 1
        else:
            incorrect_answers += 1
            

    print("\n" + "=" * 30)
    print("          QUIZ SUMMARY          ")
    print("==================================")
    print(f"Total questions answered: {total_questions}")
    print(f"Correct answers:          {correct_answers}")
    print(f"Incorrect answers:        {incorrect_answers}")
    
    if total_questions > 0:
        percentage = (correct_answers / total_questions) * 100
        print(f"Your Grade:               {correct_answers}/{total_questions} ({percentage:.1f}%)")
    else:
        print("No questions were attempted.")
    print("==================================")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()