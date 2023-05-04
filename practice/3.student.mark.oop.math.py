import curses
import math 
import numpy as np


class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.scores = []
        self.credits = []
#calculate gpa        
    def calculate_gpa(self):
        scores = np.array(self.scores)
        credits = np.array(self.credits)
        weighted_sum = np.sum(scores * credits)
        total_credits = np.sum(credits)
        return weighted_sum / total_credits
        
    def add_score(self, course, score):
        self.scores.append(math.floor(score*10)/10)
        self.credits.append(course.credits)
#add list
class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        
    def add_student(self, id, name, dob):
        self.students.append(Student(id, name, dob))
        
    def add_course(self, id, name, credits):
        self.courses.append(Course(id, name, credits))
        
    def list_courses(self):
        for course in self.courses:
            print(f'{course.id}: {course.name} - {course.credits} credits')
    
    def list_students(self):
        for student in self.students:
            print(f'{student.id}: {student.name} - {student.dob}')  
            
    def get_course(self, id):
        for course in self.courses:
            if course.id == id:
                return course
        
    def add_score(self, student_id, course_id, score):
        student = None
        for s in self.students:
            if s.id == student_id:
                student = s
        if student is None:
            print('Student not found')
            return 
        course = self.get_course(course_id)
        if course is None:
            print('Course not found')
            return
        student.add_score(course, score) 
        
    def calculate_gpas(self):
        for student in self.students:
            student.gpa = student.calculate_gpa()
#sort        
    def sort_by_gpa(self): 
        self.students.sort(key=lambda s: s.gpa, reverse=True)