student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")


lowest_score=student_scores[0]
for score in student_scores:
  if score < lowest_score:
    lowest_score = score
print(f"The lowest score in the class is: {lowest_score}")

# maximum=0
# for number in student_scores:
#     if student_scores[n] > student_scores[n+1]:
#         maximum=number
# print(maximum)

# for number in range(0, len(student_scores)):
#     number=student_scores[n]
#     print(number)
#     for maximum in student_scores:
#         if number>student_scores[n+1] :
#             print(number)

# a=0
# for n in range(0,len(student_scores)):
#     for i in range(n+1, len(student_scores)):
#         if student_scores[n]>student_scores[i]:
#             a=student_scores[n]
#             student_scores[n]=student_scores[i]
#             student_scores[i]=a
# print(a)
