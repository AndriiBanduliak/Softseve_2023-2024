def gradeCalculator(grade):
    if grade < 0:
        print("Wrong number")
    elif grade >= 90 and grade <= 100:
        print("A")
    elif grade >= 80 and grade < 90:
        print("B")
    elif grade >= 70 and grade < 80:
        print("C")
    elif grade >= 60 and grade < 70:
        print("D")
    elif grade >= 0 and grade < 60:
        print("F")
    else:
        print("Invalid input: Grade should be between 0 and 100")

