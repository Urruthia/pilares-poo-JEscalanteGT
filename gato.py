from animal import Animal


class Cat(Animal):
    def __init__(self, name: str, age: int, is_friendly: bool):
        super().__init__(name, age)
        self.is_friendly = is_friendly

    def meow(self):
        print(f'{self.name}: meow')

    def make_sound(self):
        self.meow()
