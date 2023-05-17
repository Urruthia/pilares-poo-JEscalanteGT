from animal import Animal


class Dog(Animal):
    def __init__(self, name: str, age: int, best_friend: str):
        super().__init__(name, age)
        self.best_friend = best_friend

    def bark(self):
        print(f'{self.name}: guau')

    def make_sound(self):
        self.bark()
