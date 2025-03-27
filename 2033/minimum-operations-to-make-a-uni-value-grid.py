# LeetCode 2033. Minimum Operations to Make a Uni-Value Grid
# 每次可將 grid[i][j] 裡的值 +x 或 -x 問需「調幾次」，能將每個值調成相同
# 可利用「中位數」為目標，再看需「週幾次」能成功
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = []  # 把 grid 的值，調成 1D 陣列
        for g in grid:
            a += g
        a.sort()  # 把所有的值「小到大排好」
        mid = a[len(a)//2]  # 找到「正中間」的中位數（雙數不用平均，以免有小數點）
        ans = 0  # 統計一下有幾個點
        for c in a:  # 針對每個數
            diff = abs(c-mid)  # 距離的絕對值
            if diff % x != 0: return -1  # 無法整除，表示「無法調出來」失敗
            ans += diff // x  # 能調出來的話，就看「需要調幾次」
        return ans
