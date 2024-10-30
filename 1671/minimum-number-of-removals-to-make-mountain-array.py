# LeetCode 1671. Minimum Number of Removals to Make Mountain Array
# 「像山一樣」的山形陣列，會「先上升、再下降」。nums裡「最少刪幾個」會變成「像山一樣」的山形陣列。
# Hint 1: 想找「最長」的「像山一樣」的山形subseqnece
# Hint 2: 用 LIS 問題的解法（的變形），來解類似的問題
# 所以就「左到右的LIS」和「右到左的LIS」都準備好，再巡一次，就知道答案了
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        LIS1, LIS2 = [1]*N, [1]*N  # LIS1 左到右，LIS2 右到左，預設值「自己1個人」
        LIS1[0] = 1  # LIS[i] 對應「以nums[i]結尾的LIS長度」
        for i in range(N):  # 現在處理 LIS1[i] 「左到右的LIS」
            for k in range(i):  # 左邊的每項都考慮 
                if nums[k]<nums[i]:  # 只要左小右大
                    LIS1[i] = max(LIS1[i], LIS1[k]+1)  # 就更新
        LIS2[N-1] = 1
        for i in range(N-1, -1, -1):  # 現在處理 LIS2[i] 「右到左的LIS」
            for k in range(i, N):  # 右邊的每項都考慮
                if nums[i]>nums[k]:  # 只要左大右小
                    LIS2[i] = max(LIS2[i], LIS2[k]+1)  # 就更新
        ans = 0  # 想找「山形」的「最長」
        for i in range(1,N-1): # 因為要山形，山峰不能在最左、最右邊
            if LIS1[i]!=1 and LIS2[i]!=1:  # 如果有任一個是1，就不是山形
                ans = max(ans, LIS1[i]+LIS2[i]-1)
        return N - ans  # 反過來，就是「要刪最少、要刪幾個」
