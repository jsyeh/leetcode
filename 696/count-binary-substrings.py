# LeetCode 696. Count Binary Substrings
# 有幾種 substring 裡面有「相同數量的0和1」而且「0相連」「1相連」
# 好像也可以用「毛毛蟲」來解，但更像「分group」再「兩兩併起來」即可
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1,len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        # 接下來「兩兩併起來」
        ans = 0
        for i in range(1,len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
