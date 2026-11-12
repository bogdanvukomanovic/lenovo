import math 

def part_one(games: [(int, int)]) -> int:
    
    result = 1
    for game in games:
        
        t, d = game[0], game[1]

        # f(x) = x * (t - x) - d
        x_1 = (t - math.sqrt(t**2 - 4 * d)) / 2
        x_2 = (t + math.sqrt(t**2 - 4 * d)) / 2
        
        result *= (math.ceil(x_2) - math.floor(x_1) - 1)
    
    return result

games = [(40, 233), (82, 1011), (84, 1110), (92, 1487)] 
print(part_one(games))

def part_two(game: (int, int)) -> (int, int):
    
    t, d = game[0], game[1]

    # f(x) = x * (t - x) - d
    x_1 = (t - math.sqrt(t**2 - 4 * d)) / 2
    x_2 = (t + math.sqrt(t**2 - 4 * d)) / 2

    return (math.ceil(x_2) - math.floor(x_1) - 1)

game = (40828492, 233101111101487)
print(part_two(game))