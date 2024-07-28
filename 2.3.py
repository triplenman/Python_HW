def read_lines(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []

def main():
    lines1 = read_lines('input1.txt')
    lines2 = read_lines('input2.txt')

    if lines1 and lines2:
        all_lines = lines1 + lines2
        sorted_lines = sorted(all_lines)
        with open('output.txt', 'w') as file:
            for line in sorted_lines:
                file.write(f"{line}\n")
    else:
        print("Нет данных для обработки.")

if __name__ == "__main__":
    main()
