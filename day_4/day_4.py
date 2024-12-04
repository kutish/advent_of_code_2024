import numpy as np
from tqdm import tqdm

with open('input.txt', 'r') as file:
    matrix = file.readlines()
    
matrix = [
    [mm for mm in m if mm != '\n']
    for m in matrix
]
matrix = np.array(matrix)
xmas_count = 0
search_string = 'XMAS'
# horizontal and backwards horizontal
for row in matrix:
    for index in range(len(row)):
        substring = ''.join(row[index:index+4])
        if substring == search_string or substring == search_string[::-1]:
            xmas_count += 1
            
x_coordinates = []
m_coordinates = []
a_coordinates = []
s_coordinates = []
for x in range(matrix.shape[0]):
    for y in range(matrix.shape[1]):
        if matrix[x][y]=='X':
            x_coordinates.append((x, y))
        if matrix[x][y]=='M':
            m_coordinates.append((x, y))
        if matrix[x][y]=='A':
            a_coordinates.append((x, y))
        if matrix[x][y]=='S':
            s_coordinates.append((x, y))

# diagonal
word_coordinates = set()
for next_x in tqdm(x_coordinates, desc='Diagonals search:'):
    for direction_x, direction_y in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        next_m = [(xx, yy) for xx, yy in m_coordinates if next_x[0] - xx == direction_x and next_x[1] - yy == direction_y]
        if next_m:
            next_m = next_m[0]
            next_a = [(xx, yy) for xx, yy in a_coordinates if next_m[0] - xx == direction_x and next_m[1] - yy == direction_y]
            if next_a:
                next_a = next_a[0]
                next_s = [(xx, yy) for xx, yy in s_coordinates if next_a[0] - xx == direction_x and next_a[1] - yy == direction_y]
                if next_s:
                    next_s = next_s[0]
                    word_coord = (next_x, next_m, next_a, next_s)
                    reverse_word_coord = (next_s, next_a, next_m, next_x)
                    if word_coord not in word_coordinates and reverse_word_coord not in word_coordinates:
                        word_coordinates.add(word_coord)
                        word_coordinates.add(reverse_word_coord)
                        xmas_count += 1
            
matrix = matrix.T
# vertical and backwards vertical
for row in matrix:
    for index in range(len(row)):
        substring = ''.join(row[index:index+4])
        if substring == search_string or substring == search_string[::-1]:
            xmas_count += 1
            
print(f'part 1: {xmas_count=}')

with open('input.txt', 'r') as file:
    matrix = file.readlines()

matrix = [
    [mm for mm in m if mm != '\n']
    for m in matrix
]
matrix = np.array(matrix)
mas_count = 0
mas_coordinates = set()
for next_a in tqdm(a_coordinates, desc='X-mas search:'):
    if next_a[0] - 1 < 0 or next_a[1] - 1 < 0:
        continue
    if next_a[0] + 1 >= matrix.shape[0] or next_a[1] + 1 >= matrix.shape[1]:
        continue
        
    top_left_letter = matrix[next_a[0] - 1][next_a[1] - 1]
    if top_left_letter not in ('M', 'S'):
        continue
    
    top_right_letter = matrix[next_a[0] - 1][next_a[1] + 1]
    if top_right_letter not in ('M', 'S'):
        continue
        
    bottom_left_letter = matrix[next_a[0] + 1][next_a[1] - 1]
    if bottom_left_letter not in ('M', 'S'):
        continue

    bottom_right_letter = matrix[next_a[0] + 1][next_a[1] + 1]
    if bottom_right_letter not in ('M', 'S'):
        continue
        
    if top_left_letter == bottom_right_letter:
        continue
        
    if bottom_left_letter == top_right_letter:
        continue
        
    mas_count += 1
    mas_coordinates.add((top_left_letter, top_right_letter, next_a, bottom_left_letter, bottom_right_letter))
    
print(f'part 2: {mas_count=}')
