from itertools import product


antennas_coordinates_dict = {}
field = []
with open('input.txt', 'r') as file:
    for row_num, row in enumerate(file.readlines()):
        max_x = len(row.strip())
        max_y = 0
        field.append([r for r in row if r != '\n'])
        for col_num, val in enumerate(row):
            max_y = max(max_x, col_num) if val != '\n' else max_x
            if val in '.\n':
                continue
            if val not in antennas_coordinates_dict:
                antennas_coordinates_dict[val] = [(row_num, col_num)]
            else:
                antennas_coordinates_dict[val].append((row_num, col_num))

antinodes_coordinates = []
all_antennas_coordinates = [v for val in antennas_coordinates_dict.values() for v in val]
for _, coordinates in antennas_coordinates_dict.items():
    pairs_of_pairs = product(coordinates, repeat=2)
    for coord1, coord2 in pairs_of_pairs:
        if coord1 == coord2:
            continue
            
        new_x = 2 * coord2[0] - coord1[0]
        new_y = 2 * coord2[1] - coord1[1]
        if (
                0 <= new_x <= max_x
            and 0 <= new_y <= max_y
            and (new_x, new_y) not in antinodes_coordinates
        ):
            antinodes_coordinates.append((new_x, new_y))

        new_x = 2 * coord1[0] - coord2[0]
        new_y = 2 * coord1[1] - coord2[1]
        if (
                0 <= new_x <= max_x
            and 0 <= new_y <= max_y
            and (new_x, new_y) not in antinodes_coordinates
        ):
            antinodes_coordinates.append((new_x, new_y))

antinode_count = 0
for x, y in antinodes_coordinates:
    try:
        field[x][y] = '#'
        antinode_count += 1
    except IndexError:
        continue
        
# print('\n'.join([''.join(f) for f in field]))
print(f'part 1: {antinode_count}')

antinodes_coordinates = set()
all_antennas_coordinates = [v for val in antennas_coordinates_dict.values() for v in val]
for _, coordinates in antennas_coordinates_dict.items():
    pairs_of_pairs = product(coordinates, repeat=2)
    for coord1, coord2 in pairs_of_pairs:
        if coord1 == coord2:
            continue
        
        dx = coord1[0] - coord2[0]
        dy = coord1[1] - coord2[1]
        i = 0
        while True:
            new_x = coord1[0] + i * dx
            new_y = coord1[1] + i * dy
            if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                break
            else:
                antinodes_coordinates.add((new_x, new_y))
            i += 1

        dx = coord2[0] - coord1[0]
        dy = coord2[1] - coord1[1]
        i = 0
        while True:
            new_x = coord2[0] + i * dx
            new_y = coord2[1] + i * dy
            if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                break
            else:
                antinodes_coordinates.add((new_x, new_y))
            i += 1
            
antinode_count = 0
for x, y in antinodes_coordinates:
    try:
        field[x][y] = '#'
        antinode_count += 1
    except IndexError:
        continue

print(f'part 2: {antinode_count}')