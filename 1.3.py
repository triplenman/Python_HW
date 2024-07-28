# Функция для подсчета суммы цифр числа
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Запрос числа
num = int(input("Введите число: "))

# Сложение цифр для получения результата < 10
while num >= 10:
    num = sum_of_digits(num)

print(num)
