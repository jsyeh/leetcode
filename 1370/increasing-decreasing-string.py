# LeetCode 1370. Increasing Decreasing String
# s 要變出新字串，規則：先挑最小，再挑「不重覆」的最小，直到挑不到。
# 再挑大，再挑「不重覆」的最大，直到挑不到。重覆做。
class Solution:
    def sortString(self, s: str) -> str:
        counter = Counter(s)
        ans = []
        while counter:  # 持續做到 counter 用完
            for c in sorted(counter.keys()):  # 小到大
                ans.append(c)
                counter[c] -= 1
                if counter[c]==0:  # 用完，就刪除
                    del counter[c]
            for c in sorted(counter.keys(), reverse=True):  # 大到小
                ans.append(c)
                counter[c] -= 1
                if counter[c]==0:  # 用完，就刪除
                    del counter[c]
        return ''.join(ans)
