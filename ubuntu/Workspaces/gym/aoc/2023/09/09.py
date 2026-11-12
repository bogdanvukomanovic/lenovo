def extrapolate(xs: [int]) -> int:

    level = len(xs)
    result = []

    j = 0
    while level > 0:

        if not any(xs[j:level + 1 + j]):
           level = 0
        else:
            result.append(xs[-1])

        for i in range(level - 1, 0, -1):
            xs[i+j] = xs[i+j] - xs[i+j-1]

        j += 1
        level -= 1

    return sum(result)

def solve(reports: [[int]], direction: int) -> int:

    result = 0
    for report in reports:
        result += extrapolate(report[::direction])

    return result

with open("in.txt") as f:
    reports = [list(map(int, line.split())) for line in f.read().split('\n')]

print(solve(reports.copy(), 1))
print(solve(reports.copy(), -1))