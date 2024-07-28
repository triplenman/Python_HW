import json


def sum_sales(input_file='input.txt', output_file='output.txt'):
    try:
        # Чтение файла с продажами
        with open(input_file, 'r') as file:
            sales_data = json.load(file)

        # Создание словаря для суммирования продаж
        total_sales = {}

        # Суммирование продаж каждого продукта по всем магазинам
        for store, products in sales_data.items():
            for product, amount in products.items():
                if product in total_sales:
                    total_sales[product] += amount
                else:
                    total_sales[product] = amount

        # Запись результатов в выходной файл
        with open(output_file, 'w') as file:
            for product, total in total_sales.items():
                file.write(f"{product}: {total}\n")

        print(f"Результаты суммирования продаж записаны в файл {output_file}.")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
    except json.JSONDecodeError:
        print("Ошибка: неверный формат данных в файле.")

sum_sales()
