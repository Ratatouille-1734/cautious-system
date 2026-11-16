import random


def create_numbers_file():
    with open("numbers.txt", "w") as file:
        for i in range(1, 21):
            file.write(f"{i * 5}\n")

def display_numbers():
    try:
        with open("numbers.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("The file 'numbers.txt' was not found.")

def line_numbers_program():
    filename = input("Enter the name of the file: ")
    try:
        with open(filename, "r") as file:
            line_num = 1
            for line in file:
                print(f"{line_num}: {line.strip()}")
                line_num += 1
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")


def display_first_n_numbers(n):
    try:
        with open("numbers.txt", "r") as file:
            for index, line in enumerate(file):
                if index >= n:
                    break
                print(line.strip())
    except FileNotFoundError:
        print("The file 'numbers.txt' was not found.")


def random_number_writer():
    try:
        count = int(input("How many random numbers should be written to the file? "))
        filename = input("Enter the filename to save to (e.g., random_numbers.txt): ")
        
        with open(filename, "w") as file:
            for _ in range(count):
                number = random.randint(1, 500)
                file.write(f"{number}\n")
                
        print(f"Successfully wrote {count} random numbers to '{filename}'.")
    except ValueError:
        print("Please enter a valid integer for the count.")


def random_number_reader():
    filename = input("Enter the filename to read from: ")
    total = 0
    count = 0
    
    try:
        with open(filename, "r") as file:
            print("\nNumbers found in the file:")
            for line in file:
                number = int(line.strip())
                print(number)
                total += number
                count += 1
                
        print(f"\nTotal of the numbers: {total}")
        print(f"Number of random numbers read: {count}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")


def random_number_reader_with_exceptions():
    filename = input("Enter the filename to read from: ")
    total = 0
    count = 0
    
    try:
        with open(filename, "r") as file:
            print("\nNumbers found in the file:")
            for line in file:
                try:
                    number = int(line.strip())
                    print(number)
                    total += number
                    count += 1
                except ValueError:
                    print(f"Warning: Could not convert line '{line.strip()}' to an integer. Skipping.")
                    
        print(f"\nTotal of the numbers: {total}")
        print(f"Number of random numbers read: {count}")
        
    except IOError:
        print(f"An error occurred while opening or reading the file '{filename}'.")


def personal_web_page_generator():
    name = input("Enter your name: ")
    description = input("Describe yourself: ")
    
    html_content = f"""<html>
<head>
</head>
<body>
   <center>
      <h1>{name}</h1>
   </center>
   <hr />
   {description}
   <hr />
</body>
</html>
"""
    
    filename = "my_profile.html"
    with open(filename, "w") as file:
        file.write(html_content)
        
    print(f"\nWeb page successfully created and saved as '{filename}'!")


def main():
    greeting = "Welcome. Please select an option. =)"
    
    while True:
        print(f"\n{greeting}\n")
        print("[1] Enter 1 to enter File Display.")
        print("[2] Enter 2 to enter File Head Display.")
        print("[3] Enter 3 to enter Line Numbers.")
        print("[4] Enter 4 to enter Random number file writer and reader.")
        print("[5] Enter 5 to enter Exception Handling.")
        print("[6] Enter 6 to enter Personal web page generator.")
        print("[q] Enter q to quit.\n")
        
        choice = input("What would you like to do? ").strip()
        
        if choice == '1':
            print("\nFile Display Activated.\n")
            create_numbers_file()
            print("--- Displaying Numbers from File ---")
            display_numbers()
        elif choice == '2':
            print("\nFile Head Display Activated.\n")
            create_numbers_file()
            print("--- Displaying First 5 Numbers from File ---")
            display_first_n_numbers(5)
        elif choice == '3':
            print("\nLine Numbers Activated.\n")
            line_numbers_program()
        elif choice == '4':
            print("\nRandom Number File Writer and Reader Activated.\n")
            random_number_writer()
            random_number_reader()
        elif choice == '5':
            print("\nException Handling Activated.\n")
            random_number_reader_with_exceptions()
        elif choice == '6':
            print("\nPersonal Web Page Generator Activated.\n")
            personal_web_page_generator()
        elif choice.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")      


if __name__ == "__main__":
    main()