# LeetCode 3356. Zero Array Transformation II
# queries[i] 有多組 [left,right,val]，每次把陣列 nums 的 left...right 範圍
# 都減掉 0...val 間的任意值。依序處理「幾次後」nums 可全部會變成 0？
# 這題與 3355 題很像，用 diff 從頭到尾巡，便知「可不可行」，再用 binary search 即可
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N, Q = len(nums), len(queries)  # 陣列的大小
        def helper(k):  # 想知道 queries 挑前 k 項後，能不能成功
            diff = [0]*(N+1)  # 用來「昇降」的陣列，標註 left,right 昇降資訊
            for i in range(k):  # 現在處理「前 k 項」的 queries
                left, right, val = queries[i]
                diff[left] -= val  # 從 left 開始降
                diff[right+1] += val  # 在 right+1 回昇、恢復
            totalDiff = 0  # 累積的 diff 量
            for i in range(N):  # 針對 nums 陣列裡的每個數字
                totalDiff += diff[i]  # 算出「累積」昇降值
                if nums[i]+totalDiff > 0:  # 若無法將 nums[i] 無法降為0
                    return False  # 就失敗
            return True  # 若能全部走完、都能降為0，便是成功
        ans = bisect_left(range(Q+1), True, key=helper)  # k 從 0 ... Q 哪個可以 True
        if ans > Q: return -1  # Q 次不夠用，就失敗
        return ans  # 正確的 k 的次數
