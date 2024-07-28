def read_lines(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []

def process_lines(lines, chars_to_remove):
    processed_lines = []
    for line in lines:
        stripped_line = line.rstrip(chars_to_remove + ';')
        reversed_line = stripped_line[::-1]
        processed_lines.append(reversed_line)
    return processed_lines

def write_lines(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(f"{line}\n")

def main():
    lines = read_lines('input.txt')
    if lines:
        chars_to_remove = input("Введите символы для удаления с правого края строки: ")
        processed_lines = process_lines(lines, chars_to_remove)
        write_lines('output.txt', processed_lines)
    else:
        print("Нет данных для обработки.")

if __name__ == "__main__":
    main()