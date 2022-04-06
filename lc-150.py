from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 3 2 + => 3 + 2
        # 3 2 1 + * => (3 + 2) * 1

        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                f_number, s_number = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(f_number + s_number)
                elif token == "-":
                    stack.append(s_number - f_number)
                elif token == "*":
                    stack.append(f_number * s_number)
                elif token == "/":
                    stack.append(int(s_number / f_number))
        return stack[0]


s = Solution()
tc = [3, 2, 1, "+", "*"]
print(s.evalRPN(tc))
