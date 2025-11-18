# LeetCode 717. 1-bit and 2-bit Characters
# 照著題目的方式解碼 0 or 10 or 11，
# 0 用1 bit，10 or 11 用 2 bits，問最後1個字元「是不是1bit」
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        N = len(bits)
        i = 0
        while i < N:
            if bits[i]==0:  # 遇到 0 開頭，一定是 1 bit
                i += 1  # 用掉 1 格
                last = 1  # 最近一次解碼，是 1 bit
            else:  # 遇到 1 開頭，一定是 2 bits
                i += 2  # 用掉 2 格
                last = 2  # 最近一次解碼，是 2 bits
        return last==1  # 題目問：最後一次解碼，是不是 1 bit
