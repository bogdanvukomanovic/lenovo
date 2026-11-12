from typing import List

class Solution:

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        poisoned, poison_end = 0, -1

        for i, t in enumerate(timeSeries):

            if t > poison_end:
                poisoned += duration
            else:
                poisoned += (t - timeSeries[i-1])

            poison_end = t + duration - 1

        return poisoned

timeSeries, duration = [1, 4], 2
print(Solution().findPoisonedDuration(timeSeries, duration))
