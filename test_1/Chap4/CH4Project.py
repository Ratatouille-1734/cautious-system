def main():
    greeting = "Welcome to your personal computer assistant. =)"
    
    while True:
        print(f"\n{greeting}\n")
        print("[1] Enter 1 to Generate a Design.")
        print("[2] Enter 2 to Activate Budget Mode.")
        print("[3] Enter 3 to Project Future Income.")
        print("[q] Enter q to quit.\n")
        
        choice = input("What would you like to do? ").strip()
        
        if choice == '1':
            print()
            for i in range(7, 0, -1):
                print("*" * i)
            print("\nWell, ain't that cute with 7 rows!")
            
        elif choice == '2':
            print("\nBudget mode activated.\n")
            try:
                budget = float(input('How much did you budget for "this" month? '))
            except ValueError:
                budget = 0.0
                
            total_expenses = 0.0
            count = 1
            
            while True:
                try:
                    exp = float(input(f"Amount of Expense #{count}? (Type -1 to quit.)"))
                except ValueError:
                    continue
                    
                if exp == -1:
                    break
                total_expenses += exp
                count += 1
                
            if total_expenses > budget:
                over_amount = int(total_expenses - budget)
                print(f"Okay, the bad news is you are over budget by ${over_amount} but the good news is, I found these lottery numbers! 7559710")
            
            # Update greeting for subsequent loops to match sample flow
            greeting = "Welcome to the nature center. What would you like to do?"
            
        elif choice == '3':
            try:
                days = int(input("How many days do you plan to work?"))
            except ValueError:
                days = 0
                
            total = 0.0
            amount = 0.01
            
            for day in range(1, days + 1):
                if day > 1:
                    amount *= 2
                total += amount
                print(f"Day {day}\t\t${amount:,.2f}")
                
            print(f"\nYou made a total of ${total:,.2f}\n")
            
        elif choice.lower() == 'q':
            print("\nThanks again, bye now.")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()