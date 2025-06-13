# LeetCode 2616. Minimize the Maximum Difference of Pairs
# nums 陣列裡，找到 p 組 pair 的距離 abs(nums[i]-nums[j]) 的「最大值」最小（都不重覆index）
# 可用 binary search 找答案/猜數字：如果答案 ans 當變數，答案是多少時，有 p 組 pair
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        N = len(nums)  # 陣列裡有 N 個數字
        nums.sort()  # 將 nums 小到大排好，那「最大的距離」一定是 nums[-1] - nums[0]
        def helper(ans):  # 若距離的答案是 ans，能找到 p 組 pair「最大值」<= ans 嗎？
            total = 0  # 有「幾組pair」的距離 >= ans
            prevUsed = -1  # 兩兩一組，用掉的 index i
            for i in range(N-1):  # 要比較 i 及 i+1 距離是否在 ans 距離內
                if i==prevUsed: continue  # 前一個用過的數，就跳掉
                if nums[i+1] - nums[i] <= ans:  # 合乎距離，太好了(因 sort 過，右邊比左邊大)
                    total += 1  # 相鄰的距離「在範圍內」，就多找到1組 pair
                    prevUsed = i + 1  # nums[i+1] 有用過，不能再用了哦（避開）
            return total >= p  # total >= p 就代表「能找到p組」
        ans = bisect_left(range(nums[-1]+1), True, key=helper)  # 內建的 binary search
        return ans  # 用 binary search 找答案，用helper()來評量，找到適當的ans距離
