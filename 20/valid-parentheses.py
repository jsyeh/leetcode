class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c=="(" or c=="[" or c=="{":
                stack.append(c)
            elif c==")":
                if len(stack)>0 and stack[-1]=="(":
                    stack.pop()
                else: # 沒辦法對應正確
                    return False
            elif c=="]":
                if len(stack)>0 and stack[-1]=="[":
                    stack.pop()
                else: # 沒辦法對應正確
                    return False
            elif c=="}":
                if len(stack)>0 and stack[-1]=="{":
                    stack.pop()
                else: # 沒辦法對應正確
                    return False
        if len(stack)>0:
            return False
        else:
            return True

