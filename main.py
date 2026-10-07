
students = {}


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    if student_id in students:
        print("A student with this ID already exists.")
        return

    students[student_id] = {
        "name": name,
        "grades": []
    }

    print("Student added successfully.")


def remove_student():
    student_id = input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    del students[student_id]
    print("Student removed successfully.")


def display_students():
    if not students:
        print("No students found.")
        return

    print("\nStudents:")

    for student_id, student in students.items():
        print(f"ID: {student_id} | Name: {student['name']}")


def add_grade():
    student_id = input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    try:
        grade = float(input("Enter grade: "))

        if grade < 0 or grade > 20:
            print("Grade must be between 0 and 20.")
            return

        students[student_id]["grades"].append(grade)
        print("Grade added successfully.")

    except ValueError:
        print("Please enter a valid number.")


def calculate_average():
    student_id = input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    grades = students[student_id]["grades"]

    if not grades:
        print("This student has no grades.")
        return

    average = sum(grades) / len(grades)

    print(
        f"{students[student_id]['name']}'s average: "
        f"{average:.2f}"
    )


def highest_average():
    best_student = None
    best_average = -1

    for student_id, student in students.items():

        if not student["grades"]:
            continue

        average = sum(student["grades"]) / len(student["grades"])

        if average > best_average:
            best_average = average
            best_student = student

    if best_student is None:
        print("No student has any grades.")
        return

    print(
        f"Student with highest average: "
        f"{best_student['name']} - {best_average:.2f}"
    )


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Display all students")
        print("4. Add a grade")
        print("5. Calculate a student's average")
        print("6. Find student with highest average")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            display_students()

        elif choice == "4":
            add_grade()

        elif choice == "5":
            calculate_average()

        elif choice == "6":
            highest_average()

        elif choice == "0":
            print("Goodbye!")
            break
main()
