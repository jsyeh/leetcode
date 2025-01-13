# LeetCode 3223. Minimum Length of String After Operations
# 字串 s 挑 s[i]，左邊、右邊都至少有1格與s[i]相同，把「左右最近」的2個刪掉。
# 持續做，s要變最短。
class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        ''' 印出模擬結果，發現 0,1,2 之後都是 1,2,1,2循環
        for i in range(20):
            print(i, end=':')
            while i>=3:
                i -= 2
            print(i)
        '''
        for c in counter:
            # 每次刪掉2個，但不能小於3個
            # 可能剩1、剩2，但不可能剩0個
            if counter[c] < 3:  # 3以下，保留原本的數量
                ans += counter[c]
            else:  # 3以上，就會刪掉，變 1 或 2 。規則如下
                ans += (counter[c]-3)%2 + 1
        return ans
