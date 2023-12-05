# 題目的描述不太容易懂: n <= 100, 每天會增加一些數字 n%i==1 讓數字變多。10億天後, 有多少數字
# 直接模擬, 可能要花多時間。不過別擔心, 因為全部的數字, 都不能超過n, 所以好像還好。
# 突然想到，可先暴力建好資料結構，再去模擬
class Solution:
    def distinctIntegers(self, n: int) -> int:
        d = defaultdict(list)
        for i in range(101): # 上界
            for k in range(1,i): # %k 記得分母不能是0
                if i%k==1: # 符合題目要求
                    d[i].append(k) # 建好資料結構
        
        ans = 1
        visited = [False]*(n+1)
        stack = [n] # DFS
        visited[n]
        while len(stack)>0: # DFS
            now = stack.pop()
            for i in d[now]: # 其他可放在board上的數
                if not visited[i]: # 沒有用過的話
                    stack.append(i) # 放入 stack
                    visited[i] = True # 用它
                    ans += 1 # 多放1個數
        return ans
        
        
