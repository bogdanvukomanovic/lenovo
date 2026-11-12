import math
import re

def part_one(instructions: str, graph: {str : (str, str)}) -> int:

    state = "AAA"

    i, n = 0, len(instructions)
    while state != "ZZZ":

        direction = 0 if instructions[i % n] == 'L' else 1
        state = graph[state][direction]

        i += 1

    return i

def detect_cycle(start: str, instructions: str, graph: {str : (str, str)}) -> int:

    state = start

    i, n = 0, len(instructions)
    while not state.endswith('Z'):

        direction = 0 if instructions[i % n] == 'L' else 1
        state = graph[state][direction]

        i += 1

    return i

def part_two(instructions: str, graph: {str : (str, str)}, starting_nodes: [str], ending_nodes: [str]) -> int:

    cycles = []
    for start in starting_nodes:
        cycles.append(detect_cycle(start, instructions, graph))

    return math.lcm(*cycles)

with open("in.txt") as f:
    content = f.read().split('\n\n')

instructions = content[0]
graph = {}

for node in re.findall(r'(\w\w\w) = \((\w\w\w), (\w\w\w)\)', content[1]):
    graph[node[0]] = (node[1], node[2])

print(part_one(instructions, graph))

starting_nodes = []
for node in re.findall(r'(\w\wA) =', content[1]):
    starting_nodes.append(node)

ending_nodes = []
for node in re.findall(r'(\w\wZ) =', content[1]):
    ending_nodes.append(node)

print(part_two(instructions, graph, starting_nodes, ending_nodes))