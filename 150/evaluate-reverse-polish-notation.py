class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif token == '/': # 小心負數的除法，要留下「接近0」的整數
                b = stack.pop()
                a = stack.pop()
                minus = 0
                if a<0: # 遇到負的，如果直接//除法，答案差1
                    minus += 1 # 所以先統計有幾個負的
                    a = -a # 並把負數變成正數
                if b<0:
                    minus += 1
                    b = -b
                now = a//b
                if minus==1: now = -now # 如果有1個負的，正的就改成負的
                stack.append(now)
            else:
                stack.append(int(token))
        return int(stack.pop())
