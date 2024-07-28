def read_grades(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            students = [line.strip().split(',') for line in lines]
            return [(student[0], int(student[1])) for student in students]
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []

def calculate_average(grades):
    total = sum(grade for _, grade in grades)
    return total / len(grades) if grades else 0

def write_above_average_students(filename, students, average):
    with open(filename, 'w') as file:
        for student, grade in students:
            if grade > average:
                file.write(f"{student}\n")

def main():
    grades = read_grades('input.txt')
    if grades:
        average = calculate_average(grades)
        write_above_average_students('output.txt', grades, average)
        print(f"Средняя оценка: {average}")
    else:
        print("Нет данных для обработки.")

if __name__ == "__main__":
    main()
