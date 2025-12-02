# LeetCode 3623. Count Number of Trapezoids I
# 有幾種「梯形」有一組對邊「對x軸平行」，即2個頂點y相同、另2個頂點y相同
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        counter = Counter()  # 先統計「有幾種相同的y座標」
        for x,y in points:
            counter[y] += 1  # 有相同的 y 的話，要放在一起
        MOD = 10**9+7  # 因答案很多，要取10^9+7 的餘數
        ans = 0  # 答案會有幾組
        prev = 0  # 之前可能的「挑2相同y的頂點」有幾種可能
        for y in counter:  # 迴圈，針對不同的y座標
            now = counter[y]  # 現在這層「有幾個頂點」有「相同的y」
            # 排列組合 C(now, 2) = now * (now-1) // 2  從now挑2點的可能
            ans = (ans + now * (now-1) // 2 * prev) % MOD  # + 這層挑2點 * 之前可能的挑法
            prev += now * (now-1) // 2  # 累積到「之前的可能挑法」
        return ans
