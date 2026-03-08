# LeetCode 1980. Find Unique Binary String
# 陣列 nums 有N個「長度N的二進位字串」，找「沒出現在nums」且「長度N的字串」
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)  # 剛好 陣列大小len(nums) == 字串長度len(nums[0])
        s = set(nums)  # 把陣列裡的字串，變成 set() 加速「找有沒有出現在nums」
        for i in range(N+1):  # N 最大只有16，用for迴圈暴力找 N+1 個數
            if bin(i)[2:].zfill(N) not in s:  # 「二進位字串」沒有出現在nums
                # 轉成二進位字串'0bXXX'，再用[2:]取0b後面的數，再用 0 補齊 N 位數
                return bin(i)[2:].zfill(N)  # 用 zfill(N) 補齊長度N
