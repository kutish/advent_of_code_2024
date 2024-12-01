with open('input.txt', 'r') as file:
    lines = file.readlines()
    
locations_list_1 = [int(l.split(' ')[0].strip()) for l in lines]
locations_list_2 = [int(l.split(' ')[-1].strip()) for l in lines]

locations_list_1.sort()
locations_list_2.sort()

total_distance = 0
for l1, l2 in zip(locations_list_1, locations_list_2):
    total_distance += abs(l1 - l2)
print(f'{total_distance=}')

similarity_score = 0
for l1 in locations_list_1:
    similarity_score += l1 * len([l2 for l2 in locations_list_2 if l2 == l1])
print(f"{similarity_score=}")
