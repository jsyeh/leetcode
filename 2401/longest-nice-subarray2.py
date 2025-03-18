# LeetCode 2401. Longest Nice Subarray
# 想找「最長的連續subarray」裡「任兩數」bitwise AND 為 0
# 也就是，連續subarray裡，所有數「都不能用到相同的bit」
# 今天的主題是 bit 相關，使用 & | ^ 來做，配合「毛毛蟲」來找答案。
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        usedBit = 0  # 把「毛毛蟲」裡用的 bit 都塞進去
        ans = 1  # 不管如何，1個數，一定不會重覆，是預設的答案
        j = 0  # 左邊的尾巴
        for i in range(len(nums)):  # 右邊的頭 i 往右吃
            while usedBit & nums[i] != 0:  # 用「AND 比對」發現有bit重覆
                usedBit ^= nums[j]  # 「XOR 去掉」左邊尾巴 nums[j]
                j += 1  # 左邊的尾巴「吐出來」
            usedBit |= nums[i]  # 「OR 加入」將 nums[i] 正式加入
            ans = max(ans, i-j+1)  # 更新答案的長度
        return ans
