import json
from playsound import playsound

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Какой-то звук"

    def eat(self):
        return f"{self.name} принимает пищу"

# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        playsound('sound/popugai.wav')
        return str(self.name)+" орёт 'Попка-дурак'"

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        playsound('sound/lion.wav')
        return str(self.name)+" рычит: Р-р-р-р-р"

# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        playsound('sound/snake.wav')
        return str(self.name)+" шипит: Ш-ш-ш-ш-ш-ш"

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

    def save_to_file(self, filename):
        data = {
            "animals": [
                {
                    "type": type(animal).__name__,
                    "name": animal.name,
                    "age": animal.age,
                    # Сохраняем конкретное имя атрибута в зависимости от типа животного
                    "wing_span": animal.wing_span if isinstance(animal, Bird) else None,
                    "fur_color": animal.fur_color if isinstance(animal, Mammal) else None,
                    "scale_type": animal.scale_type if isinstance(animal, Reptile) else None
                }
                for animal in self.animals
            ],
            "staff": [
                {
                    "type": type(staff).__name__,
                    "name": staff.name,
                    "age": staff.age
                }
                for staff in self.staff
            ]
        }
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r', encoding="utf-8") as file:
            data = json.load(file)
        self.animals = []
        self.staff = []
        for animal_data in data["animals"]:
            # Обработка различных типов животных
            if animal_data["type"] == "Bird":
                animal = Bird(animal_data["name"], animal_data["age"], animal_data["wing_span"])
            elif animal_data["type"] == "Mammal":
                animal = Mammal(animal_data["name"], animal_data["age"], animal_data["fur_color"])
            elif animal_data["type"] == "Reptile":
                animal = Reptile(animal_data["name"], animal_data["age"], animal_data["scale_type"])
            else:
                print(f"Неизвестный тип животного: {animal_data['type']}")
                continue
            self.animals.append(animal)
        for staff_data in data["staff"]:
            if staff_data["type"] == "ZooKeeper":
                staff = ZooKeeper(staff_data["name"], staff_data["age"])
            elif staff_data["type"] == "Veterinarian":
                staff = Veterinarian(staff_data["name"], staff_data["age"])
            else:
                print(f"Неизвестный тип сотрудника: {staff_data['type']}")
                continue
            self.staff.append(staff)

# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed_animal(self, animal):
        if animal.name == 'Попугай':
            rod_animal = 'попугая'
        elif animal.name == 'Лев':
            rod_animal = 'льва'
        elif animal.name == 'Змея':
            rod_animal = 'змею'
        else:
            rod_animal = animal.name

        return f"{self.name} кормит {rod_animal}"

# Класс Veterinarian
class Veterinarian:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def heal_animal(self, animal):
        if animal.name == 'Попугай':
            rod_animal = 'попугая'
        elif animal.name == 'Лев':
            rod_animal = 'льва'
        elif animal.name == 'Змея':
            rod_animal = 'змею'
        else:
            rod_animal = animal.name
        return f"{self.name} лечит {rod_animal}"

# Пример использования
if __name__ == "__main__":
    # Создаем зоопарк
    zoo = Zoo()

    # Создаем животных
    bird = Bird("Попугай", 2, 30)
    mammal = Mammal("Лев", 5, "Golden")
    reptile = Reptile("Змея", 3, "Scaly")

    # Добавляем животных в зоопарк
    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    # Создаем сотрудников
    zookeeper1 = ZooKeeper("Иван Змеевский", 30)
    zookeeper2 = ZooKeeper("Сергей Коровин", 25)
    veterinarian1 = Veterinarian("Доктор Айболит", 45)
    veterinarian2 = Veterinarian("Ветеринар Маша Иванова", 26)

    # Добавляем сотрудников в зоопарк
    zoo.add_staff(zookeeper1)
    zoo.add_staff(zookeeper2)
    zoo.add_staff(veterinarian1)
    zoo.add_staff(veterinarian2)

    # Демонстрируем звуки животных
    animal_sound(zoo.animals)

    # Сохраняем информацию о зоопарке в файл
    zoo.save_to_file("zoo.txt")

    # Загружаем информацию о зоопарке из файла
    new_zoo = Zoo()
    new_zoo.load_from_file("zoo.txt")

    print("\nЗвуки животных после загрузки из файла:")
    animal_sound(new_zoo.animals)

    print("\nИнформация о сотрудниках:")
    for staff in new_zoo.staff:
        print(f"{staff.name}, возраст: {staff.age}")

    # Выводим информацию офункциях персонала (кто каких животных кормит, а кто их лечит)
    # кормежники
    print(zookeeper1.feed_animal(bird))
    print(zookeeper2.feed_animal(mammal))
    print(zookeeper2.feed_animal(reptile))

    # лечители
    print(veterinarian2.heal_animal(bird))
    print(veterinarian1.heal_animal(mammal))
    print(veterinarian1.heal_animal(reptile))