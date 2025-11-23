# LeetCode 1262. Greatest Sum Divisible by Three
# 將 nums 裡的數儘量相加，加出的結果「是3的倍數」且「最大」
# (1) 3的倍數全加，一定可以 (2) 餘1、餘2可配對 (3) 3個餘1、3個餘2，也可
# Hint 建議用 Dynamic Programming 來解，保證得到正確解答
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        table = [0, 0, 0]  # %3 餘0、餘1、餘2 的最大值，持續更新
        for num in nums:  # 逐一處理 nums 裡的每個數
            # table[:] 會複製 餘0、餘1、餘2 的最大值，再依 num 來更新
            for prev in table[:]:  # 複製目前餘數的3種可能（都是目前最大值）
                mod = (prev+num)%3  # 加起來的（新）餘數是多少
                if prev+num > table[mod]:  # 如果加上 num 後，能讓（新）餘數對應加總更大
                    table[mod] = prev+num  # 就更新
        return table[0]  # 最後「加總的3的倍數（餘0）最大」就是答案
