# LeetCode 150. Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token=='+':
                now = s.pop()
                s[-1] += now
            elif token=='-':
                now = s.pop()
                s[-1] -= now
            elif token=='*':
                now = s.pop()
                s[-1] *= now
            elif token=='/':
                now = s.pop()
                s[-1] = int(s[-1]/now)
            else:
                s.append(int(token))
            # print(s)
        return s[-1]
