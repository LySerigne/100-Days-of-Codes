# Returning the highest num in a list without using the max function

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

heighest_score = 0
for num in student_scores:
  if num > heighest_score:
    heighest_score = num
   
print(f"The greatest num is: {heighest_score}")



