# LeetCode 2501. Longest Square Streak in an Array
# 找到 array 裡，挑一些數，小到大，裡面是「平方」的關係
# 題目 Hint 介紹 set() 快速查看「數字是否在 array 裡。
# 因「平方」長得很快, nums[i] <= 10^5 代表 while 迴圈最多只會跑5次
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)  # 利用 set() 來確認數字出現過
        ans = -1
        for num in nums:  # 依序看有沒有數字出現過
            now = 1  # 挑任1個數，長度從1個始
            while num*num in s:  # 平方數有出現
                num = num*num  # 就變身成「平方」
                now += 1  # 連續的長度+1
            if now>=2:  # 連續2個以上，才叫 streak 才查看它的長度
                ans = max(ans, now)  # 更新答案
        return ans
        
