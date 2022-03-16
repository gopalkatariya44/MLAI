# StudentInfo
#     student_rollno
#     student_name

class StudentInfo:
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
# StudentMarks
#     student_rollno
#     student_marks_one
#     student_marks_two
#     student_marks_three
class StudentMarks:
    def __init__(self,student_info_obj,marks_one,marks_two,marks_three):
        self.student_info_obj = student_info_obj
        self.marks_one = marks_one
        self.marks_two = marks_two
        self.marks_three = marks_three

    def average(self):
        return self.marks_one + self.marks_two + self.marks_three // 3
    
    def grade(self):
        return "pass"

# Main Class
#     Constructor
#     user will input no of students
#     user will input data for StudentInfo-Constructor
#     user will input data for StudentMarks-Constructor
#     calculate the average & grade-Function
#     90 to 100->A grade
# 	  80 to 90->B grade
# 	  60 to 80->C grade
# 	  40 to 60->D grade
# 	  < 40     ->Fail
# 	  >100 	->Invalid Marks

class Main:
    def __init__(self):
        student_list = []
        student_dict = {}
        self.stu_no = int(input("Enter no of student = "))
        student_info_obj = StudentInfo()
        for i in range(self.stu_no):
            student_marks_obj = StudentMarks(student_info_obj,)

