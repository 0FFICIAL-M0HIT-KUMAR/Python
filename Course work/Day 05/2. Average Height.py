student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
#Instead of this 👉 total_height = sum(student_heights) we are using below code
total_height = 0
for height in student_heights:
    total_height = total_height + height
# print(total_height)

# total_students = len(student_heights)
total_students = 0
for students in student_heights:
    total_students = total_students + 1
# print(total_students)

average = total_height/total_students
print(round(average))
