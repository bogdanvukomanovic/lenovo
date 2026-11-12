import re
from typing import List

def part_one(xs: List[str]) -> int:

    sum =  0

    for x in xs:

        numbers = re.findall(r'\d', x)
        sum += int(numbers[0] + numbers[-1])
        
    return sum

table = {
    "one"   : "1",
    "two"   : "2",
    "three" : "3",
    "four"  : "4",
    "five"  : "5",
    "six"   : "6",
    "seven" : "7",
    "eight" : "8",
    "nine"  : "9",
}

def convert(x: str, y: str) -> int:
    
    if x in table:
        x = table[x]
    
    if y in table:
        y = table[y]
    
    return int(x + y)

def part_two(xs: List[str]) -> int:
    
    sum = 0

    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

    for x in xs:

        numbers = re.findall(pattern, x)
        sum += convert(numbers[0], numbers[-1])
    
    return sum

with open("in.txt") as f:
    xs = f.readlines()

print(part_one(xs))
print(part_two(xs))