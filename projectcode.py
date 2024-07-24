# initializing dictionary
stu_grades = {} 

# Add a new student
def add_student(name, grade): #function definition
    if name in stu_grades:    #check if name is in stu_grades or not
        stu_grades[name]  
    else:
        stu_grades[name] = [grade]   #if not then data will added on new dictionary
    print(f"Added {name} with marks: {grade}")

# Update a student
def update_student(name, grade):
    if name in stu_grades:
        stu_grades[name] = [grade]  # Replace the existing grades with the new grade  
        print(f"Updated {name} with a {grade}")
    else:
        add_student(name, grade)

# Displaying all students and their grades
def display_students():
    if stu_grades:
        for name, grades in stu_grades.items():
            average_grade = sum(grades) / len(grades)
            print(f"{name} : {grades} (Average grade : {average_grade:.2f})")
    else:
        print("No students in the list")

# Validate student name
def valid_name():
    while True:
        name = input("Enter the name of the student: ")
        if name.isalpha():
            return name
        else:
            print("Invalid input. The name should only contain alphabetic characters.")

# Validate student grade 
def valid_grade():
    while True:
        try:            #prints exceptional  value
            grade = float(input("Enter the grade of the student (0-100): ").strip())    # Strip() removes space
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main logic of this program
def main():
    while True:

        print("\nStudent Grades Management System")
        print("add - Add a student")
        print("update - Update a student")
        print("view - Display all students")
        print("exit - Exit")

        choice = input("What do you want to do? ")
        if choice == "add":
            name = valid_name()
            grade = valid_grade()
            add_student(name, grade)
        elif choice == "update":
            name = valid_name()
            grade = valid_grade()
            update_student(name, grade)
        elif choice == "view":
            display_students()
        elif choice == "exit":
            print("Closing the program...")
            break
        else:
            print("Invalid choice. Please try again.")

main()

