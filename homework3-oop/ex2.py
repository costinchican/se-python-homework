"""
    Create 3 classes:
        - Cat
        - Dog
        - Mouse

    All of these 3 classes must inherit from the Animal class.

    public attributes:
        - inherited from Animal (on init (or also called constructor))
        - enemy (on constructor (init))
            - is reference to the enemy of the current Animal
            e.g. Dog is the enemy of Cat

    private attributes:
        - specific_sound: str

    public methods:
        - inherited from Animal

    private methods:
        - enemy_fear_sound() - returns str
            - this is called inside the sound() method, and if an enemy has
            been passed on the constructor, then the sound should be different
            than the usual sound of the animal

            e.g.
                if Cat is called with enemy = Dog, then the cat should make
            a "meoooooow scared" sound.
                else the cat makes a "meow" sound
"""
from ex1 import Animal, AnimalEnum


class Dog(Animal):
    def __init__(self, color: str, age: int, enemy: AnimalEnum = None):
        super().__init__(color, age, animal_type=AnimalEnum.DOG)
        self.enemy = enemy
        self.__specific_sound = "bark"

    def __enemy_fear_sound(self):
        return "baaaark scared"

    def sound(self):
        if self.enemy == AnimalEnum.MOUSE:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age += 1


class Cat(Animal):
    def __init__(self, color: str, age: int, enemy: AnimalEnum = None):
        super().__init__(color, age, animal_type=AnimalEnum.CAT)
        self.enemy = enemy
        self.__specific_sound = "meow"

    def __enemy_fear_sound(self):
        return "meeeow scared"

    def sound(self):
        if self.enemy == AnimalEnum.DOG:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age += 1


class Mouse(Animal):
    def __init__(self, color: str, age: int, enemy: AnimalEnum = None):
        super().__init__(color, age, animal_type=AnimalEnum.MOUSE)
        self.enemy = enemy
        self.__specific_sound = "kitz"

    def __enemy_fear_sound(self):
        return "kiiitz scared"

    def sound(self):
        if self.enemy == AnimalEnum.CAT:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age += 1


if __name__ == "__main__":
    cat1 = Cat('white', 1)
    cat2 = Cat('brown', 4, AnimalEnum.DOG)
    cat3 = Cat('black', 10, AnimalEnum.MOUSE)

    print(cat1.sound())
    print(cat2.sound())
    print(cat3.sound())

    print(cat1.tell_age())
    cat1.age_up()
    print(cat1.tell_age())
