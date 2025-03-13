# LeetCode 3355. Zero Array Transformation I
# queries 裡 [left,right] 把 nums[left]...nums[right] 可減 1
# 問 queries 全部做完後，有沒有機會把 nums 全部變成 0
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        diff = [0] * (N+1)  # Hint 建議用 diff array
        for left, right in queries:
            diff[left] -= 1  # left 這格開始降
            diff[right+1] += 1  # 再右邊1格，才會回昇
        totalDiff = 0  # 累積 total 昇降值
        for i in range(N):  # 從頭到尾巡一輪
            totalDiff += diff[i]
            if nums[i] + totalDiff > 0:  # 若昇降後，還有剩
                return False  # 那就沒辦法「降為0」失敗
        return True
