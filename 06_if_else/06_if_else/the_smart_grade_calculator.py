# 🔺 Level 3 — Full Integration
# "The Smart Grade Calculator"

# Taking user input
name = input("Enter student name: ")
subject_1 = float(input("Enter marks for Subject 1: "))
subject_2 = float(input("Enter marks for Subject 2: "))
subject_3 = float(input("Enter marks for Subject 3: "))

# Logic
average_marks = (subject_1 + subject_2 + subject_3) / 3
rounded_average_marks = round(average_marks,2)

# Option 1: Comparison Chaining (Cleanest)
# if not (0 <= subject_1 <= 100 and 0 <= subject_2 <= 100 and 0 <= subject_3 <= 100):
#    print("Invalid marks entered.")

# Option 2: Using a List (Scalable)
# marks = [subject_1, subject_2, subject_3]
# if any(m < 0 or m > 100 for m in marks):
#    print("Invalid marks entered.")

# Condition as per question
if subject_1 < 0 or subject_1 > 100 or subject_2 < 0 or subject_2 > 100 or subject_3 < 0 or subject_3 > 100: #if not (0 <= subject_1 <= 100 and 0 <= subject_2 <= 100 and 0 <= subject_3 <= 100):
    print("Invalid marks entered.")

else:
    if average_marks >= 90:
        grade = "A"
        remark = "Excellent!"
    elif average_marks >= 80:
        grade = "B"
        remark = "Good Performance"
    elif average_marks >= 70:
        grade = "C"
        remark = "Average Performance"
    elif average_marks >= 60:
        grade = "D"
        remark = "Needs Improvement"
    else:
        grade = "F"
        remark = "Please Work Harder"
    
    # Output

    print(f"===== Grade Report for {name} =====")
    print(f"Subject 1  : {subject_1}")
    print(f"Subject 2  : {subject_2}")
    print(f"Subject 3  : {subject_3}")
    print(f"Average    : {rounded_average_marks}")
    print(f"Grade      : {grade}")
    print(f"Remark     : {remark}")
    print("================================")
