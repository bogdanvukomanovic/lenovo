from typing import List

def sweep(rows: List[str], row: int, start: int, end: int) -> bool:

    start = max(0, start-1)
    end = min(len(rows[row])-1, end + 1)

    if not rows[row][start].isdigit() and rows[row][start] != '.':
        return True  
    
    if not rows[row][end].isdigit() and rows[row][end] != '.':
        return True          

    for i in range(start, end + 1):
        
        if row != 0 and rows[row-1][i] != '.':
            return True
        
        if row != len(rows)-1 and rows[row+1][i] != '.':
            return True

    return False

def part_one(rows: List[str]) -> int:

    n = len(xs[0])
    result = 0
    for i, row in enumerate(rows):

        j = 0
        while j < n:
            
            number = ""
            if row[j].isdigit():
                
                start = j
                number += row[j]
                while j < n - 1 and row[j+1].isdigit():
                    number += row[j+1]
                    j += 1
                
                if sweep(rows, i, start, j):
                    result += int(number)
            
            number = ""

            j += 1

    return result

def get_gears(rows: List[str], row: int, x: int, n: int) -> (int, int):

    def get_number(row: str, i: int) -> int:
        
        number = row[i]
        
        l = i - 1
        r = i + 1

        while l > -1 and row[l].isdigit():
            number = row[l] + number
            l -= 1
        
        while r < len(row) and row[r].isdigit():
            number = number + row[r]
            r += 1

        return int(number)

    def up(row: str, start: int, end: int) -> List[int]:
        
        numbers = []

        i = start
        while i < end:
            if row[i].isdigit():
                numbers.append(get_number(row, i))
                break
            i += 1
        
        if end - start == 2 and row[end-1] == '.' and row[end].isdigit():
            numbers.append(get_number(row, end))

        return numbers
    
    def down(row: str, start: int, end: int) -> List[int]:
        
        numbers = []
        
        i = start
        while i < end:
            if row[i].isdigit():
                numbers.append(get_number(row, i))
                break
            i += 1
        
        if end - start == 2 and row[end-1] == '.' and row[end].isdigit():
            numbers.append(get_number(row, end))
        
        return numbers
    
    result = []

    if row != 0:
        result += up(rows[row-1], max(0, x - 1), min(len(rows[row]) - 1, x + 1))
    
    if row != n:
        result += down(rows[row+1], max(0, x-1), min(len(rows[row]) - 1, x + 1))

    l = x - 1
    west = ""
    while l > -1 and rows[row][l].isdigit():
        west = rows[row][l] + west
        l -= 1
    
    r = x + 1
    east = ""
    while r < len(rows[row]) and rows[row][r].isdigit():
        east = east + rows[row][r] 
        r += 1

    result.append(0 if west == "" else int(west))
    result.append(0 if east == "" else int(east))    

    result.sort(reverse = True)

    return result[0] * result[1]

def part_two(rows : List[str]) -> int:
    
    n = len(xs[0])
    result = 0
    for i, row in enumerate(rows):

        j = 0
        while j < n:
            
            if row[j] == '*':
                result += get_gears(rows, i, j, len(rows))
        
            j += 1

    return result

with open("in.txt") as f:
    xs = f.read().split('\n')

print(part_one(xs))
print(part_two(xs))