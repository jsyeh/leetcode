# LeetCode 2999. Count the Number of Powerful Integers
# start...finish 的這些數裡，結尾是 s 的數，每位數都 <= limit 的數「有幾個」
# 但 10^15 是超大範圍，不能用 for 迴圈暴力試。Hint 1: 用 DP 解1..x
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        @cache  # 利用 Top-down dynamic programming 來解
        def helper(x, full):  # 函式呼叫函式，參數：現在數字（的字串）、有沒有全滿
            if int(x) < int(s): return 0  # 現在的數 x 太小、不足 s，失敗
            if len(x)==len(s): return 1  # 長度剛好夠湊 1 個數，就是 s 本身
            now, others = x[0], x[1:]  # 「最高位」及「剩下」
            ALL9 = str(10**(len(x)-1) - 1)  # 比 x 少1位、全部都是 9
            if full or int(now) > limit:  # 很夠用（全滿or最高位更大）那倍數是 limit + 1 
                return helper(ALL9, True) * (limit+1)  # 全滿的部分，拿 999 之類的數，能有 limit + 1 倍
            else:  # 不夠用、沒有滿，就只能 0... now-1 共 now 個數，再
                ans1 = helper(ALL9, True) * int(now)  # 全滿的部分，拿 999 之類的數，能有 now 倍
                ans2 = helper(str(others), False)  # 剩下的量、沒有全滿
                return ans1 + ans2
        return helper(str(finish), False) - helper(str(start-1), False)  # Hint 3: 照範圍「相減」
