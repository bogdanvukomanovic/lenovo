from typing import List

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ms = []

        for i, temperature in enumerate(temperatures):

            while ms and temperature > ms[-1][0]:
                x = ms.pop()
                temperatures[x[1]] = i - x[1]

            ms.append((temperature, i))

        for x in ms:
            temperatures[x[1]] = 0

        return temperatures

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
