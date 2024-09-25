**Student Grade Tracker**

**Overview**
The Student Grade Tracker is a simple Python program that allows users to track grades for multiple students across seven predefined subjects. It calculates the total marks, percentage, and assigns a grade based on the percentage obtained by each student.

**Subjects:**
English
Computer Graphics
Discrete Mathematics
Probability and Statistics
Python
Web Technologies
Psychology

Each subject has a maximum score of 100, and the total score is 700.

**Features**
Input student names and their respective grades for each of the 7 subjects.
Calculate the total marks, percentage, and final grade based on the following grade system:
A+: 90% and above
A: 80% to 89%
B: 70% to 79%
C: 60% to 69%
D: 50% to 59%
F: Below 50%
Allows multiple students to be tracked in a single run.
Displays a well-formatted summary of each student’s performance.

**Installation and Usage**

**Prerequisites**
Python 3.x

**How to Run**
Clone or download the project files.
Navigate to the directory where the script (CodeAlpha_GradeTracker.py) is located.
Run the program using Python:

**Program Flow**
The program will first prompt for the student’s name.
After entering the name, it will automatically ask for marks in each of the 7 subjects.
Once the marks for all subjects are entered, the program calculates:
Total marks (out of 700)
Percentage
Final grade based on the percentage
Repeat for multiple students by entering new names. To stop entering students, type done when prompted for the student's name.
After all entries, the program will print a detailed summary of each student’s grades, percentage, and final grade.

**Example Output**
Enter the student's name (or type 'done' to finish): Ali
Enter marks for English (0-100): 85
Enter marks for Computer Graphics (0-100): 90
Enter marks for Discrete Mathematics (0-100): 75
Enter marks for Probability and Statistics (0-100): 80
Enter marks for Python (0-100): 95
Enter marks for Web Technologies (0-100): 88
Enter marks for Psychology (0-100): 70

Enter the student's name (or type 'done' to finish): done

Student Grade Report:

Grades for Ali:
English: 85
Computer Graphics: 90
Discrete Mathematics: 75
Probability and Statistics: 80
Python: 95
Web Technologies: 88
Psychology: 70
Total Marks: 583 / 700
Percentage: 83.29%
Final Grade: A

**Customization**
If you wish to modify the grade system or the subjects, you can edit the subjects list and the calculate_grade() function in the script. This allows you to add or remove subjects or tweak the grade boundaries
