class Solution:

    def isValid(self, xs: str) -> bool:

        if len(xs) == 1:
            return False

        open = set(['(', '{', '['])
        close = {')': '(', '}' : '{', ']' : '['}

        stack = []
        for s in xs:
            if s in open:
                stack.append(s)
            elif len(stack) == 0 or stack.pop() != close[s]:
                return False

        return True if len(stack) == 0 else False

print(Solution().isValid("()[]{}"))
