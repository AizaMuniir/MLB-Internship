student_name = input("Enter Student Name: ")
student_class = input("Enter Student Class: ")

print("Student Name: ", student_name)
print("Student Class: ", student_class)

subject = []
mark = []
grade = []

subject_num = int(input("Enter Total Number of Subjects: "))


for i in range(subject_num):
    sub_name = input("Enter Subject Name: ")
    sub_mark = int(input("Enter Marks : "))

    subject.append(sub_name)
    mark.append(sub_mark)

    if sub_mark >= 80:
        sub_grade = "A"
    elif sub_mark >= 70:
        sub_grade = "B"
    elif sub_mark >= 60:
        sub_grade = "C"
    else:
        sub_grade = "F"

    grade.append(sub_grade)

print("\nStudent Result:")

for i in range(subject_num):
  print("Subject:", subject[i], "Marks:", mark[i], "Grade:", grade[i])

average = sum(mark) / subject_num

if average >= 80:
    all_grade = "A"
elif average >= 70:
    all_grade = "B"
elif average >= 60:
    all_grade = "C"
else:
    all_grade = "F"

print("\nOverall Result: ")
print("Average Marks: ", average)
print("Overall Grade: ", all_grade)