
s_credit = 0
s_grade = 0

for i in range(20):
    name, credit, grade = input().split()

    if grade == "A+":
        grade = 4.5
    elif grade == "A0":
        grade = 4.0
    elif grade == "B+":
        grade = 3.5
    elif grade == "B0":
        grade = 3.0
    elif grade == "C+":
        grade = 2.5
    elif grade == "C0":
        grade = 2.0
    elif grade == "D+":
        grade = 1.5
    elif grade == "D0":
        grade = 1.0
    elif grade == "F":
        grade = 0.0
    else:
        continue

    credit = float(credit)
    s_credit += credit
    s_grade += credit * grade

print("%.6f" %(s_grade/s_credit))