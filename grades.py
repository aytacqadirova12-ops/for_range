students = [("Aysel", 95), ("Murad", 72), ("Leyla", 84), ("Elvin", 48), ("Nigar", 63)]
for i in range(len(students)):
    name, grade = students[i]
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    print(f"{name}: {grade} → {letter_grade}")