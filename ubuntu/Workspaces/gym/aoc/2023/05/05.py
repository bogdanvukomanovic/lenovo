import re

def apply(f: list[(int, int, int)], x: int) -> int:

    lb = 0
    ub = len(f)

    if x < f[lb][1] or x >= f[ub-1][1] + f[ub-1][2]:
        return x
    
    while lb < ub - 1:

        m = lb + (ub - lb) // 2

        if x >= f[m][1]:
            lb = m
        else:
            ub = m

    if x > f[lb][1] + f[lb][2]:
        return x

    return (x - f[lb][1]) + f[lb][0] 

def part_one(maps: list[list[(int, int, int)]], xs: list[int]) -> int:
    
    result = float('inf')

    for x in xs:
        for f in maps:
            x = apply(f, x)

        result = min(result, x)
    
    return result

with open("in.txt") as f:
    content = f.read().split('\n\n')

xs = list(map(lambda x: int(x), re.findall(r'(\d+)', content[0])))

maps = []
for f in content[1:]:
    maps.append(sorted(list(map(lambda x: (int(x[0]), int(x[1]), int(x[2])), map(lambda x: x.split(), re.findall(r'(\d+ \d+ \d+)', f)))), key = lambda x: x[1]))

print(part_one(maps, xs))

def intersect(a: (int, int), b: (int, int)) -> bool:
    return a[0] <= b[1] and b[0] < a[1]

def apply_on_ranges(f: list[(int, int, int)], ranges: list[(int, int)]) -> list[(int, int)]:
  
    result = []

    for range in ranges:
        
        processed = []
        
        for pair in f:
            
            if intersect((pair[1], pair[1] + pair[2]), range):

                A = max(range[0], pair[1])
                B = min(range[1], pair[1] + pair[2] - 1)

                result.append(((A - pair[1]) + pair[0], (B - pair[1]) + pair[0]))
                
                processed.append((A, B))

        for interval in sorted(processed, key = lambda x: x[0]):

            if interval[0] == range[0]:
                range = (interval[1], range[1])
            else:
                result.append((range[0], interval[0] - 1))
                
                range = (interval[1] + 1, range[1])

        if range[0] != range[1]:
            result.append(range)  

    return result
    
def part_two(ranges: list[(int, int)], maps: list[list[(int, int, int)]]) -> int:

    for f in maps:
        ranges = apply_on_ranges(f, ranges)

    return sorted(ranges, key = lambda x : x[0])[0][0]

xs = list(map(lambda x: (int(x[0]), int(x[0]) + int(x[1])), map(lambda x: x.split(), re.findall(r'(\d+ \d+)', content[0]))))

maps = []
for f in content[1:]:
    maps.append(sorted(list(map(lambda x: (int(x[0]), int(x[1]), int(x[2])), map(lambda x: x.split(), re.findall(r'(\d+ \d+ \d+)', f)))), key = lambda x: x[0]))

print(part_two(xs, maps))

# def apply_inverse(f: list[(int, int, int)], y: int) -> int:

#     lb = 0
#     ub = len(f)

#     if y < f[lb][0] or y >= f[ub-1][0] + f[ub-1][2]:
#         return y
    
#     while lb < ub - 1:

#         m = lb + (ub - lb) // 2

#         if y >= f[m][0]:
#             lb = m
#         else:
#             ub = m

#     if y > f[lb][0] + f[lb][2]:
#         return y

#     return f[lb][1] + (y - f[lb][0])

# def part_two(maps: list[list[(int, int, int)]], ranges: list[(int, int)]) -> int:

#     i = 0

#     while True:
        
#         y = i 
#         for f in maps[::-1]:
#             y = apply_inverse(f, y)

#         for range in ranges:
#             if range[0] <= y and y <= range[1]:
#                 return i
            
#         i += 1