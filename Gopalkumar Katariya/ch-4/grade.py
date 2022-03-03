marks = int(input("Enter your score : "))

if 90 <= marks <= 100:
    print("A grade")
elif 80 <= marks < 90:
    print("B grade")
elif 70 <= marks < 80:
    print("C grade")
elif 60 <= marks < 70:
    print("D grade")
elif 35 <= marks < 60:
    print("E grade")
elif marks < 35:
    print("You failed")
else:
    print("Enter valid marks")