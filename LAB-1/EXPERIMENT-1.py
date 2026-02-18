class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
        self.next = None

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        total_points = sum(self.grades.values())
        return round(total_points / len(self.grades), 2)


class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, name, student_id, grades):
        new_student = Student(name, student_id, grades)
        new_student.next = self.head
        self.head = new_student

    def display_students(self):
        if not self.head:
            print("No students found in the list")
            return

        current = self.head
        while current:
            print(f"Name: {current.name}, Student ID: {current.student_id}, GPA: {current.calculate_gpa()}")
            current = current.next

    def calculate_average_gpa(self):
        total_gpa = 0
        total_students = 0
        current = self.head

        while current:
            total_gpa += current.calculate_gpa()
            total_students += 1
            current = current.next

        if total_students == 0:
            return 0.0

        return round(total_gpa / total_students, 2)

    def get_gpa_grade(self):
        average_gpa = self.calculate_average_gpa()

        if average_gpa >= 3.7:
            return 'A'
        elif 3.0 <= average_gpa < 3.7:
            return 'B'
        elif 2.0 <= average_gpa < 3.0:
            return 'C'
        elif 1.0 <= average_gpa < 2.0:
            return 'D'
        else:
            return 'F'
        
    def add_student_from_input(self):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")

        grades = {}
        num_subjects = int(input("Enter number of subjects: "))

        for i in range(num_subjects):
            subject = input(f"Enter subject {i+1} name: ")
            grade = float(input(f"Enter grade for {subject}: "))
            grades[subject] = grade

        self.add_student(name, student_id, grades)
        print("Student added successfully!\n")


if __name__ == '__main__':
    student_list = StudentList()

    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Show Class Average GPA")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_list.add_student_from_input()

        elif choice == '2':
            print("\nList of Students:")
            student_list.display_students()

        elif choice == '3':
            avg = student_list.calculate_average_gpa()
            grade = student_list.get_gpa_grade()
            print(f"\nOverall Class Average GPA: {avg}")
            print(f"Overall Class Grade: {grade}")

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")
