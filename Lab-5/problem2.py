# Exercise 2: Student Marks Investigator

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

def calculate_average(marks):
    if not marks:
        return 0.0
    # Validate marks between 0 and 100
    valid_marks = [m for m in marks if 0 <= m <= 100]
    if len(valid_marks) != len(marks):
        print("Warning: Contains invalid mark(s) out of 0-100 range.")
    return sum(valid_marks) / len(valid_marks)

def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

def display_report(student_list):
    print(f"\n{'ID':<6} {'Name':<10} {'Average':<10} {'Performance':<18}")
    print("-" * 46)
    for student in student_list:
        s_id, name, marks = student
        avg = calculate_average(marks)
        perf = classify_performance(avg)
        print(f"{s_id:<6} {name:<10} {avg:<10.2f} {perf:<18}")

# Test run
if __name__ == "__main__":
    display_report(students)