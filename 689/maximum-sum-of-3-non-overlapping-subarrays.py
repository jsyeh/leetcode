# LeetCode 689. Maximum Sum of 3 Non-Overlapping Subarrays
# 將 nums 分成 3 段「長度為k」且「不重疊」，加來要最大。本題目用了 3 次 Dynamic Programming 的技巧（先左邊、再右邊，最後查中間）
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        def sumK(i): return preSum[i+k] - preSum[i]  # 工具一：nums[i] 起 k 項總和（用preSum頭尾相減）
        def sumKKK(iLeft, iMiddle, iRight):  # 工具二：3 段(長度為k)加起來
            return sumK(iLeft) + sumK(iMiddle) + sumK(iRight)  # 左邊、中間、右邊，三段「長度為k」的 加起來
        N = len(nums)  # 陣列長度
        preSum = [0]  # 先算出 prefix sum
        for num in nums:  # 之後可用 prefix sum 再用減法，算出 nums[i] 起 k 項的和
            preSum.append(preSum[-1]+num)
        # 先左邊 DP
        posLeft = [0]  # 利用 DP 記錄前 i 項的最佳答案，對應 index
        for i in range(1,N-k+1):
            i0 = posLeft[-1]  # 之前最佳解的 index 位置
            if sumK(i) > sumK(i0): posLeft.append(i)  # 答案更好，改放 i
            else: posLeft.append(i0)  # 答案沒更好，照舊放 i0
        # 再右邊 DP
        posRight = [ N-k ]  # 利用 DP 記錄（從右到左的）前 i 項的最佳答案，對應 index
        for i in range(N-k-1, -1, -1):
            i0 = posRight[-1]  # 之前最佳解的 index 位置
            if sumK(i) >= sumK(i0): posRight.append(i)  # 答案更好（或相同但更左邊），改放 i
            else: posRight.append(i0)  # 答案沒更好，照舊放 i0
        posRight.reverse()  # 將陣列反過來，以便 postRight[i] 對應 i 之後的最佳解的位置
        # 有了 posLeft 和 posRight，接下來，試中間這段 DP
        ans = [0, k, k*2]  # 最簡單的答案，先試 連續的 3 段 k 個連起來（對應的 index）
        for i in range(k, N-k-k+1):  # 中間 middle 的 index 可能的位置，都去試
            iLeft, iRight = posLeft[i-k], posRight[i+k]  # 將 middle 的 k 個保留後，查左邊、右邊「對應最好的 index」
            if sumKKK(iLeft, i, iRight) > sumKKK(ans[0], ans[1], ans[2]):  # 查表法，查出「現在這個組合」是否更好
                ans = [iLeft, i, iRight]  # 更好的話，就更新成「現在這個組合」的 index
        return ans
