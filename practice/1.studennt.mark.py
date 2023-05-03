#create list 
students =[]
courses =[]

#input infor of students
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student DOB: ")
    students.append((student_id, student_name, student_dob))

#input infor of courses
num_courses = int(input("Enter number of courses: "))  
for i in range(num_courses):
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    courses.append((course_id, course_name))

course_mark = {}
#get list
def list_students():
    for student in students:
        print(student[1])

def list_courses():
    for course in courses:
        print(course[1])

#get mark
def get_marks(course_id):
    for course in courses:
        if course[0] == course_id:
            course_name = course[1]
    if course_id in course_marks:
        for student_id, marks in course_marks[course_id].items():
            for student in students:
                if student[0] == student_id:
                    student_name = student[1]
            print(f"{student_name}: {marks}") 
    else:
        print(f"No marks entered for {course_name} yet!")
#Add marks
course_id = input("Enter course ID to add marks: ")
for student in students:
    student_id = student[0]
    marks = int(input(f"Enter marks for {student[1]} in {course_id}: "))
    if course_id in course_marks:
        course_marks[course_id][student_id] = marks
    else:
        course_marks[course_id] = {student_id: marks}
#Check all list
while True:
    choice = input("Enter 'l' to list courses, 's' to list students, 'm' to get marks for a course, 'q' to quit: ")
    if choice == 'l':
        list_courses()
    elif choice == 's':
        list_students()
    elif choice == 'm':
        get_marks(input("Enter course ID to get marks: "))
    elif choice == 'q':
        break