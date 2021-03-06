# created dictionaries that hold values for different types of assignments.
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [101.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Functions used to find the grade average for each student.
def average(numbers):
    total = sum(numbers)
    total = float(total) / len(numbers)
    return total
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    grade1 = homework * .10
    grade2 = quizzes * .30
    grade3 = tests * .60
    
    return grade1 + grade2 + grade3
# Function used to determine the letter grade in the course.   
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else: 
        return "F"
print get_letter_grade(lloyd)
# Function used to determine the average class grade and average class letter grade.
students = [lloyd, alice, tyler]
def get_class_average(students):
    results = []
    for student in students:
        avg = get_average(student)
        results.append(avg)
    return average(results)
print get_class_average(students)
print get_letter_grade(get_class_average(students))
