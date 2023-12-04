grades = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7
}

def gpa_cal(grades):
    total = 0
    total_no_credits = 0
    while True:
        grade,credit = input("Enter grade and credit separated by a space: ").split()
        if grade == "q":
            break
        if grade not in grades:
            print("Unknown grade '{0}' being ignored".format(grade))
            continue
        total += grades[grade]*int(credit)
        total_no_credits += int(credit)  
    if total_no_credits > 0:
        print("Your GPA is {0:.4}".format(total / total_no_credits))
    else:
        print("You didn't enter any grades")

gpa_cal(grades)