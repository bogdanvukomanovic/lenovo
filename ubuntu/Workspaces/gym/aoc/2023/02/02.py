import re
from typing import List

def part_one(xs: List[str]) -> int:

    R, G, B = 12, 13, 14
    r, g, b = 0, 0, 0 

    result = 0

    for x in xs:
        
        games = re.findall(r"(\d+) (red|green|blue)", x)
        for game in games:
            
            match game[1]:
            
                case "red":
                    r = max(r, int(game[0]))
            
                case "green":
                    g = max(g, int(game[0]))
                    
                case "blue":
                    b = max(b, int(game[0]))

        if r <= R and g <= G and b <= B:
            result += int(re.findall(r"Game (\d+)", x)[0])

        r, g, b = 0, 0, 0

    return result
            

def part_two(xs: List[str]) -> int:

    r, g, b = 0, 0, 0 

    result = 0

    for x in xs:
        
        games = re.findall(r"(\d+) (red|green|blue)", x)
        for game in games:
            
            match game[1]:
            
                case "red":
                    r = max(r, int(game[0]))
            
                case "green":
                    g = max(g, int(game[0]))
                    
                case "blue":
                    b = max(b, int(game[0]))

        result += (r * g * b)
        r, g, b = 0, 0, 0

    return result

with open("in.txt") as f:
    xs = f.readlines()

print(part_one(xs))
print(part_two(xs))