import random


def generate_problem():
  """Generates a random math problem (+, -, *, /), prints it in a

  vertical format, and returns the correct answer.
  """
  operators = ["+", "-", "*", "/"]
  op = random.choice(operators)

  if op == "+":
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f"\n  {num1}\n+ {num2}\n-------")

  elif op == "-":
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    # Ensure num1 >= num2 to keep subtraction beginner-friendly
    if num1 < num2:
      num1, num2 = num2, num1
    correct_answer = num1 - num2
    print(f"\n  {num1}\n- {num2}\n-------")

  elif op == "*":
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    correct_answer = num1 * num2
    print(f"\n  {num1}\n* {num2}\n-------")

  else:  # Division
    # Generate numbers that cleanly divide into whole numbers
    num2 = random.randint(1, 12)
    quotient = random.randint(1, 12)
    num1 = num2 * quotient
    correct_answer = quotient
    print(f"\n  {num1}\n/ {num2}\n-------")

  return correct_answer


def ask_and_check(correct_answer):
  """Asks for user input, checks if 'done', and compares

  the user's answer to the correct answer.
  """
  user_input = input("Your answer: ").strip().lower()

  if user_input == "done":
    return "done"

  try:
    user_answer = float(user_input)
    # Compare rounded values to handle standard float representation
    if round(user_answer, 2) == round(float(correct_answer), 2):
      print("Correct! Great job!")
      return True
    else:
      print(f"Incorrect. The correct answer was {correct_answer}.")
      return False
  except ValueError:
    print('Invalid input. Please enter a valid number or type "done".')
    return False


def main():
  print("=== Welcome to the Math Quiz Game! ===")
  print('Type "done" at any time to finish and view your final score.\n')

  total_questions = 0
  correct_answers = 0
  incorrect_answers = 0

  while True:
    correct_ans = generate_problem()
    result = ask_and_check(correct_ans)

    if result == "done":
      break

    total_questions += 1
    if result:
      correct_answers += 1
    else:
      incorrect_answers += 1

  # Final Statistics Output
  print("\n" + "=" * 30)
  print("       QUIZ SUMMARY       ")
  print("=" * 30)
  print(f"Number of questions answered : {total_questions}")
  print(f"Number of correct answers    : {correct_answers}")
  print(f"Number of incorrect answers  : {incorrect_answers}")

  if total_questions > 0:
    percentage = (correct_answers / total_questions) * 100
    print(
        f"Grade                        : {correct_answers}/{total_questions}"
        f" ({percentage:.1f}%)"
    )
  else:
    print("Grade                        : No questions answered.")
  print("=" * 30)


if __name__ == "__main__":
  main()