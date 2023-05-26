# import numpy as np
import random
from typing import Callable

seed = 1234

class Building:

    # rng = np.random.default_rng(seed)
    cid = 0

    def __init__(self, x: int, y: int, _id = None):
        self.coordinates = (x, y)
        self.dominance = None
        if _id is None:
            self.id = Building.cid
        else:
            self.id = _id
        Building.cid += 1
    
    @staticmethod
    def create_random_buildings(numbuilding: int) -> list:

        buildings = []
        coordinates = []
        used_x = set()
        used_y = set()

        while len(coordinates) < numbuilding:
            x = random.randint(1, numbuilding)
            y = random.randint(1, numbuilding)

            if x not in used_x and y not in used_y:
                coordinates.append((x, y))
                used_x.add(x)
                used_y.add(y)
        
        for i in range(numbuilding):
            buildings.append(Building(coordinates[i][0], coordinates[i][1]))

        return buildings

        # buildings = []
        # buildings.append(Building(1,5))
        # buildings.append(Building(2,2))
        # buildings.append(Building(3,3))
        # buildings.append(Building(4,1))
        # buildings.append(Building(6,4))
        # return buildings
    
    @staticmethod
    def print_dominance(buildings: list) -> None:
        buildings.sort(key=lambda x: x.id)
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


def test(my_answer: Callable[[list[Building]], None], map_size = 7) -> None:
    buildings_solution = Building.create_random_buildings(map_size)
    buildings_my_solution = []
    for i in range(len(buildings_solution)):
        buildings_my_solution.append(Building(buildings_solution[i].coordinates[0], buildings_solution[i].coordinates[1], buildings_solution[i].id))
    solution(buildings_solution)
    my_answer(buildings_my_solution)

    buildings_solution.sort(key=lambda x: x.id)
    buildings_my_solution.sort(key=lambda x: x.id)
    
    print('Expected solution:')
    Building.print_dominance(buildings_solution)

    print('\nMy solution:')
    Building.print_dominance(buildings_my_solution)

def test_bulk(my_answer: Callable[[list[Building]], None], number_of_random_tries: int, map_size = 100) -> None:
    total_fail = 0
    for trial in range(number_of_random_tries):
        print('-------------------------------------------------------------------------------')
        f_count = 0
        total_count = 0
        print(f'TRIAL: {trial + 1} (Randomly generated map size: {map_size})')
        buildings_solution = Building.create_random_buildings(map_size)
        buildings_my_solution = []
        for i in range(len(buildings_solution)):
            buildings_my_solution.append(Building(buildings_solution[i].coordinates[0], buildings_solution[i].coordinates[1], buildings_solution[i].id))
        solution(buildings_solution)
        my_answer(buildings_my_solution)

        buildings_solution.sort(key=lambda x: x.id)
        buildings_my_solution.sort(key=lambda x: x.id)

        for i in range(len(buildings_solution)):
            total_count += 1
            if (buildings_my_solution[i].dominance != buildings_solution[i].dominance):
                f_count += 1
                print(f'FAILED: ({buildings_solution[i].coordinates[0]}, {buildings_solution[i].coordinates[1]}) : {buildings_my_solution[i].dominance} (expected {buildings_solution[i].dominance})')
            else:
                print(f'PASSED: ({buildings_solution[i].coordinates[0]}, {buildings_solution[i].coordinates[1]}) : {buildings_my_solution[i].dominance}')
        
        print(f'CASE SUMMARY: {f_count} / {total_count} ({f_count * 100 / total_count} % PASSED) - CASE {"FAILED" if f_count > 0 else "PASSED"}')
        if f_count > 0:
            total_fail += 1

    print('===============================================================================')
    print(f'TEST SUMMARY: {number_of_random_tries - total_fail} / {number_of_random_tries} ({total_fail * 100 / number_of_random_tries} % CASE FAILED)')