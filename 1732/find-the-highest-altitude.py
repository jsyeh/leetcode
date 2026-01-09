# LeetCode 1732. Find the Highest Altitude
# 騎車走山路時，坡度「上上下下」的，可從 gain[i] 知道「上昇or下降多少」
# 從這個資訊，找出「山路的最高點」。可用 prefix sum 找到答案
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = now = 0
        for diff in gain:  # 逐一分析「上昇or下降」的資訊
            now += diff  # 累加到「現在的高度中」
            ans = max(ans, now)  # 持續更新、記錄「最高點」
        return ans
