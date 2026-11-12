class Solution:
    
    def removeDuplicates(self, xs: str) -> str:
        stack = []

        for s in xs:

            if len(stack) != 0 and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)

        return "".join(stack)

xs = "azxxzy"
print(Solution().removeDuplicates(xs))