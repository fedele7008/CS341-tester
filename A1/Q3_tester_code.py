import numpy as np
from typing import Callable

seed = 1234

class Building:

    rng = np.random.default_rng(seed)

    def __init__(self, x: int, y: int):
        self.coordinates = (x, y)
        self.dominance = None
    
    @staticmethod
    def create_random_buildings(
            numbuilding: int,
            max_x: int,
            max_y: int) -> list:
        buildings = []
        for _ in range(numbuilding):
            x = Building.rng.integers(max_x, endpoint=True)
            y = Building.rng.integers(max_y, endpoint=True)
            buildings.append(Building(x, y))
        return buildings
    
    @staticmethod
    def print_dominance(buildings: list) -> None:
        for building in buildings:
            print(f'{building.coordinates} : {building.dominance}')


def solution(buildings: list[Building]) -> None:
    # reset building dominace to 0
    for building in buildings:
        if building.dominance is None:
            building.dominance = 0

    for i in range(len(buildings)):
        for j in range(len(buildings)):
            # if indices are pointing at same buildings, continue
            if i == j:
                continue

            if (((buildings[i].coordinates[0] > buildings[j].coordinates[0])
                    and (buildings[i].coordinates[1] > buildings[j].coordinates[1]))
                    or ((buildings[i].coordinates[0] < buildings[j].coordinates[0])
                    and (buildings[i].coordinates[1] < buildings[j].coordinates[1]))):
                buildings[i].dominance += 1


def test(my_answer: Callable[[list[Building]], None]) -> None:
    buildings_solution = Building.create_random_buildings(7, 5, 5)
    buildings_my_solution = []
    for i in range(len(buildings_solution)):
        buildings_my_solution.append(Building(buildings_solution[i].coordinates[0], buildings_solution[i].coordinates[1]))
    solution(buildings_solution)
    my_answer(buildings_my_solution)
    
    print('Expected solution:')
    Building.print_dominance(buildings_solution)

    print('\nMy solution:')
    Building.print_dominance(buildings_my_solution)
