import random
import time

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0

    def __str__(self):
        return f"Имя: {self.name}, голод: {self.hunger}, нудьга: {self.boredom}"

    def feed(self):
        print(f"{self.name} їсть...")
        self.hunger -= 1
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        print(f"{self.name} грає...")
        self.boredom -= 1
        if self.boredom < 0:
            self.boredom = 0

    def pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def mood(self):
        if self.hunger > 5:
            return "голодний"
        elif self.boredom > 5:
            return "нудьгує"
        else:
            return "в порядку"


def main():
    pet_name = input("Ім'я кота: ")
    cat = Cat(pet_name)

    while True:
        print("\nЩо хочете зробити?")
        print("1. Пгодувати")
        print("2. Пограти")
        print("3. Переглянути настрій кота")
        print("0. Вихід")

        choice = input("Виберіть дію: ")

        if choice == "1":
            cat.feed()
        elif choice == "2":
            cat.play()
        elif choice == "3":
            print(cat)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Не правільний вибір.")

        cat.pass_time()
        print(f"\nСтан кота: {cat.mood()}")

        # Задержка перед следующим ходом
        time.sleep(1)


if __name__ == "__main__":
    main()
