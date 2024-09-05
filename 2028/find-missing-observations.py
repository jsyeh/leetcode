# LeetCode 2028. Find Missing Observations
# 丟n+m個骰子，有n個miss沒看到，但有mean平均值。找出miss掉的n個值
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # 要從 m 個 rolls[i] 的值，及總平均值mean，找出n個miss值
        total = mean * (len(rolls)+n)
        now = total - sum(rolls)  # 現在now要分給n個骰子
        if now/n < 1 or now/n > 6:
            return []  # 竟然比1小 or 比6大，不合理的平均值失敗
        diff = now % n  # 比平均now//n多的數，要再分配出去
        ans = [now//n]*(n-diff) + [now//n+1]*diff
        # 前面放平均的整數now//n，後面放 diff 個 +1 的數
        return ans
