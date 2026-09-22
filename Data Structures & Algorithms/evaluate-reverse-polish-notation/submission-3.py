class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if (c == '+'):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1 + num2)
            elif (c == '-'):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2 - num1)
            elif (c == '*'):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1 * num2)
            elif (c == '/'):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2 / num1)
            else:
                stack.append(int(c))
        return int(stack[0])
