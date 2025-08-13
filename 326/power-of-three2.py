# LeetCode 326. Power of Three
# 給整數 n 請檢查它「是不是3的很多次方」
# ex. 1, 3, 9, 27, 81, 243, ...
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False  # 負數 or 0 都不是答案
        while n > 1:  # 剝皮法，一直剝到1為止
            if n%3 != 0:  # 過程中，一旦無法被3整除
                return False  # 就是失敗
            n = n // 3  # 繼續剝皮
        # 經過上面的 while 迴圈層層檢查，都沒失敗
        return True  # 那就是成功
