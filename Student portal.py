data = []
my_dict = {}
Roll_number = []
Name = []
Courses = []
Marks = []


def add_student():
    try:
        student_name = input("Please enter the student name: ").title()
        if student_name.isalpha():
            student_id = int(input("Please enter the student id: "))
            data.append(student_name)
            data.append(student_id)
            Roll_number.append(student_id)
            Name.append(student_name)
            print("Data enter successfully")
        else:
            print("Only alphabet are allowed")
    except ValueError as e:
        print("Value error are occurred")


def add_marks_of_student():
    if data:
        print("All data")
        try:
            roll_number = int(input('Enter the roll number: '))
            if data[1] == roll_number:
                n = int(input("Enter the number of courses: "))
                if n == 1:
                    for i in range(n):
                        key = input("Enter course: ").title()
                        if key.isalpha():
                            value = int(input("Enter marks: "))
                            Marks.append(value)
                            Courses.append(key)
                            my_dict.update({key: value})
                        else:
                            print("Only alphabet are allowed")
                else:
                    for i in range(n):
                        key = input("Enter course no {}: ".format(i+1)).title()
                        if key.isalpha():
                            value = int(input("Enter marks {}: ".format(i+1)))
                            Marks.append(value)
                            Courses.append(key)
                            my_dict.update({key: value})
                        else:
                            print("Only alphabet are allowed")
                for s in my_dict:
                    print(f"Course is {s} and this marks is {my_dict[s]}")
            else:
                print(f"{roll_number} roll number not exist")
        except ValueError as e:
            print("Value error are occurred")
        except KeyError as e:
            print("Key error are occurred")
    else:
        print("No data found")


def student_pre_requires():
    if data:
        new_dict = {
            'Python': 'Django',
            'ICT': 'PF',
            'Web': 'Web3.0',
            'Networking': 'Crypto'
        }
        for i in my_dict:
            try:
                target = input("Enter target course: ").title()
                if target.isalpha():
                    if my_dict[target] < 50:
                        print(f"You are not eligible for {new_dict[target]}")
                    else:
                        print(f"You are eligible for {new_dict[target]}")
                else:
                    print("Only alphabet are allowed")
            except ValueError as e:
                print("Value error are occurred")
            except KeyError as e:
                print("Key error are occurred")
    else:
        print("No data found")


def class_result():
    if data:
        for i in Roll_number:
            print("All roll numbers is", i, end="| ")
        for m in Name:
            print("All name is", m, end="| ")
        for k in Courses:
            print("All courses is", k, end="|")
        for o in Marks:
            print("All marks is", o, end="")
    else:
        print("No data found")


def Total_class_performance():
    if data:
        sum = 0
        for i in Marks:
            sum += i
        x = len(Marks)
        y = x * 100
        p = int(sum) / int(y)
        performance = p * 100
        if performance < 50:
            print(f"Total class performance is Fail and total class percentage is {performance}.")
        elif performance <= 75:
            print(f"Total class performance is Pass and total class percentage is {performance}.")
        else:
            print(f"Total class performance is extraordinary and total percentage is {performance}.")
    else:
        print("No data found")


def main():
    while True:
        choice = """
        1): Add the student
        2): Add marks of student
        3): Student pre requires
        4): Class result
        5): Total class performance
        6): Exit program
        """
        print(choice)
        try:
            choice = int(input("Please enter the choice: "))
            if choice == 1:
                add_student()
            elif choice == 2:
                add_marks_of_student()
            elif choice == 3:
                student_pre_requires()
            elif choice == 4:
                class_result()
            elif choice == 5:
                Total_class_performance()
            elif choice == 6:
                print("Exit")
                break
            else:
                print("Invalid choice")
        except ValueError as e:
            print("Value error are occurred")


main()