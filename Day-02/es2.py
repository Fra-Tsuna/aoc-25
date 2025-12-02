import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    line = f.readline()
    ranges = [l.split('-') for l in line.split(',')]

def is_invalid(s):
    check = ''
    for c in s:
        check += c
        pattern = r"^(?:{}){{2,}}$".format(re.escape(check))
        if re.fullmatch(pattern, s):
            return True
    return False

total = 0

for r in ranges:
    a, b = r
    for num in range(int(a), int(b)+1):
        num_str = str(num)
        if is_invalid(num_str):
            total += num            
print(total)