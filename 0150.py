class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for val in tokens:
            if val not in '+-*/':
                stack.append(int(val))
                continue
            x, y = stack.pop(), stack.pop()
            if val == '+':
                stack.append(x+y)
            elif val == '*':
                stack.append(x*y)
            elif val == '/':
                res = float(y)/x
                stack.append(int(res))
            elif val == '-':
                stack.append(y-x)
        return stack[0]