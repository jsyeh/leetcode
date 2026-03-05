# LeetCode 1758. Minimum Changes To Make Alternating Binary String
# 每次可換1格（0變1或1變0），問最少要換幾格， 能把字串 s 變成「0、1交錯」
class Solution:
    def minOperations(self, s: str) -> int:
        ans0 = ans1 = 0  # 對應目標：0開始的交錯字串、1開始的交錯字串
        for i in range(len(s)):  # 逐一檢查
            if i%2==0:  # 偶數位（開始的也是偶數位）
                if s[i]=='0': ans1 += 1  # 若開始是0，則ans1付出代價
                else: ans0 += 1  # 若開始是1，則ans0付出代價
            else:  # 奇數位
                if s[i]=='1': ans1 += 1  # 模仿上面
                else: ans0 += 1  # 模仿上面
        return min(ans0, ans1)  # 最少的次數
