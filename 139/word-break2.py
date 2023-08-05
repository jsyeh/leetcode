# 再重寫一次：先建 hash set，再將 s 逐字斷句，看能否在hash set裡找到。剛好到到句尾就成功
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        global found # found is a global variable
        hashset = set(wordDict)
        N = len(s)
        visited = [False]*(N+1)
        found = False
# google: python UnboundLocalError: local variable referenced before assignment but it is global vairable
# https://bobbyhadz.com/blog/python-unboundlocalerror-local-variable-name-referenced-before-assignment
# Local variable referenced before assignment in Python

        def visit(n):
            global found # found is a global variable
            # print("visit()", n)

            if n == N: 
                found = True # found is a global variable
            if found: return
            if n > N: return
            if visited[n]: return
            visited[n] = True

            for right in range(n+1,N+1):
                if right>N: continue # 避開
                # print(s[n:right], n, right)

                if s[n:right] in hashset:
                    visit(right)

        visit(0)
        # print(visited)
        return found
