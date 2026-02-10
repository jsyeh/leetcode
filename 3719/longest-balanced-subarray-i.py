# LeetCode 3719. Longest Balanced Subarray I
# nums 找到一段「最長」的小陣列，裡面「不同的奇數、不同的偶數」數量相等
# `因為 N 很小，試著用暴力法來試`
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums) 
        ans = 0
        for i in range(N):  # subarray 的開始位置
            countOdd, countEven = Counter(), Counter()  # 計算數量
            for k in range(i, N):  # 持續試各種可能的結束位置
                if nums[k]%2==1: countOdd[nums[k]] += 1
                else: countEven[nums[k]] += 1
            
                if len(countOdd) == len(countEven):  # 符合條件
                    ans = max(ans, k-i+1)  # 更新答案
        return ans

# 下面是用 prefix sum 的概念，但在一些測試資料[6,6]會錯。

''' 
# 用 prefix sum 概念，記錄 diff count 位置。若重覆出現，「相減」即為「0」代表「數量相同」
        table = {0:-1}  # 之前出現過的位置：記錄「奇數數量-偶數數量」的第一次出現的位置
        table2 = {0,(0,0)}
        countOdd = Counter()  # 用來累計「不同的奇數數字」出現的數量
        countEven = Counter()  # 用來累計「不同的偶數數字」出現的數量
        ans = 0
        for i, num in enumerate(nums):
            if num%2==1: countOdd[num] += 1  # 更新「奇數數字」的出現數量
            else: countEven[num] += 1  # 更新「偶數數數字」的出現數量
            diff = len(countOdd) - len(countEven)  # diff count
            if diff in table:  # 若重覆出現，「相減」即為「0」代表「數量相同」
                ans = max(ans, i - table[diff])  # 現在位置 - 第一次出現的位置
            else:  # 若沒出現，就記錄 diff 值第一次出現的位置
                table[diff] = i
        return ans
# testcase 917/999: [6,6]
[10,6,10,7]
[22,22,26,25,10]
'''
