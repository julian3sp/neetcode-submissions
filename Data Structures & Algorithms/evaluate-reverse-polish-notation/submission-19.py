class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                result = (stack.pop()) + (stack.pop())
                stack.append(result)
            elif token == '-':
                a, b = (stack.pop()), (stack.pop())
                result = b - a
                stack.append(result)
            elif token == '/':
                a, b = (stack.pop()), (stack.pop())
                result = int(float(b) / (a))
                stack.append(result)
            elif token == '*':
                result = (stack.pop()) * (stack.pop())
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]