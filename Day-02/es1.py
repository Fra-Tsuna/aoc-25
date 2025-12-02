import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    line = f.readline()
    ranges = [l.split('-') for l in line.split(',')]

def split_string(s, l):
    l = len(s)
    return s[:l//2], s[l//2:]
    
def is_invalid(a, b):
    return a == b

total = 0

for r in ranges:
    a, b = r
    for num in range(int(a), int(b)+1):
        num_str = str(num)
        l = len(num_str)
        if l % 2 == 0:
            s1, s2 = split_string(num_str, l)
            if is_invalid(s1, s2):
                total += num            
print(total)