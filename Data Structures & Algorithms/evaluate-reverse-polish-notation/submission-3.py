class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(float(y) / x))
            else:
                stack.append(int(token))
        
        return stack[0]