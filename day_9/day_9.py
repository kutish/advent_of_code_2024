from tqdm import tqdm

with open('input.txt', 'r') as file:
    line = file.readline()
    
line = [int(l) for l in line]
data_list = []
is_data = True
file_id = 0
for char in tqdm(line, "Building data list"):
    if is_data:
        for b in range(char):
            data_list.append(file_id)
        file_id += 1
    else:
        for b in range(char):
            data_list.append('.')
    is_data = not is_data

dots_count = sum([1 if char == '.' else 0 for char in data_list])
for _ in tqdm(range(dots_count), "Moving parts of files"):
    first_dot_index = [ind for ind, val in enumerate(data_list) if val == '.'][0]
    last_nondot_index = [ind for ind, val in enumerate(data_list) if val != '.'][-1]
    data_list[first_dot_index], data_list[last_nondot_index] = data_list[last_nondot_index], data_list[first_dot_index]
    
control_sum = sum(num * val for num, val in enumerate(data_list) if val != '.')
print(f'part 1: {control_sum}')

with open('input.txt', 'r') as file:
    line = file.readline()

line = [int(l) for l in line]
data_list = []
is_data = True
file_id = 0
file_size_dict = {}
for char in tqdm(line, "Building data list"):
    if is_data:
        file_size_dict[file_id] = char
        for b in range(char):
            data_list.append(file_id)
        file_id += 1
    else:
        for b in range(char):
            data_list.append('.')
    is_data = not is_data
    
for file_id in tqdm(sorted(file_size_dict.keys(), reverse=True), "Moving whole files"):
    leftmost_pos = min(ind for ind, val in enumerate(data_list) if val == file_id)
    size = file_size_dict[file_id]
    end_pos = None
    current_size = 0
    for i in range(0, leftmost_pos):
        if data_list[i] == '.':
            current_size += 1
        else:
            current_size = 0
        if current_size == size:
            end_pos = i
            break
    
    if not end_pos:
        continue
        
    for k in range(size):
        data_list[leftmost_pos + k], data_list[end_pos - k] = data_list[end_pos - k], data_list[leftmost_pos + k]
    
control_sum = sum(num * val for num, val in enumerate(data_list) if val != '.')
print(f'part 2: {control_sum}')
