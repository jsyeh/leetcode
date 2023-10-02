# 模擬題，照著rings來放，最後回傳「3色都有」的柱子有幾個
class Solution:
    def countPoints(self, rings: str) -> int:
        table = [set() for _ in range(10)] # 神奇的資料結構
        # table[i] 對應 rod i 有幾個色彩的 set()

        N = len(rings)
        for i in range(0,N,2): # 一次查2個字母 [RGB][0-9]
            c, d = rings[i], int(rings[i+1])
            table[d].add(c) # rod d 要加入 color c
        
        ans = 0
        for i in range(10):
            if len(table[i])==3: # 如果 rod i 有3色
                ans += 1 # 答案 += 1
        return ans
