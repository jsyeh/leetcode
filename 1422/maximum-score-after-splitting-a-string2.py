# LeetCode 1422. Maximum Score After Splitting a String
# "00111" 想知道左邊幾個0、右邊幾個1 加起來最多
# for left in range(N-1)    0...left左邊  右邊left+1...N-1
# 把字串斷成左邊、右邊
# 左邊有「幾個」0, 加右邊有「幾個」1, 求最大值
# 先寫「很沒有效率」的方法, 用兩層迴圈, 暴力去試全部的可能。
class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s) # 先知道長度, 以便迴圈使用
        ans = 0 # 最後(最好)的答案
        for left in range(N-1): # 0...left 是左邊, left+1...N-1 是右邊
            now = 0 # 現在這個 left 對應的加總結果
            for i in range(N): # 每格都去巡
                if i<=left and s[i]=='0': now += 1 # 左邊的0 都要加
                if i>left and s[i]=='1': now += 1 # 右邊的1 都要加
            if now>ans: ans = now # 答案更好的話, 更新答案
        return ans
