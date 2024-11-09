'''
Write a program that converts their scores to grades.

The scoring criteria: 
- Scores 91 - 100: Grade = "Outstanding" 
- Scores 81 - 90: Grade = "Exceeds Expectations" 
- Scores 71 - 80: Grade = "Acceptable" 
- Scores 70 or lower: Grade = "Fail" 
'''

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] < 71:
        student_grades[key] = "Fail"

print(student_grades)