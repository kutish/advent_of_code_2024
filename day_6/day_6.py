from tqdm import tqdm
from copy import deepcopy
from itertools import product
from time import time

with open('input.txt', 'r') as file:
    area_map = file.readlines()

area_map = [[aa for aa in a if aa != '\n'] for a in area_map]

next_direction_dict = {'^': '>', 'v': '<', "<": "^", ">": "v"}


def get_next_coordinates(coordinates_, currect_direction):
    match currect_direction:
        case "^":
            next_coordinates_ = [coordinates_[0] - 1, coordinates_[1]]
        case "v":
            next_coordinates_ = [coordinates_[0] + 1, coordinates_[1]]
        case "<":
            next_coordinates_ = [coordinates_[0], coordinates_[1] - 1]
        case ">":
            next_coordinates_ = [coordinates_[0], coordinates_[1] + 1]
        case _:
            raise ValueError(f"Unknown direction: {currect_direction}")
    return next_coordinates_


def check_for_obstacle(area_map_: list, currect_direction: str, coordinates_: list):
    next_coordinates_ = get_next_coordinates(coordinates_, currect_direction)
    if any(n < 0 for n in next_coordinates_):
        return False, True, next_coordinates_

    try:
        area_map_[next_coordinates_[0]][next_coordinates_[1]]
    except IndexError:
        return False, True, next_coordinates_

    is_obstacle_ = area_map_[next_coordinates_[0]][next_coordinates_[1]] == "#"
    return is_obstacle_, False, next_coordinates_


def make_next_step(area_map_: list, current_direction: str, coordinates_: list):
    is_obstacle, is_out_of_bounds_, next_coordinates = check_for_obstacle(area_map_, current_direction, coordinates_)
    if is_obstacle:
        new_direction = next_direction_dict[current_direction]
    else:
        new_direction = current_direction

    new_coordinates = get_next_coordinates(coordinates, new_direction)
    area_map_[coordinates[0]][coordinates[1]] = 'X'
    if not is_out_of_bounds_:
        area_map_[new_coordinates[0]][new_coordinates[1]] = new_direction
    return area_map_, new_direction, new_coordinates, is_out_of_bounds_


coordinates = [ind for ind, row in enumerate(area_map) if '^' in row]
coordinates = [
    coordinates[0],
    [ind for ind, col in enumerate(area_map[coordinates[0]]) if col == '^'][0]
]
direction = '^'
visited_coordinates = []

while True:
    area_map, direction, coordinates, is_out_of_bounds = make_next_step(area_map, direction, coordinates)
    if coordinates not in visited_coordinates:
        visited_coordinates.append(coordinates)
    if is_out_of_bounds:
        break

area_map = '\n'.join(''.join(a) for a in area_map)
print('part 1:', sum([1 if a == 'X' else 0 for a in area_map]))

with open('input.txt', 'r') as file:
    area_map = file.readlines()

area_map = [[aa for aa in a if aa != '\n'] for a in area_map]
loop_count = 0
for obstacle_coordinates in tqdm(
        list(
            product(
                [i for i in range(len(area_map))],
                [i for i in range(len(area_map[0]))],
            )
        )
):
    new_area_map = deepcopy(area_map)
    if new_area_map[obstacle_coordinates[0]][obstacle_coordinates[1]] != '.':
        continue

    new_area_map[obstacle_coordinates[0]][obstacle_coordinates[1]] = '#'

    coordinates = [ind for ind, row in enumerate(area_map) if '^' in row]
    coordinates = [
        coordinates[0],
        [ind for ind, col in enumerate(area_map[coordinates[0]]) if col == '^'][0]
    ]
    direction = '^'
    start = time()
    while True:
        new_area_map, direction, coordinates, is_out_of_bounds = make_next_step(new_area_map, direction, coordinates)
        if is_out_of_bounds:
            break
            
        if time() - start > 1:
            loop_count += 1
            break

print(f'part 2: {loop_count}')
