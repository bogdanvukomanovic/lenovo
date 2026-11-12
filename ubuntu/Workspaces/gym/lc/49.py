from typing import List

class Solution:

    def groupAnagrams(self, xs: List[str]) -> List[List[str]]:

        hash = {}

        for x in xs:

            y = "".join(sorted(x))

            if y in hash:
                hash[y].append(x)
            else:
                hash[y] = [x]

        return [v for (_, v) in hash.items()]

xs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(xs))
