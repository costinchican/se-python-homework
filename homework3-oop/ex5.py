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

# WORK IN PROGRESS

cat4 = Cat('brown', 4, AnimalEnum.DOG)
w1 = World(10, 10)
entitate = WorldEntity(cat4, w1)
w1.init_world()
#w1.see_world()
w1.update_world(entitate)
w1.see_world()
print("MATRICE2")
entitate.move_down()
entitate.move_down()
entitate.move_right()
entitate.move_right()
entitate.move_up()
entitate.move_left()
w1.see_world()