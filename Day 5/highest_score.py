student_score = [150, 142, 185, 12, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
        
print(f'Highest score is {highest_score}')