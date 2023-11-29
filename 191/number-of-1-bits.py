# 要數「有幾個1」可以用我上課教的「剝皮法」慢慢把每個 bit 拆出來。
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n>0: # 剝皮法, 只要還有剩洋蔥, 就繼續剝
            ans += n%2 # 剝下來的皮, 加到答案中, 累積有幾個1
            n = n // 2 # 像剝洋蔥一樣, 一層層剝, 剝完後, 數字就變小
        return ans
