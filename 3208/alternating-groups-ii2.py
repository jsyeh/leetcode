# LeetCode 3208. Alternating Groups II
# colors 有一堆0和1，繞成圈。請問有幾種「長度為k」的片段，是0、1交錯？
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        prev = colors[-1]
        N = len(colors)
        combo = 1
        for i in range(N+k-2):  # 要累積 k 項的話，要比對 k-1 次，再試 N-1 次
            if prev==colors[i%N]: combo = 1
            else: combo += 1
            if combo >= k: ans += 1
            prev = colors[i%N]
        return ans
