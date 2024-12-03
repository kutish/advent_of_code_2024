import re

with open('input.txt', 'r') as file:
    string = file.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern=pattern, string=string)
    total_mul_sum = 0
    for m in matches:
        first_number = int(m.split(',')[0].replace('mul(', ''))
        second_number = int(m.split(',')[-1].replace(')', ''))
        total_mul_sum += first_number * second_number
    print(f'part 1: {total_mul_sum}')
    
    pattern_do, pattern_dont = r"do\(\)", r"don't\(\)"
    total_mul_sum_corrected = 0
    is_enabled = True
    while len(string):
        m = re.search(pattern=pattern, string=string)
        if not m:
            break
        
        m_do = re.search(pattern=pattern_do, string=string[:m.end()])
        if m_do:
            is_enabled = True
        else:
            m_dont = re.search(pattern=pattern_dont, string=string[:m.end()])
            if m_dont:
                is_enabled = False
                
        if is_enabled:
            first_number = int(m[0].split(',')[0].replace('mul(', '')) # noqa
            second_number = int(m[0].split(',')[-1].replace(')', '')) # noqa
            total_mul_sum_corrected += first_number * second_number
        
        string = string[m.end():]

    print(f'part 2: {total_mul_sum_corrected}')
    