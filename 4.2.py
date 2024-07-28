def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        print(f"Наибольший общий делитель: {gcd(a, b)}")
    except ValueError:
        print("Введите корректные целые числа")

if __name__ == "__main__":
    main()