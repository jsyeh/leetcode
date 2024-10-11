# LeetCode 154. Find Minimum in Rotated Sorted Array II
# 這題是 Hard 題，但是如果直接暴力法去找，是否也是可以的呢？
# 因為數字只有 5000 個，直接暴力法，竟然就接受了，直接呼叫函式也行。
# 但題目應該希望「善用sorted」的概念，用變形的 binary search 來做吧！
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
