students_scores = {
    "Jalal": 95,
    "Jafar": 85,  
    "Usman" : 89,
    "Jaweria" : 90,
    "Muzammil" : 80, 
    "Rimsha" : 88, 
    "Faseeh" : 92,
    "Jesse" :96,
    "Iqbal" : 97
}

students_grades = {}

for key in students_scores:
    score = students_scores[key]
    if score >= 91 and score <= 100:
        students_grades[key] = "Outstanding"

    elif score >= 81 and score <= 90:
        students_grades[key] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        students_grades[key] = "Acceptable"
    else:
        students_grades[key] = "Fail"

print(students_grades)



