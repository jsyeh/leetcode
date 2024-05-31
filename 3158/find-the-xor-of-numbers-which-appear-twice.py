# LeetCode 3158. Find the XOR of Numbers Which Appear Twice
# 找到 nums 裡「剛好出現2次」的數, 全部用 XOR 混起來。
# 直覺會利用「字典」, 記下「數字出現的次數」,看誰出現2次
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        table = {}  # 這裡用Python 的「字典」來做
        for num in nums:  # 全部數字都巡一次
            if num not in table:  # 若沒出現過
                table[num] = 1  # 就加到 table 裡
            else:  # 若曾出現過
                table[num] += 1  # 出現次數就+1
        ans = 0
        for num in table:  # 巡第2次, 看 table 裡的每個數
            if table[num]==2:  # 題目要的、剛好出現2次的數
                ans ^= num  # 照題目要求, 用 XOR 混起來
        return ans
