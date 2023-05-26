from Q3_tester_code import *

def helper(buildings: list[Building]):
    n = len(buildings)
    i = 0
    j = n // 2

    # front side
    while (i < n // 2 and j < n):
        if (buildings[i].coordinates[0] < buildings[j].coordinates[0]):
            buildings[i].dominance = n - j
            i = i + 1
        elif (buildings[i].coordinates[0] > buildings[j].coordinates[0]):
            j = j + 1
    i = n - 1
    j = n // 2 - 1
    # back side
    while (i >= n // 2 and j >= 0):
        if (buildings[i].coordinates[0] < buildings[j].coordinates[0]):
            j = j - 1
        elif (buildings[i].coordinates[0] > buildings[j].coordinates[0]):
            buildings[i].dominance = j + 1
            i = i - 1

    return buildings

def my_solution(buildings: list[Building]) -> None:
    # reset building dominace to 0
    for building in buildings:
        if building.dominance is None:
            building.dominance = 0

    buildings.sort(key=lambda x: x.coordinates[1])
    mid_point = len(buildings) // 2
    left_building = buildings[:mid_point]
    right_building = buildings[mid_point:]

    left_building.sort(key=lambda x: x.coordinates[0])
    right_building.sort(key=lambda x: x.coordinates[0])
    buildings = left_building + right_building
    buildings = helper(buildings)
    return buildings

if __name__ == '__main__':
    # test(my_solution, map_size = 7)
    test_bulk(my_solution, number_of_random_tries = 5, map_size = 10)