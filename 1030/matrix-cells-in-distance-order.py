# 題目的英文寫的有點難懂。看了Solutions才搞𢤦題目，
# 原來是要在 「以0,0開始」的 rows x cols 矩陣裡，把座標都列出來
# 再依照 rCenter, cCenter 的距離，小到大都列出來
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ans = [[i,j] for i in range(rows) for j in range(cols)]
        # 先把 rows x cols 的全部值，都列出來
        ans.sort(key = lambda x: abs(x[0]-rCenter)+abs(x[1]-cCenter))
        return ans
