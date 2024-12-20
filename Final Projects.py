# Define the Student class with seven fields
class Student:
    def __init__(self, student_id, first_name, last_name, dob, email, major, enrollment_year):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.major = major
        self.enrollment_year = enrollment_year

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.first_name} {self.last_name}, DOB: {self.dob}, Email: {self.email}, Major: {self.major}, Enrollment Year: {self.enrollment_year}"

# Initialize the database as a list
school_database = []

# Function to add a student to the database
def add_student(student):
    school_database.append(student)

# Function to find a student by ID
def find_student(student_id):
    for student in school_database:
        if student.student_id == student_id:
            return student
    return None

# Function to update a student's information
def update_student(student_id, **kwargs):
    student = find_student(student_id)
    if student:
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)

# Function to remove a student from the database
def remove_student(student_id):
    global school_database
    school_database = [student for student in school_database if student.student_id != student_id]

# Main function to interact with the database
def main():
    while True:
        print("\nSchool Database Menu:")
        print("1. Add Student")
        print("2. Find Student")
        print("3. Update Student")
        print("4. Remove Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            email = input("Enter Email: ")
            major = input("Enter Major: ")
            enrollment_year = input("Enter Enrollment Year: ")
            student = Student(student_id, first_name, last_name, dob, email, major, enrollment_year)
            add_student(student)
            print("Student added successfully.")

        elif choice == '2':
            student_id = input("Enter Student ID to find: ")
            student = find_student(student_id)
            if student:
                print("Student found:")
                print(student)
            else:
                print("Student not found.")

        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            student = find_student(student_id)
            if student:
                print("Enter new values for the fields you want to update (leave blank to keep current value):")
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                dob = input("Enter Date of Birth (YYYY-MM-DD): ")
                email = input("Enter Email: ")
                major = input("Enter Major: ")
                enrollment_year = input("Enter Enrollment Year: ")
                update_data = {}
                if first_name:
                    update_data["first_name"] = first_name
                if last_name:
                    update_data["last_name"] = last_name
                if dob:
                    update_data["dob"] = dob
                if email:
                    update_data["email"] = email
                if major:
                    update_data["major"] = major
                if enrollment_year:
                    update_data["enrollment_year"] = enrollment_year
                update_student(student_id, **update_data)
                print("Student updated successfully.")
            else:
                print("Student not found.")

        elif choice == '4':
            student_id = input("Enter Student ID to remove: ")
            remove_student(student_id)
            print("Student removed successfully.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
