def calculate_cgpa(credit_hours, grades):
    total_credit_hours = sum(credit_hours)
    total_grade_points = 0

    for i in range(len(grades)):
        grade = grades[i]
        credit_hour = credit_hours[i]

        if grade == 'A':
            grade_point = 4.0
        elif grade == 'A-':
            grade_point = 3.7
        elif grade == 'B+':
            grade_point = 3.3
        elif grade == 'B':
            grade_point = 3.0
        # Add more grade conversions here

        total_grade_points += grade_point * credit_hour

    cgpa = total_grade_points / total_credit_hours
    return cgpa


sub = int(input("enter the number of subject:"))
#name = (input("enter the subject:"))
#credit_hours = (int(input("enter the credit_hours:")))
#grades = (input("enter the grades:"))
for sub in range(sub):
    print((input("enter the subject:")))
    print((int(input("enter the credit_hours:"))))
    print((input("enter the grades:")))

credit_hours = [3, 4, 3]
grades = ['A', 'B+', 'A-']
result_cgpa = calculate_cgpa(credit_hours, grades)
print("Your CGPA is:", result_cgpa)
