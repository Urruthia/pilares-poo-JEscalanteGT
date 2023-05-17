class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def breathe(self):
        print(f'{self.name} estoy respirando')

    def make_sound(self):
        raise NotImplementedError