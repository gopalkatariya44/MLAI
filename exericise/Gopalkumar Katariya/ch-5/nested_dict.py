stu_dist = {}

size = int(input("Enter the No. of Student : "))

for i in range(size):
    roll_no = input("Enter the Roll number of Student: ")
    stu_dist[roll_no] = {}
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    stu_dist[roll_no]["name"] = name
    stu_dist[roll_no]["branch"] = branch
    
print(stu_dist)