# 比較沒有效率的寫法, 不過同學比較容易理解
class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        ans = 0 # 最後的答案
        for left in range(N-1): # 要減1 留給右邊
            # 0...left   left+1...N-1  左邊有幾個0,右邊有幾個1
            now = 0 # 現在的答案
            for i in range(N):
                if i<=left and s[i]=='0': now += 1 # 左邊的0
                if i>left and s[i]=='1': now += 1  # 右邊的1
            if now > ans: ans = now # 如果現在now比答案ans更大, 更新答案
        return ans
