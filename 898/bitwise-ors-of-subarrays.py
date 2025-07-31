# LeetCode 898. Bitwise ORs of Subarrays
# arr 取出「連續 subarray（最短有1個）」進行 bitwise OR 有幾種答案？
# 暴力法「用2層for迴圈」會超過時間。
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()  # 所有可能 subarray 的 OR 答案，放這裡
        now = set()  # 到 arr[i] 為止所有 subarray 的 OR 值
        for i in range(len(arr)):
            now = {arr[i] | prev for prev in now} | {arr[i]}
            ans |= now
        return len(ans)
