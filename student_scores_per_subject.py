num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))
scores = []

for i in range(num_students):
    print(f"Student {i + 1}:")
    student_scores = []
    for j in range(num_subjects):
        score = float(input(f"  Enter score {j + 1}: "))
        student_scores.append(score)
        scores.append(score) 
    average_score = sum(student_scores) / num_subjects
    print(f"Average score for Student {i + 1}: {average_score:.2f}")

class_average = sum(scores) / (num_students * num_subjects)
print(f"Class Average = {class_average:.2f}")
