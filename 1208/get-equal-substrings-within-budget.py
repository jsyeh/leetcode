# LeetCode 1208. Get Equal Substrings Within Budget
# 兩個長度相同的字串 s, t，想找「最長的 substring」能在修改後相同。
# （修改需要 cost, 但能用的cost有上限）
# substring 是字串中「某段」連續的字母。可以利用 sliding window 解
# 技巧：像「毛毛蟲」一樣，頭（右邊）往右前進、尾（左邊）適時退縮。
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)  # 字串長度
        ans = 0
        head, tail = 0, 0
        while head < N:  # 頭head最後的終點（右邊界）
            maxCost -= abs(ord(s[head])-ord(t[head])) # 用到 cost
            while maxCost<0:  # 不夠用、變成負的，那尾巴就右退縮
                maxCost += abs(ord(s[tail])-ord(t[tail]))
                tail += 1
            ans = max(ans, head-tail+1)  # 更新答案
            head += 1
        return ans
