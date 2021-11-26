"""
    Create a class WorldEntity.


    public attributes:
        - entity_type: instance of Animal or classes that extend Animal
            - this is on the constructor
            - use https://docs.python.org/3/library/typing.html to force
            the user to initialize this attribute with an Animal (or classes
            that extend Animal)
        - world: instance of World class
            - this is on the constructor
            - this should be the same for every entity
        - current_position: tuple(x, y)
            - this is NOT on the constructor
            - the current position is a tuple of 2 elements, representing
            the current position of the entity on the map
            - initially, the elements of the tuple are two integers between
            map_height and map_height which you have given to the world
            previously.
                - 0 < x < map_height
                - 0 < y < map_width
        - entity_id - int
            - this is NOT on the constructor
            - this is decided at init, when passed the animal type
                - DOG = 1
                - CAT = 2
                - MOUSE = 3

    public mehtods:
        - move_up - returns nothing
            - moves the entity up on the world map (modifies current_position)
            - updates the world
        - move_down - returns nothing
            - moves the entity down on the world map (modifies current_position)
            - updates the world
        - move_left - returns nothing
            - moves the entity left on the world map (modifies current_position)
            - updates the world
        - move_right - returns nothing
            - moves the entity right on the worl map (modifies current_position)
            - updates the world
"""
from ex1 import Animal, AnimalEnum
from ex2 import Dog, Cat, Mouse
import random


class WorldEntity:
    def __init__(self, entity_type: Animal, world):
        self.entity_type = entity_type
        self.world = world
        a = random.randrange(1, world.map_height)
        b = random.randrange(1, world.map_width)
        self.current_position = (a, b)
        self.entity_id = entity_type.animal_type.value

    def move_up(self):
        try:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
            self.world.world_map[self.current_position[0] + 1, self.current_position[1]] = 0
            self.world.update_world(self)
        except:
            print("Map Limit Reached. Try a different move.")

    def move_down(self):
        try:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
            self.world.world_map[self.current_position[0] - 1, self.current_position[1]] = 0
            self.world.update_world(self)
        except:
            print("Map Limit Reached. Try a different move.")

    def move_left(self):
        try:
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
            self.world.world_map[self.current_position[0], self.current_position[1] + 1] = 0
            self.world.update_world(self)
        except:
            print("Map Limit Reached. Try a different move.")

    def move_right(self):
        try:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
            self.world.world_map[self.current_position[0], self.current_position[1] - 1] = 0
            self.world.update_world(self)
        except:
            print("Map Limit Reached. Try a different move.")
