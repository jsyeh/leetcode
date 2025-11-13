# LeetCode 3228. Maximum Number of Operations to Move Ones to the End
# s 字串中，挑 '10' 的1，移到最右邊「撞到另1個1為止」，想移動「最多次」
# 直覺像「開碰碰車」一樣，最左邊的先往右，就可移「最多次」。
# 變成「幾個1」然後「一堆0」再「幾個1」再「一堆0」即可算出答案
class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0  # 累積答案
        ones = 0  # 左邊累積「幾個1」
        nowOne = False  # 現在是'1'嗎？
        for c in s:  # 逐一處理字母
            if c=='1':  # 遇到1個1
                ones += 1  # 累積1
                nowOne = True  # 現在是'1'
            elif nowOne and c=='0':  # 現在「從1變成0」
                nowOne = False  # 狀態改變
                ans += ones  # 狀態改變時，左邊有「幾個1」都能增加「移動量」
        return ans
