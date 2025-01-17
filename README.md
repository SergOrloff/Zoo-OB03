# Зоопарк: Пример использования классов и полиморфизма

## Описание проекта

Данный проект представляет собой симуляцию зоопарка с использованием объектно-ориентированного программирования (ООП) на языке Python. В проекте реализованы базовые классы для животных и сотрудников зоопарка, а также функции для сохранения и загрузки данных о зоопарке в файлы.

## Структура проекта

Проект состоит из следующих основных компонентов:
1. **Классы для животных**:
    - `Animal`: базовый класс для всех животных.
    - `Bird`: подкласс, представляющий птиц.
    - `Mammal`: подкласс, представляющий млекопитающих.
    - `Reptile`: подкласс, представляющий рептилий.

2. **Классы для сотрудников зоопарка**:
    - `ZooKeeper`: класс, представляющий смотрителя зоопарка.
    - `Veterinarian`: класс, представляющий ветеринара.

3. **Класс Zoo**: основной класс, представляющий зоопарк и содержащий методы для добавления животных и сотрудников, а также для сохранения и загрузки данных.

4. **Функция для демонстрации полиморфизма**: функция `animal_sound`, которая принимает список животных и вызывает для каждого из них метод `make_sound`.

## Установка

Для работы программы необходима установка следующих библиотек:
- `playsound` для воспроизведения звуков.

Для установки библиотеки `playsound` выполните следующую команду:
```sh
pip install playsound
```

## Запуск программы

1. Создайте файл `zoo.py` и вставьте в него следующий код:

```python
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
        return str(self.name) + " орёт 'Попка-дурак'"

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        playsound('sound/lion.wav')
        return str(self.name) + " рычит: Р-р-р-р-р"

# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        playsound('sound/snake.wav')
        return str(self.name) + " шипит: Ш-ш-ш-ш-ш-ш"

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
        return f"{self.name} кормит {animal.name}"

# Класс Veterinarian
class Veterinarian:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}"

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

    print(zookeeper1.feed_animal(bird))
    print(zookeeper2.feed_animal(mammal))
    print(zookeeper2.feed_animal(reptile))
```

2. Убедитесь, что в папке проекта есть папка `sound` с нужными звуковыми файлами:
    ```
    sound/
        popugai.wav
        lion.wav
        snake.wav
    ```

3. Запустите программу:
    ```sh
    python zoo.py
    ```

## Функциональные возможности

- **Создание и добавление животных в зоопарк**: Поддерживаются птицы, млекопитающие и рептилии.
- **Создание и добавление сотрудников в зоопарк**: Поддерживаются смотрители зоопарка и ветеринары.
- **Воспроизведение звуков животных**: Используется библиотека `playsound`.
- **Сохранение и загрузка данных о зоопарке в файл**: Данные сохраняются в формате JSON.
- **Полиморфизм**: Вызов методов `make_sound` для различных типов животных.

## Контакты

Для вопросов и предложений вы можете связаться с автором проекта по электронной почте: [6202818@gmail.com](mailto:6202818@gmail.com).

## Лицензия

Этот проект лицензирован под MIT License. Подробности см. в файле `LICENSE`.
