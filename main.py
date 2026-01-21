# Student Result Management System
# Author: SALAMI FOLORUNSHO 24/14785

students = {}  # Dictionary to store student name and score

def add_student():
    while True:
        name = input("Enter student name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        if name == "":
            print("Name cannot be empty.")
            continue

        score_input = input(f"Enter score for {name}: ").strip()
        if not score_input.isdigit():
            print("Score must be a number between 0 and 100.")
            continue
        score = int(score_input)
        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            continue

        students[name] = score
        print(f"Student {name} added successfully!")

def view_students():
    if not students:
        print("No students added yet.")
        return

    print("\n--- Student Results ---")
    total_score = 0
    for name, score in students.items():
        print(f"{name}: {score}")
        total_score += score

    average = total_score / len(students)
    print(f"\nTotal Students: {len(students)}")
    print(f"Average Score: {average:.2f}")

def main():
    while True:
        print("\nStudent Result Management System")
        print("1. Add Student(s)")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
