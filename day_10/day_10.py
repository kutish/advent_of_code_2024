with open('input.txt', 'r') as file:
    map_ = file.readlines()

map_ = [[int(mm) for mm in m.strip()] for m in map_]
coordinates_of_zeros = [
    (row_num, col_num)
    for row_num, row in enumerate(map_)
    for col_num, val in enumerate(row)
    if val == 0
]
part_1_dict = {}
part_2_dict = {}


def traverse(map__: list, paths: list) -> (list, bool):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new_paths = []
    increased = False
    for path in paths:
        xlast, ylast, current_val_ = path[-1]
        for dx, dy in deltas:
            try:
               next_val = map__[xlast + dx][ylast + dy]
            except IndexError:
                continue
            if xlast + dx < 0 or ylast + dy < 0:
                continue
            if next_val - current_val_ == 1:
                new_paths.append(path + [(xlast + dx, ylast + dy, next_val),])
                increased = True
    
    if all(path[-1][-1] == 9 for path in new_paths):
        increased = False
    
    return new_paths, increased
    
    
for x0, y0 in coordinates_of_zeros:
    current_val = 0
    all_paths = [
        [(x0, y0, current_val)]
    ]
    do_continue = True
    while do_continue:
        all_paths, do_continue = traverse(map_, all_paths)

    part_2_dict[(x0, y0)] = len(all_paths)
    all_paths = len(list(set(path[-1] for path in all_paths)))
    part_1_dict[(x0, y0)] = all_paths       

print(f'part 1: {sum(part_1_dict.values())}')
print(f'part 2: {sum(part_2_dict.values())}')
