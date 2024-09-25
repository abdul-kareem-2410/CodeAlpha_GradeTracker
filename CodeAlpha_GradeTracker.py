# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'


# Main grade tracker function
def grade_tracker():
    subjects = ["English", "Computer Graphics", "Discrete Mathematics",
                "Probability and Statistics", "Python", "Web Technologies", "Psychology"]

    students = {}

    while True:
        student_name = input("Enter the student's name (or type 'done' to finish): ")
        if student_name.lower() == 'done':
            break

        # Dictionary to store subject marks for the student
        grades = {}
        total_marks = 0

        for subject in subjects:
            while True:
                try:
                    marks = float(input(f"Enter marks for {subject} (0-100): "))
                    if 0 <= marks <= 100:
                        break
                    else:
                        print("Marks should be between 0 and 100. Try again.")
                except ValueError:
                    print("Invalid input! Please enter numerical marks between 0 and 100.")

            grades[subject] = marks
            total_marks += marks

        # Calculate percentage and grade
        percentage = (total_marks / 700) * 100
        grade = calculate_grade(percentage)

        # Store student data
        students[student_name] = {
            "grades": grades,
            "total_marks": total_marks,
            "percentage": percentage,
            "grade": grade
        }

    # Display all student data if there are entries
    if students:
        print("\nStudent Grade Report:")
        for student, data in students.items():
            print(f"\nGrades for {student}:")
            for subject, marks in data['grades'].items():
                print(f"{subject}: {marks}")
            print(f"Total Marks: {data['total_marks']} / 700")
            print(f"Percentage: {data['percentage']:.2f}%")
            print(f"Final Grade: {data['grade']}")
    else:
        print("No students or grades were entered.")

1
# Call the function to run the program
grade_tracker()
