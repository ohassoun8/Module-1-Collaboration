# Author: Othman Hassoun
# File Name: student_qualifications.py
# Description: This app accepts student names and GPAs, checks if they qualify for the Dean's List or Honor Roll,
# and prints appropriate messages. The app stops processing when the last name entered is 'ZZZ'.

def main():
    print("Welcome to the Dean's List and Honor Roll Checker")

    while True:
        # Ask for and accept the student's last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()

        # Quit processing if the last name is 'ZZZ'
        if last_name.upper() == 'ZZZ':
            print("Exiting the program. Goodbye!")
            break

        # Ask for and accept the student's first name
        first_name = input("Enter the student's first name: ").strip()

        # Ask for and accept the student's GPA as a float
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid GPA. Please enter a numeric value.")
            continue

        # Test if the student qualifies for the Dean's List or Honor Roll
        if gpa >= 3.5:
            print(f"Congratulations, {first_name} {last_name}! You have made the Dean's List.")
        elif gpa >= 3.25:
            print(f"Well done, {first_name} {last_name}! You have made the Honor Roll.")
        else:
            print(f"Keep working hard, {first_name} {last_name}! Your current GPA is {gpa:.2f}.")

if __name__ == "__main__":
    main()