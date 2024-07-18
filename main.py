
# Шаг 1: Создаем абстрактный класс для оружия
# Создадим абстрактный класс `Weapon` с абстрактным методом `attack()`.

from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуем конкретные типы оружия
# Создадим несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`.

# Класс для оружия "Меч"
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

# Класс для оружия "Лук"
class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Шаг 3: Модифицируем класс Fighter
# Добавим в класс `Fighter` поле для хранения объекта класса `Weapon` и метод для смены оружия.

# Класс для бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    # Метод для смены оружия
    def changeWeapon(self, weapon):
        self.weapon = weapon

    # Метод атаки
    def attack(self):
        if self.weapon is not None:
            return self.weapon.attack()
        else:
            return "Боец безоружен."

# Шаг 4: Реализация боя
# Создаем класс `Monster` и реализуем механизм боя.

# Класс для монстра
class Monster:
    def __init__(self, name):
        self.name = name

    # Метод для получения урона
    def take_damage(self, damage):
        return f"Монстр {self.name} получает урон: {damage}"

# Реализация боя
def battle(fighter, monster):
    print(fighter.attack())
    print(monster.take_damage(fighter.attack()))

# Демонстрация работы программы
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Боец выбирает меч
    sword = Sword()
    fighter.changeWeapon(sword)
    print("Боец выбирает меч.")
    battle(fighter, monster)

    # Боец выбирает лук
    bow = Bow()
    fighter.changeWeapon(bow)
    print("Боец выбирает лук.")
    battle(fighter, monster)

### Результат

# При выполнении программы вы получите следующий вывод в консоли:
#
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр Монстр получает урон: Боец наносит удар мечом.
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр Монстр получает урон: Боец наносит удар из лука.
# ```
#
# Объяснение
# 1. **Абстрактный класс Weapon**: Определяет интерфейс для всех типов оружия.
# 2. **Конкретные классы Sword и Bow**: Реализуют метод `attack()` своим уникальным способом.
# 3. **Класс Fighter**: Представляет бойца, который может менять оружие и атаковать.
# 4. **Класс Monster**: Представляет монстра, который может получать урон.
# 5. **Функция battle**: Демонстрирует бой между бойцом и монстром, используя выбранное оружие.

