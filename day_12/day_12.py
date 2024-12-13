with open('test_input.txt', 'r') as file:
    garden = file.readlines()


def update_price_part1(map_: list, letter: str) -> (list, int):
    starting_point_x = min(ind for ind, row in enumerate(map_) if letter in row)
    starting_point_y = min(ind for ind, val in enumerate(map_[starting_point_x]) if val == letter)
    map_[starting_point_x][starting_point_y] = '.'
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    points = {(starting_point_x, starting_point_y): 0}
    increase = [(starting_point_x, starting_point_y)]
    while len(increase):
        new_increase = []
        for x, y in increase:
            for dx, dy in deltas:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_x >= len(map_) or new_y < 0 or new_y >= len(map_[0]):
                    continue
                if not map_[new_x][new_y] == letter:
                    continue

                points[(new_x, new_y)] = 0
                new_increase.append((new_x, new_y))
                map_[new_x][new_y] = '.'

        increase = new_increase

    for (x, y) in points.keys():
        for (dx, dy) in deltas:
            update_x, update_y = x + dx, y + dy
            if (update_x, update_y) in points.keys():
                points[(x, y)] += 1

    area, perimeter = 0, 0
    for neighbours in points.values():
        area += 1
        perimeter += 4 - neighbours

    return map_, area * perimeter


def update_price_part2(map_: list, letter: str) -> (list, int):
    starting_point_x = min(ind for ind, row in enumerate(map_) if letter in row)
    starting_point_y = min(ind for ind, val in enumerate(map_[starting_point_x]) if val == letter)
    map_[starting_point_x][starting_point_y] = '.'
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    points = {(starting_point_x, starting_point_y): 1}
    increase = [(starting_point_x, starting_point_y)]
    while len(increase):
        new_increase = []
        for x, y in increase:
            for dx, dy in deltas:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_x >= len(map_) or new_y < 0 or new_y >= len(map_[0]):
                    continue
                if not map_[new_x][new_y] == letter:
                    continue

                points[(new_x, new_y)] = 1
                new_increase.append((new_x, new_y))
                map_[new_x][new_y] = '.'

        increase = new_increase
    
    area, angles = 0, 0        
    for x, y in points:
        area += 1
        top = points.get((x - 1, y)) == 1
        top_right = points.get((x - 1, y + 1)) == 1
        right = points.get((x, y + 1)) == 1
        bottom_right = points.get((x + 1, y + 1)) == 1
        bottom = points.get((x + 1, y)) == 1
        bottom_left = points.get((x + 1, y - 1)) == 1
        left = points.get((x, y - 1)) == 1
        top_left = points.get((x - 1, y - 1)) == 1
        
    return map_, area * angles


garden = [[gg for gg in g if gg != '\n'] for g in garden]
unique_plants = set(gg for g in garden for gg in g)
total_price = 0
for plant in unique_plants:
    garden_plant = [[gg if gg == plant else '.' for gg in g] for g in garden]
    plant_price = 0
    while True:
        garden_plant, price = update_price_part1(garden_plant, plant)
        plant_price += price
        if all(gg == '.' for g in garden_plant for gg in g):
            break
    total_price += plant_price
print(f'part 1: {total_price=}')

total_price = 0
for plant in unique_plants:
    garden_plant = [[gg if gg == plant else '.' for gg in g] for g in garden]
    plant_price = 0
    while True:
        garden_plant, price = update_price_part2(garden_plant, plant)
        plant_price += price
        if all(gg == '.' for g in garden_plant for gg in g):
            break

    total_price += plant_price
print(f'part 2: {total_price=}')
