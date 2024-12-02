safe_reports = 0
dampened_safe_reports = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = [int(l) for l in line.split()]
        line_shift = line[1:]
        is_safe = True
        deltas = [next_level - level for level, next_level in zip(line, line_shift)]
        if not (all([d > 0 for d in deltas]) or all([d < 0 for d in deltas])):
            is_safe = False
        elif not all([1 <= d <= 3 or -3 <= d <= -1 for d in deltas]):
            is_safe = False
        
        if is_safe:
            safe_reports += 1
            continue

        is_dampened = False
        for index, _ in enumerate(line):
            dampened_line = [l for i, l in enumerate(line) if i != index]
            dampened_line_shift = dampened_line[1:]
            dampened_is_safe = True
            deltas = [next_level - level for level, next_level in zip(dampened_line, dampened_line_shift)]
            if not (all([d > 0 for d in deltas]) or all([d < 0 for d in deltas])):
                dampened_is_safe = False
            elif not all([1 <= d <= 3 or -3 <= d <= -1 for d in deltas]):
                dampened_is_safe = False

            if dampened_is_safe:
                is_dampened = True
                break
        
        if is_dampened:
            dampened_safe_reports += 1

print(f'part 1: {safe_reports=}')
print(f'part 2: {dampened_safe_reports=}')
