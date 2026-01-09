# LeetCode 1004. Max Consecutive Ones III
# 最多的連續1 --- 如果你能把 nums 裡把k個0變成1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = 0  # 左手i 右手j
        ans = 0  # 將 k 個0變成1後，最多的連續1數量
        zeros = 0  # 在 s[i]...s[j] 裡，有幾個0（不可超過k）
        while j < len(nums):  # 右手j往右
            zeros += (nums[j]==0)  # 更新 zeros
            while zeros > k:  # 若太多 zeros
                zeros -= (nums[i]==0)  # 左手i 吐掉
                i += 1  # 左手i 右移
            ans = max(ans, j-i+1)  # 更新答案（左右包含，要+1）
            j += 1  # 右手j 右移
        return ans
