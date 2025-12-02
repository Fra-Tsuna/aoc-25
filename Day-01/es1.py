import os

with open("Day-01/input1.txt") as f:
    lines = [line.strip() for line in f]

data = [
    int(line[1:]) if line.startswith('R') else -1*int(line[1:]) for line in lines
]   

total = 50
result = [
    1 if (total:=total+d) % 100 == 0 else 0 for d in data 
]

print(sum(result))