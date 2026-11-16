def DailySalesTracker():
    print("Daily Sales Tracker")
    sales = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    total_sales = 0.0

    for day in days:
        sale = float(input(f"Enter sales for {day}: "))
        sales.append(sale)

    for amount in sales:
        total_sales += amount

    print(f"\nTotal sales for the week: ${total_sales:,.2f}")

def analyze_numbers():
    numbers = []
    
    print("Please enter 20 numbers:")
    for i in range(20):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    print("\n--- Number Analysis Results ---")
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average}")

def drivers_license_exam():
    questions = """\
1. What should you do when approaching a stop sign?
   A. Come to a complete stop before the stop line or crosswalk.
   B. Slow down and continue if no other cars are nearby.
   C. Stop only when another vehicle is present.
   D. Honk and proceed carefully.

2. What should you do when an emergency vehicle approaches with its siren on?
   A. Speed up so it can follow you.
   B. Stop immediately in your current lane.
   C. Move to the right and stop when it is safe to do so.
   D. Follow it through traffic.

3. Why should you leave a safe following distance behind the vehicle ahead?
   A. It gives you time and space to react and stop.
   B. It prevents other vehicles from entering your lane.
   C. It allows you to use your high-beam headlights.
   D. It makes your vehicle use less fuel.

4. What should you do when approaching a pedestrian in a marked crosswalk?
   A. Yield and allow the pedestrian to cross.
   B. Drive around the pedestrian without slowing.
   C. Honk so the pedestrian stops.
   D. Stop only if a traffic officer is present.

5. When should you signal before turning or changing lanes?
   A. Only when another vehicle is close behind you.
   B. After you have started turning or changing lanes.
   C. Only at intersections with traffic lights.
   D. In advance, to give other road users time to react."""
    correct_answers = ["A", "C", "A", "A", "D"]
    print("\n--- Driver's License Exam ---")
    print(questions.strip())

    student_answers = []
    for question_number in range(1, len(correct_answers) + 1):
        while True:
            answer = input(
                f"Your answer for question {question_number} (A/B/C/D): "
            ).strip().upper()
            if answer in {"A", "B", "C", "D"}:
                student_answers.append(answer)
                break
            print("Please enter A, B, C, or D.")

    correct_count = 0
    incorrect_questions = []

    for index, answer in enumerate(student_answers):
        if answer == correct_answers[index]:
            correct_count += 1
        else:
            incorrect_questions.append(index + 1)

    if correct_count > 3:
        print("Result: PASSED")
    else:
        print("Result: FAILED")

    print(f"Total correctly answered questions: {correct_count}")
    print(f"Total incorrectly answered questions: {len(incorrect_questions)}")

    if incorrect_questions:
        print("Question numbers of incorrectly answered questions:", incorrect_questions)
    else:
        print("Congratulations! No incorrect answers.")

def Prime_number_Gen(num):
    """Checks if a number is prime and prints it if it is."""
    if num < 2:
        return
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

def prime_number_generator():
    limit = int(input("Enter an integer greater than 1: "))
    while limit <= 1:
        print("Invalid input. Please enter a number greater than 1.")
        limit = int(input("Enter an integer greater than 1: "))
        
    numbers = list(range(2, limit + 1))
    
    print(f"\nPrime numbers less than or equal to {limit}:")
    for number in numbers:
        Prime_number_Gen(number)
    print()

def main():
    while True:
        print("\nHello, welcome to the program! please select an option below.")
        print("[1] Total Sales Tracker")
        print("[2] Number Analysis Program")
        print("[3] Drivers License Exam")
        print("[4] Prime Number Generator")
        print("[q] Quit")

        choice = input("What would you like to do? ").strip().lower()

        if choice == "1":
            DailySalesTracker()
        elif choice == "2":
            analyze_numbers()
        elif choice == "3":
            drivers_license_exam()
        elif choice == "4":
            prime_number_generator()
        elif choice == "q":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()