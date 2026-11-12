from typing import List
import re

def part_one(games: List[str]) -> int:
    
    result = 0
    
    for game in games:
        
        game = game.split('|')
        
        win = list(map(lambda x: int(x), re.findall(r"(\d+)", game[0])))
        got = list(map(lambda x: int(x), re.findall(r"(\d+)", game[1])))
        
        win = set(win[1:])
        
        match = 0
        for x in got:
            if x in win:
                match += 1

        if match != 0:
            result += 2**(match - 1)
    
    return result
        
def part_two(games: List[str]) -> int:
    
    result = [1] * len(games)

    for i, game in enumerate(games):
        
        game = game.split('|')
        
        win = list(map(lambda x: int(x), re.findall(r"(\d+)", game[0])))
        got = list(map(lambda x: int(x), re.findall(r"(\d+)", game[1])))
        
        win = set(win[1:])

        match = 0
        for x in got:
            if x in win:
                match += 1

        for j in range(i + 1, i + match + 1):
            result[j] += result[i]

    return sum(result)

with open("in.txt") as f:
    xs = f.readlines()

print(part_one(xs))
print(part_two(xs))