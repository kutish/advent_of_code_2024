from itertools import product
from tqdm import tqdm


def check(operands_: list, operators_: tuple, result_: int) -> bool:
    calculations_list = []
    for i in range(len(operands_) + len(operators_)):
        if i % 2:
            calculations_list.append(operators_[i//2])
        else:
            calculations_list.append(operands_[i//2])
    
    res = calculations_list[0]
    current_operator = -2 # -1 == +, 0 == *, 1 == |
    for elem in calculations_list[1:]:
        if elem == '+':
            current_operator = -1
        elif elem == '*':
            current_operator = 0
        elif elem == '|':
            current_operator = 1
        elif isinstance(elem, int):
            if current_operator == -1:
                res += elem
            elif current_operator == 0:
                res *= elem
            else:
                res = int(str(res) + str(elem))
        
    return result_ == res


with open('input.txt', 'r') as file:
    correct_calibration_result_sum = 0
    for line in tqdm(file.readlines()):
        result, operands = line.split(':')[0], line.split(':')[1:]
        result = int(result)
        operands = [op.strip() for op in operands][0]
        operands = [int(op) for op in operands.split()]
        possible_operators = ['*', '+', '|'] # ["*", "+"] for part 1
        all_combinations_of_operators = [comb for comb in product(possible_operators, repeat=len(operands)-1)]
        for operators in all_combinations_of_operators:
            if check(operands, operators, result):
                correct_calibration_result_sum += result
                break
        
    print(f'part 2: {correct_calibration_result_sum=}')
