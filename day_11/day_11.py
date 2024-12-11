from functools import cache
import sys
sys.set_int_max_str_digits(100000)

with open('input.txt', 'r') as file:
    stones_list = file.readline()

stones_list = [int(stone) for stone in stones_list.split() if stone != '\n']


@cache
def count_stones(stone: int, steps:int) -> int:
    if steps == 0:
        return 1
    if not (ln:=divmod(len(str_stone:=str(stone)),2))[1]:
        return sum(count_stones(int(st),steps-1) for st in [str_stone[:ln[0]],str_stone[ln[0]:]])
    else:
        return count_stones(stone*2024 if stone else 1,steps-1)
    

def part1(data:list) -> int:
    return sum(count_stones(stone,25) for stone in data)


def part2(data:list) -> int:
    return sum(count_stones(stone,75) for stone in data)

print(f'part 1: {part1(stones_list)}')
print(f'part 2: {part2(stones_list)}')