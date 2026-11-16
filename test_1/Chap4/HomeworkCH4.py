access= input("Access Bug collector? Y/N:").upper()

if access =="Y":
    total_bugs = 0

    for day in range(1, 6):
        bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
        total_bugs += bugs

    print(f"\nTotal number of bugs collected over 5 days: {total_bugs}")
else: print("access denied")

access= input("Access Calrories burnt? Y/N:").upper()

if access =="Y":


    calories_per_minute = 4.2

    print(f"{'Minutes':<10}{'Calories Burned':<20}")
    print("-" * 30)

    for minutes in range(10, 31, 5):
        calories_burned = calories_per_minute * minutes
        print(f"{minutes:<10}{calories_burned:<20.1f}")
else:
    print("access denied")

access= input("Access Distance traveled? Y/N:").upper()

if access =="Y":
    speed = float(input("What is the speed of the vehicle in mph? "))
    hours = int(input("How many hours has it traveled? "))

    print(f"\n{'Hour':<10}{'Distance Traveled':<20}")
    print("-" * 30)

    for hour in range(1, hours + 1):
        distance = speed * hour
        print(f"{hour:<10}{distance:<20.1f}")
else:
    print("access denied")

access= input("Access Rainfall information? Y/N:").upper()

if access =="Y":
    years = int(input("Enter the number of years: "))
    total_rainfall = 0
    total_months = years * 12

    for year in range(1, years + 1):
        print(f"\n--- Year {year} ---")
        for month in range(1, 13):
            rainfall = float(input(f"Enter inches of rainfall for month {month}: "))
            total_rainfall += rainfall

    average_rainfall = total_rainfall / total_months

    print("\n--- Summary ---")
    print(f"Total months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")
else:
    print("access denied")

access= input("Access Celsius to Fahrenheit? Y/N:").upper()

if access =="Y":
    print(f"{'Celsius':<10}{'Fahrenheit':<15}")
    print("-" * 25)

    for celsius in range(21):
        fahrenheit = (9/5) * celsius + 32
    print(f"{celsius:<10}{fahrenheit:<15.1f}")
else:
    print("access denied")

access= input("Access Penny for pay? Y/N:").upper()

if access =="Y":
    days = int(input("Enter the number of days: "))
    total_pay_pennies = 0
    daily_pay_pennies = 1

    print(f"\n{'Day':<10}{'Salary ($)':<15}")
    print("-" * 25)

    for day in range(1, days + 1):
        salary_dollars = daily_pay_pennies / 100.0
        print(f"{day:<10}${salary_dollars:<14.2f}")
        total_pay_pennies += daily_pay_pennies
        daily_pay_pennies *= 2

        total_pay_dollars = total_pay_pennies / 100.0
        print("-" * 25)
    print(f"Total Pay: ${total_pay_dollars:.2f}")
else:
    print("access denied")

access= input("Access Weight loss? Y/N:").upper()

if access =="Y":
    starting_weight = float(input("Enter your starting weight (in pounds): "))
    loss_per_month = 4

    print(f"\n{'Month':<10}{'Expected Weight (lbs)':<25}")
    print("-" * 35)

    current_weight = starting_weight
    for month in range(1, 7):
        current_weight -= loss_per_month
        print(f"{month:<10}{current_weight:<25.1f}")
else:
    print("access denied")


access= input("Access Star pattern 1? Y/N:").upper()

if access =="Y":
    for i in range(7, 0, -1):
        print("*" * i)
else:    print("access denied")

access= input("Access Star pattern 2? Y/N:").upper()

if access =="Y":
    print("##")
    for spaces in range(1, 5):
        print("#" + " " * spaces + "#")
    print("#     #")
else:
    print("access denied")    