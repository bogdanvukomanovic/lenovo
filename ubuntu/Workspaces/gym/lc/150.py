from typing import List

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operators = {
            "+" : lambda x, y : x + y,
            "-" : lambda x, y : x - y,
            "*" : lambda x, y : x * y,
            "/" : lambda x, y : x / y
        }

        for token in tokens:

            if token in operators:
                y, x = stack.pop(), stack.pop()
                stack.append(int(operators[token](x, y)))
            else:
                stack.append(int(token))

        return stack.pop()

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))
