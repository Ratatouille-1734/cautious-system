import random


def save_robot_scores():
    filename = "roboscores.txt"
    with open(filename, "w") as file:
        print("Enter team records (type 'done' for team name when finished):")
        while True:
            team_name = input("Enter team name: ")
            if team_name.lower() == 'done':
                break
            try:
                score = float(input(f"Enter Robo Rank Score (RRS) for {team_name}: "))
               
                file.write(f"{team_name},{score}\n")
            except ValueError:
                print("Please enter a valid numeric score.")
    print(f"\nRecords successfully saved to '{filename}'.")

def display_robot_scores():
    filename = "roboscores.txt"
    try:
        with open(filename, "r") as file:
            print("\n--- Robot Olympics Leaderboard ---")
            print(f"{'Team Name':<20} | {'RRS Score':<10}")
            print("-" * 35)
            for line in file:
                if line.strip():
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        name, score = parts
                        print(f"{name:<20} | {score:<10}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")


def generate_the_file():
    filename = "the.txt"
    with open(filename, "w") as file:
        for _ in range(365):
            daily_count = random.randint(0, 100)
            file.write(f"{daily_count}\n")
    print(f"Successfully generated 365 numbers and saved to '{filename}'.")

def calculate_monthly_averages():
    filename = "the.txt"
    
    month_names = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
        if len(lines) < 365:
            print("Error: The file does not contain all 365 days of data.")
            return
            
        day_index = 0
        print("\n--- Monthly Average 'The' Counts ---")
        for name, days in zip(month_names, month_days):
            month_total = 0
            for _ in range(days):
                month_total += int(lines[day_index].strip())
                day_index += 1

            monthly_avg = round(month_total / days)
            print(f"{name} average 'the's : {monthly_avg} per day")
            
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except ValueError:
        print("Error: Invalid data format found in the file.")

def main():
    while True:
        print("\nRobot Olympics and Monthly Averages")
        print("[1] Enter robot team scores")
        print("[2] Display robot leaderboard")
        print("[3] Generate daily 'the' counts")
        print("[4] Calculate monthly averages")
        print("[q] Quit")

        choice = input("What would you like to do? ").strip().lower()

        if choice == "1":
            save_robot_scores()
        elif choice == "2":
            display_robot_scores()
        elif choice == "3":
            generate_the_file()
        elif choice == "4":
            calculate_monthly_averages()
        elif choice == "q":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()