class Solution:

    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels = set([c for c in jewels])

        return sum([1 if c in jewels else 0 for c in stones]) 

jewels, stones = "aA", "aAAbbbb"
print(Solution().numJewelsInStones(jewels, stones))
