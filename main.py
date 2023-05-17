"""
from city import City

city1 = City(
    'Quetzaltenango',
    14.840553,
    -91.5179788
)
"""
from perro import Dog
from gato import Cat
from animal import Animal
cat1 = Cat('misho', 2, True)
cat2 = Cat('mish', 3, False)
cat3 = Cat('mishi', 4, True)
dog1 = Dog('chucho', 3, 'Do comedia')
dog2 = Dog('chucho1', 4, 'alguien')
dog3 = Dog('chucho2', 5, 'alguien2')

animals: list[Animal]=[cat1, cat2, cat3, dog1,dog2, dog3]
