# nums1[i] = [id, val] 前面是 id 後面是對應的值
# nums2[i] = [id, val] 請把兩個 array 的對應 id 加起來
# 可都轉成 dict 方便加起來
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = defaultdict(int)
        for id, val in nums1:
            ans[id] = val # 逐項建好字典
        for id, val in nums2:
            ans[id] += val # 再逐項加起來
        ans = [[id, ans[id]] for id in ans] # 組合成 list
        return sorted(ans) # 再以id為主，排序好答案
