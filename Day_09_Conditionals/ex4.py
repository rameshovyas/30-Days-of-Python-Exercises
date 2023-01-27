# Write a code which gives grade to students according to theirs scores
score = int(input("Enter your score : "))
if(score>=90):
    grade = 'A'
elif ((score>=70) and (score<90)):
    grade = 'B'
elif ((score>=60) and (score<70)):
    grade = 'C'
elif ((score>=50) and (score<60)):
    grade = 'D'
else:
    grade ='F'

print("Grade : ", grade)
