def is_balanced(s):
    stack = []
    opening = {'(', '[', '{', '<'}
    closing = {')': '(', ']': '[', '}': '{', '>': '<'}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != closing[char]:
                return False
            stack.pop()

    return not stack


def main():
    try:
        with open('input.txt', 'r') as infile:
            lines = infile.readlines()

        results = []
        for line in lines:
            results.append(is_balanced(line.strip()))

        with open('output.txt', 'w') as outfile:
            for result in results:
                outfile.write(str(result).lower() + '\n')
    except FileNotFoundError:
        print("Файл не найден")


if __name__ == "__main__":
    main()