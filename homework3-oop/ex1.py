"""
    Create a class "Animal". You will use this class later to extend it
    with other types of animals.

    This should be an abstract class (no functionality, only works as an
    interface for the other classes). https://docs.python.org/3/library/abc.html

    public attributes:
        - color: str
        - age: int
        - animal_type: Enum (https://docs.python.org/3/library/enum.html)

    public methods:
        - sound() - returns str
            - should return the sound the animal makes
                e.g. Dog - "woof"
        - tell_age() - returns int
            - returns the current animal age
        - age_up() - returns nothing
            - should add 1 year to the current age
        - all_implemented() - returns bool
            - this method must have a functionality, if all the methods
            above have been implemented, then this should return True,
            otherwise it should return False.

    This is an abstract class! Pay attention, this class MUST NOT have any
    functionality in it (besides all_implemented()).
    The explanations for what the methods should do are mainly for the classes
    that will extend the Animal class.
"""


import abc
from enum import Enum


class AnimalEnum(Enum):
    DOG = 1
    CAT = 2
    MOUSE = 3


class Animal(abc.ABC):
    def __init__(self, color: str, age: int, animal_type: AnimalEnum):
        self.color = color
        self.age = age
        self.animal_type = animal_type

    @abc.abstractmethod
    def sound(self):
        pass

    @abc.abstractmethod
    def tell_age(self):
        pass

    @abc.abstractmethod
    def age_up(self):
        pass

    @classmethod
    def all_implemented(cls):
        if len(cls.__abstractmethods__):  # List of abstract methods
            print(cls.__abstractmethods__)
            return False
        else:
            return True
