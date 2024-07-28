import random

class Animal:
    def __init__(self, name, size, food_type, habitat, lifespan):
        self.name = name
        self.size = size
        self.food_type = food_type
        self.habitat = habitat
        self.lifespan = lifespan
        self.age = 0
        self.satiety = 100
        self.gender = random.choice(["male", "female"])

    def __repr__(self):
        return f"{self.name} ({self.gender}), Age: {self.age}, Satiety: {self.satiety}%"


def add_animal(animals, name, size, food_type, habitat, lifespan):
    animals.append(Animal(name, size, food_type, habitat, lifespan))


def increase_plant_food(plant_food, amount):
    return plant_food + amount


def display_animal_info(animals):
    for animal in animals:
        print(animal)


def reproduce(animals, animal1, animal2):
    if animal1.food_type != animal2.food_type:
        return
    if animal1.gender == animal2.gender:
        return
    if animal1.habitat != animal2.habitat:
        return

    if animal1.habitat == "water" and animal1.satiety > 50 and animal2.satiety > 50:
        for _ in range(10):
            animals.append(Animal(animal1.name, animal1.size, animal1.food_type, animal1.habitat, animal1.lifespan))
    elif animal1.habitat == "air" and animal1.satiety > 42 and animal1.age > 3 and animal2.age > 3:
        for _ in range(4):
            animals.append(Animal(animal1.name, animal1.size, animal1.food_type, animal1.habitat, animal1.lifespan))
    elif animal1.habitat == "land" and animal1.satiety > 20 and animal1.age > 5 and animal2.age > 5:
        for _ in range(2):
            animals.append(Animal(animal1.name, animal1.size, animal1.food_type, animal1.habitat, animal1.lifespan))


def advance_time(animals, plant_food):
    for animal in animals:
        animal.age += 1
        if animal.age >= animal.lifespan:
            plant_food += animal.size
            animals.remove(animal)
        elif animal.food_type == "plants":
            if plant_food > 0:
                plant_food -= 1
                animal.satiety += 26
            else:
                animal.satiety -= 9
        else:
            if random.random() > 0.5:
                animal.satiety += 53
            else:
                animal.satiety -= 16

        if animal.satiety < 10:
            plant_food += animal.size
            animals.remove(animal)

    return plant_food


def main():
    animals = [
        Animal("Fish", 1, "plants", "water", 5),
        Animal("Eagle", 3, "animals", "air", 10),
        Animal("Tiger", 7, "animals", "land", 15)
    ]

    plant_food = 50

    while True:
        print("1. Add Animal")
        print("2. Increase Plant Food")
        print("3. Display Animal Info")
        print("4. Reproduce Animals")
        print("5. Advance Time")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            size = int(input("Enter size: "))
            food_type = input("Enter food type (plants/animals): ")
            habitat = input("Enter habitat (water/air/land): ")
            lifespan = int(input("Enter lifespan: "))
            add_animal(animals, name, size, food_type, habitat, lifespan)
        elif choice == "2":
            amount = int(input("Enter amount of plant food to add: "))
            plant_food = increase_plant_food(plant_food, amount)
        elif choice == "3":
            display_animal_info(animals)
        elif choice == "4":
            name1 = input("Enter the name of the first animal: ")
            name2 = input("Enter the name of the second animal: ")
            animal1 = None
            animal2 = None
            for animal in animals:
                if animal.name == name1:
                    animal1 = animal
                if animal.name == name2:
                    animal2 = animal
            if animal1 and animal2:
                reproduce(animals, animal1, animal2)
        elif choice == "5":
            plant_food = advance_time(animals, plant_food)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()