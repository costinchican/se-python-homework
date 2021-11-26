"""
    Initialize a World. Size of the world is
        - width = 10
        - height = 10

    Populate the world with 10 entities.
        - the entities must be generated randomly
        - update the world map

    Each entity should make 5 random moves.
        - iterate through the entities generated
        - pick a move between the 4 available (move_up, move_down, move_right,
        move_left) and execute it, then do it 4 more times.
        - every time, you must update the world map

    Print the World.
        - The world has 100 entries (10 x 10)
        - 90 of them should be 0
        - 10 of them should be numbers between 1 and 3 (Dog, Cat, Mouse)
"""
from ex1 import Animal, AnimalEnum
from ex2 import Cat, Dog, Mouse
from ex3 import World
from ex4 import WorldEntity
import random


colours = ['brown', 'white', 'black', 'gray']
age = range(15)
animale = [Cat(random.choice(colours), random.choice(age), AnimalEnum.CAT),
           Dog(random.choice(colours), random.choice(age), AnimalEnum.DOG),
           Mouse(random.choice(colours), random.choice(age), AnimalEnum.MOUSE)]

entities = []

w1 = World(10, 10)
w1.init_world()

for i in range(10):
    entity = WorldEntity(random.choice(animale), w1)
    entities.append(entity)
    w1.update_world(entity)

for entity in entities:
    moves = [entity.move_up, entity.move_down, entity.move_left, entity.move_right]
    m = random.choice(moves)
    for i in range(5):
        m()

w1.see_world()
