def filter_cities_by_population(input_file='cities.txt', output_file='filtered_cities.txt'):
    try:
        # Чтение файла с городами
        with open(input_file, 'r') as file:
            cities = file.readlines()

        # Запрос у пользователя минимального значения количества жителей
        min_population = int(input("Введите минимальное количество жителей: "))

        # Создание списка городов с населением больше минимального
        filtered_cities = []
        for city in cities:
            name, population = city.split(':')
            if int(population.strip()) > min_population:
                filtered_cities.append(name.strip())

        # Сортировка списка городов в алфавитном порядке
        filtered_cities.sort()

        # Запись очищенного списка в выходной файл
        with open(output_file, 'w') as file:
            for city in filtered_cities:
                file.write(city + '\n')

        print(f"Фильтрованный список городов записан в файл {output_file}.")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
    except ValueError:
        print("Ошибка: неверный формат данных в файле или введено не числовое значение.")

filter_cities_by_population()