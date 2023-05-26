from Q3_tester_code import *
import copy

def mergesort_and_count_upper_right(buildings: list[Building]) -> list[Building]:
    if len(buildings) == 1:
        buildings[0].dominance = 0
        return buildings
    else:
        mid = len(buildings) // 2
        left = mergesort_and_count_upper_right(buildings[:mid])
        right = mergesort_and_count_upper_right(buildings[mid:])

        left_index = 0
        right_index = 0
        merged_index = 0
        pivot_index = -1

        result_buildings = copy.deepcopy(buildings)

        while left_index < len(left) and right_index < len(right):
            if left[left_index].coordinates[1] < right[right_index].coordinates[1]:
                result_buildings[merged_index] = left[left_index]
                left_index += 1
                pivot_index = merged_index
            else:
                result_buildings[merged_index] = right[right_index]
                if pivot_index > -1:
                    if result_buildings[pivot_index].coordinates[0] < result_buildings[merged_index].coordinates[0]:
                        result_buildings[pivot_index].dominance += 1
                right_index += 1
            merged_index += 1

        while left_index < len(left):
            result_buildings[merged_index] = left[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right):
            result_buildings[merged_index] = right[right_index]
            if pivot_index > -1:
                if result_buildings[pivot_index].coordinates[0] < result_buildings[merged_index].coordinates[0]:
                    result_buildings[pivot_index].dominance += 1
            right_index += 1
            merged_index += 1

        return result_buildings

def mergesort_and_count_lower_left(buildings: list[Building]) -> list[Building]:
    if len(buildings) == 1:
        buildings[0].dominance = 0
        return buildings
    else:
        mid = len(buildings) // 2
        left = mergesort_and_count_lower_left(buildings[:mid])
        right = mergesort_and_count_lower_left(buildings[mid:])

        left_index = 0
        right_index = 0
        merged_index = 0
        pivot_index = -1

        result_buildings = copy.deepcopy(buildings)

        while left_index < len(left) and right_index < len(right):
            if left[left_index].coordinates[0] > right[right_index].coordinates[0]:
                result_buildings[merged_index] = left[left_index]
                left_index += 1
                pivot_index = merged_index
            else:
                result_buildings[merged_index] = right[right_index]
                if pivot_index > -1:
                    if result_buildings[pivot_index].coordinates[1] > result_buildings[merged_index].coordinates[1]:
                        result_buildings[pivot_index].dominance += 1
                right_index += 1
            merged_index += 1

        while left_index < len(left):
            result_buildings[merged_index] = left[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right):
            result_buildings[merged_index] = right[right_index]
            if pivot_index > -1:
                if result_buildings[pivot_index].coordinates[1] > result_buildings[merged_index].coordinates[1]:
                    result_buildings[pivot_index].dominance += 1
            right_index += 1
            merged_index += 1

        return result_buildings

def my_solution(buildings: list[Building]) -> None:
    # sort buildings by x coordinates
    upper_right_building = copy.deepcopy(buildings)
    lower_left_building = copy.deepcopy(buildings)

    upper_right_building.sort(key = lambda x: x.coordinates[0])
    lower_left_building.sort(key = lambda x: x.coordinates[1], reverse = True)

    upper_right_building = mergesort_and_count_upper_right(upper_right_building)
    lower_left_building = mergesort_and_count_lower_left(lower_left_building)

    upper_right_building.sort(key = lambda x: x.id)
    lower_left_building.sort(key = lambda x: x.id)
    buildings.sort(key = lambda x: x.id)

    for i in range(len(upper_right_building)):
        buildings[i].dominance = upper_right_building[i].dominance + lower_left_building[i].dominance

if __name__ == '__main__':
    # test(my_solution, map_size = 7)
    test_bulk(my_solution, number_of_random_tries = 10000, map_size = 250)