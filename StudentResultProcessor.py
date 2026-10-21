import csv
import os

FILE_NAME = "student_result.csv"

def load_results():
    students = []
    if not os.path.exists(FILE_NAME):
        return students
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
           
            for row in reader:
                try:
                    name = row["name"].strip()
                    average = float(row["average"])
                    grade = row["grade"].strip()


                    if name and 0 <= average <= 100:
                        students.append({
                            "name": name,
                            "average": average,
                            "grade": grade
                        })
                except (ValueError, KeyError, TypeError):
                    continue
    except Exception as error:
        print(f"Error Loading results: {error}")
    return students 



def calculate_average(scores):
    return sum(scores) / len(scores)


def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))


            if number > 0:
                return number

            print("Error: please enter a positive integers")
        except ValueError:
            print("Error: enter a valid whole number")


def get_scores(number):

    while True:
        try:
            score = float(input(f"score {number}: "))

            if 0 <= score <= 100:
                return score

            print("Error: please enter a score between 0 and 100")
        except ValueError:
            print("Error: please enter a valid number")



def add_student(students, expected_subjects):
    name = input("Student name: ").strip()


    if not name:
        print("Error: student name cannot be empty.")
        return expected_subjects

    number_of_subjects = get_positive_integer(
        "Number of Subjects: "
    )

    if expected_subjects is not None:
        if number_of_subjects != expected_subjects:
            print(
                f"Error: each student must have "
                f"{expected_subjects} subjects."
            )
            return expected_subjects
    else:
        expected_subjects = number_of_subjects


    scores = []

    for number in range(1, number_of_subjects + 1):
        scores.append(get_scores(number))

    average = calculate_average(scores)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print("\nStudent result:")
    print(f"Name: {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}\n")

    return expected_subjects


def class_sumarry(students):
    if not students:
        print("No student results available.")
        return

    total = sum(student["average"] for student in students)
    class_average = total / len(students)

    highest_student = max(students, key=lambda student: student["average"])
    lowest_student = min(students, key=lambda student: student["average"])

    print("\n-- Class Summary --")
    print(f"Number of Students: {len(students)}")
    print(f"Class Average: {class_average:.2f}")
    print(
        f"Highest: {highest_student['name']} "
        f"({lowest_student['average']:.2f})"


    )


def save_results(students):
    try:
        with open(
            FILE_NAME, "w", newline="", encoding="utf-8"
        ) as file:
            fieldnames = ["name", "average", "grade"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()


            for students in students:
                writer.writerow({
                    "name": students["name"],
                    "average": f"{students['average']:.2f}",
                    "grade": students["grade"]
                })
        print(f"Results saved to {FILE_NAME}.")

    except OSError as error:
        print(f"Error saving results: {error}")



def main():
    students = load_results()
    expected_subjects = None

    print("== Students Result Processor ==")


    if students:
        print(f"Loaded {len(students)} previously saved students results.")

    while True:
        print("\n--- Student Result Processor ---")
        print("1. Add Student Result")
        print("2. View Class Summary")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            expected_subjects = add_student(
                students, expected_subjects
                )
        elif choice == "2":
            class_sumarry(students)

        elif choice == "3":
            save_results(students)

        elif choice == "4":
            save_results(students)
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
