# 有種直覺的作法，是XOR全部巡過，便會得到答案 O(n)
# 不過題目要求，要O(log n)的時間，所以不能全部巡一次。
# 可以使用 binary search, 查某2相鄰的是否相同。相同就在右半邊、不相同就在左半邊
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        return ans
