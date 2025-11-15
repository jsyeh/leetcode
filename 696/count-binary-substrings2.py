# LeetCode 696. Count Binary Substrings
# 有幾種 substring 裡面有「相同數量的0和1」而且「0相連」「1相連」
# 好像也可以用「毛毛蟲」來解，但更像「分group」再「兩兩併起來」即可
# 也可直接用2個數來計算、不用開陣列
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = now = 0
        prevC = 0  # 前一個字母
        ans = 0  # 累積的數量
        for i in range(len(s)):
            if prevC != s[i]:  # 不相同的話
                ans += min(prev,now)  # 累積的數量，是左右相鄰的最小值
                prev, now = now, 1  # 換下一組
                prevC = s[i]  # 換字母
            else:  # 相同的話
                now += 1  # 現在的數量+1
        ans += min(prev, now)  # 累積的數量，是左右相鄰的最小值
        return ans
