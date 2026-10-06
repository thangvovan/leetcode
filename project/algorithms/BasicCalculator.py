class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = num = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c=='+':
                result += sign * num
                num = 0
                sign = 1
            elif c=='-':
                result += sign * num
                num = 0
                sign = -1
            elif c=='(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c==')':
                result += sign * num
                num=0
                result *= stack.pop()
                result += stack.pop()
        return result + sign * num

    def calculate2(self, s: str) -> int:
        stack = []
        n = 0
        op = '+'
        s += '+'

        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                n = n * 10 + int(c)
                continue
            if op == '+':
                stack.append(n)
            elif op == '-':
                stack.append(-n)
            elif op == '*':
                stack.append(stack.pop() * n)
            elif op == '/':
                stack.append(int(stack.pop() / n))

            op = c
            n = 0
        return sum(stack)