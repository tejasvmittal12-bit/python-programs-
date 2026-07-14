classmates = ["Aarav" , "Priya" , "Rahul" , "Sneha" , "Dev"]
print("Class List:", classmates)

print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First Three :", classmates[:3])

classmates.append("Meera")
print("\nAfter adding Meera:", classmates)
classmates.remove("Dev")
print("After removing Dev:", classmates)
classmates.sort()
print("Sorted Alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)
teacher = {"Name": "Mr.Sharma", "Subject": "Python", "Experience": "5"}
print("\nTeacher Profile:", teacher)

print("Subject:", teacher["Subject"])
print("Experience:", teacher.get("Experience", "Not found"))
teacher["Experience"] = "6"
teacher["Email"] = "sharma@school.com"
teacher.pop("Experience")
print("Updated Teacher Profile:", teacher)

roll_numbers = (1, 2, 3, 4, 5)
names = ("Aarav", "Priya", "Rahul", "Sneha", "Meera")
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("Student with Roll  3:", student_directory[3])
