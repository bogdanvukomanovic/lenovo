from typing import List

class Solution:

    def intersect(self, k1: int, n1: int, k2: int, n2: int) -> float:
        return k1 * ((n2 - n1) / (k1 - k2)) + n1

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        idx = list(zip(*sorted(enumerate(position), key = lambda x : x[1], reverse = True)))[0]

        for i in idx:

            if stack and stack[-1][1] < speed[i] and self.intersect(stack[-1][1], stack[-1][0], speed[i], position[i]) <= target:
                    x = stack.pop()
                    stack.append((x[0], x[1]))
            else:
                stack.append((position[i], speed[i]))

        return len(stack)

target, position, speed = 12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]
target, position, speed = 10, [3], [3]
target, position, speed = 100, [0, 2, 4], [4, 2, 1]
target, position, speed = 10, [0, 4, 2], [2, 1, 3]
target, position, speed = 31, [5, 26, 18, 25, 29, 21, 22, 12, 19, 6], [7, 6, 6, 4, 3, 4, 9, 7, 6, 4]
print(Solution().carFleet(target, position, speed))
