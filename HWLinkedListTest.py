from Student import Student
from HWLinkedList import HWLinkedList

# Boolean to control whether the menu should continue running
run = True 
# Initialize the linked list to store students
students = HWLinkedList()

while run:
    # Display menu options and get user input
    options = int(input("Choose from the following options: \n1. Add a new student to the end \n2. Add a new student to the head"+
                        "\n3. Remove a student \n4. Search for a student \n5. Print all students \n6. QUIT\n\n"))
    
    # Option 6: Quit the program
    if options == 6:
        print("Goodbye.")
        run = False  # Set run to False to stop the loop

    # Option 1: Add a new student to the end of the list
    elif options == 1:
        name = input("What is the name of the student you would like to add? ")
        house = input("What house are they in? ")
        student = Student(name=name, house=house)  # Create a new Student object
        students.add(student)  # Add student to the end of the list
        print(f"{name} from house {house} was added at the end of the list.")

    # Option 2: Add a new student to the head of the list
    elif options == 2:
        name = input("What is the name of the student you would like to add? ")
        house = input("What house are they in? ")
        student = Student(name=name, house=house)  # Create a new Student object
        students.addAtHead(student)  # Add student to the beginning of the list
        print(f"{name} from house {house} was added at the beginning of the list.")

    # Option 3: Remove a student from the list
    elif options == 3:
        name = input("What is the name of the student you would like to remove? ")
        removal = Student(name=name)  # Create a Student object with just the name for comparison
        # Attempt to remove the student from the list
        if students.remove(students.head, None, removal):
            print(f"{name} has been removed.")
        else:
            print(f"{name} was not found.")  # If the student isn't found, notify the user
    
    # Option 4: Search for a student in the list
    elif options == 4:
        name = input("What student would you like to search for? ")
        search = Student(name=name)  # Create a Student object with just the name for comparison
        # Search for the student in the list
        if students.searchList(students.head, search=search):
            print(f"{name} was found.")
        else:
            print(f"{name} was not found.")  # Notify user if student is not found
    
    # Option 5: Print all students in the list
    elif options == 5:
        print("The students in the list are: ")
        print(students)  # Calls the __str__ method of HWLinkedList to print all students

    # If user input is invalid
    else: 
        print("That is not a valid option. Please pick from the following prompts.")
