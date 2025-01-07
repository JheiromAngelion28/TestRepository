# Function to get student data
def get_student_data():
    student_grades = {}
    while True:
        name = input("Enter student name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {name}: "))
            student_grades[name] = grade
        except ValueError:
            print("invalod grade, Please enter a number")
    return student_grades

def calculate_statistics(student_grades):
    if not student_grades:
        return None
    
    average_grade = sum(student_grades.values())/ len(student_grades)
    highest_grade = max(student_grades, key=student_grades.get)
    lowest_grade = min(student_grades, key=student_grades.get)

    return {
        'average':average_grade,
        'highest': highest_grade,
        'lowest': lowest_grade
    }

def display_results(student_grades, Statistics):
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")

    print("\n---Statistics---")
    print(f"Average Grade : {Statistics['average']:.2f}")
    print(f"Highest Grade : {Statistics['highest'][0]} ({Statistics['highest'][1]})")
    print(f"Lowest Grade : {Statistics['lowest'][0]} ({Statistics['lowest'][1]})")



if __name__ == "__main__":
    student_grades = get_student_data()
    statistics = calculate_statistics(student_grades)
    display_results(student_grades, statistics)



