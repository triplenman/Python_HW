def count_ways(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_ways(n-1) + count_ways(n-2)

def main():
    try:
        n = int(input("Введите количество ступенек: "))
        print(f"Количество способов подняться на {n} ступенек: {count_ways(n)}")
    except ValueError:
        print("Введите корректное целое число")

if __name__ == "__main__":
    main()