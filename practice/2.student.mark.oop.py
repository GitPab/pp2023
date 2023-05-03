#get course
class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        return self.course_name
#get student
class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob

    def __str__(self):
        return self.student_name
#get mark
class Mark:
    def __init__(self, course, student, mark):
        self.course = course
        self.student = student
        self.mark = mark
#Add infor
class StudentMarks:
    def __init__(self):
        self.courses = [] 
        self.students = []
        self.marks = []

    def add_course(self, course_id, course_name):
        course = Course(course_id, course_name)
        self.courses.append(course)

    def add_student(self, student_id, student_name, student_dob):
        student = Student(student_id, student_name, student_dob)
        self.students.append(student)

    def add_mark(self, course_id, student_id, mark):
        course = None
        for c in self.courses:
            if c.course_id == course_id:
                course = c
                break
                
        student = None
        for s in self.students:
            if s.student_id == student_id:
                student = s
                break  
                
        if course and student:
            mark = Mark(course, student, mark)
            self.marks.append(mark)          

    def list_courses(self):
        for course in self.courses:
            print(course)        

    def list_students(self):
        for student in self.students:
            print(student)  

    def get_marks(self, course_id):
        for mark in self.marks:
            if mark.course.course_id == course_id:
                print(f"{mark.student}: {mark.mark}")   
#main
if __name__ == "__main__": 
    sms = StudentMarks()
    num_courses = int(input("Enter number of courses: "))  
    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        sms.add_course(course_id, course_name)
        
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student DOB: ")
        sms.add_student(student_id, student_name, student_dob)
 #check       
    while True:
        choice = input("Enter 'l' to list courses, 's' to list students, 'm' to get marks for a course, 'q' to quit: ")
        if choice == 'l':
            sms.list_courses() 
        elif choice == 's':
            sms.list_students()
        elif choice == 'm':
            course_id = input("Enter course ID to get marks: ")
            sms.get_marks(course_id)
        elif choice == 'q':
            break