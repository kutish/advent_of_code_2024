from functools import cmp_to_key

rules_list = []
manuals_list = []
is_rules = True

with open('input.txt', 'r') as file:
    for line in file.readlines():
        if not line.strip():
            is_rules = False
            continue

        if is_rules:
            rules_list.append(line.strip().split('|'))
        else:
            manuals_list.append(line.strip().split(','))

correct_middle_pages_sum = 0
incorrect_middle_pages_sum = 0
for manual in manuals_list:
    is_correct = True
    relevant_rules_list = []
    for rule in rules_list:
        is_relevant = any(rule[0] == m for m in manual)
        is_relevant |= any(rule[1] == m for m in manual)
        if is_relevant:
            relevant_rules_list.append(rule)

        if not is_correct:
            continue

        index_rule_0 = [i for i, val in enumerate(manual) if val==rule[0]]
        if not index_rule_0:
            continue

        index_rule_1 = [i for i, val in enumerate(manual) if val==rule[1]]
        if not index_rule_1:
            continue

        if index_rule_0[0] > index_rule_1[0]:
            is_correct = False

    if is_correct:
        correct_middle_pages_sum += int(manual[len(manual)//2])
        continue

    correct_manual = sorted(manual, key=cmp_to_key(lambda x,y: 1-2*([x, y] in relevant_rules_list)))
    incorrect_middle_pages_sum += int(correct_manual[len(correct_manual)//2])

print(f'part 1: {correct_middle_pages_sum=}')
print(f'part 2: {incorrect_middle_pages_sum=}')