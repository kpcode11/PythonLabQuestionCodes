marks = []
sub = int(input("Enter the number of subjects: "))
for i in range(sub):
    mark = int(input(f"Enter the marks of subject {i+1}: "))
    marks.append(mark)

average = sum(marks) / sub

if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 70:
    print("Grade C")
elif average >= 60:
    print("Grade D")
elif average >= 50:
    print("Grade E")
else:
    print("Grade F")

print(f"Average marks: {average}")
print(f"Grade:")
