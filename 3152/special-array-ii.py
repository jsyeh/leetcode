# LeetCode 3152. Special Array II
# 希望 nums[query開始...query結束] 的 subarray 裡，相鄰的數「奇偶數」相交錯。
# 因 queries 有 10^5 次，且 nums 有 10^5 個，不能暴力兩層for迴圈。
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        N = len(nums)
        prevSpecial = [0]*N  # 記錄「到nums[i]為止，「奇偶數交錯」最長（往前回溯）到哪裡
        for i in range(1,N):
            if nums[i-1]%2 != nums[i]%2:  # 很好，是交錯的
                prevSpecial[i] = prevSpecial[i-1]  # 可繼承前一項的位置
            else:  # 若不是交錯
                prevSpecial[i] = i  # 只好歸零，從現在這裡「重新累積」交錯的部分
        # 建好後，便可照著 queries 逐項找答案
        ans = []
        for Qfrom, Qto in queries:
            if prevSpecial[Qto] <= Qfrom:  # 交錯範圍夠長，範圍能包含 Qfrom...Qto
                ans.append(True)  # 可以成功
            else:  # 交錯範圍不足
                ans.append(False)  # 就失敗了
        return ans
