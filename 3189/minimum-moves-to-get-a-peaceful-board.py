# LeetCode 3189. Minimum Moves to Get a Peaceful Board
# 西洋棋的城堡，可直走、橫走。有n個城堡（有n組座標），放在nxn的棋盤上
# 一次可移動1格，要走幾格後，才能讓「城堡」和平相處/互相不攻擊。
class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        n = len(rooks)
        ans = 0
        
        # 只要把兩個方向，都能「每格分開」，就完成了
        rooks.sort()  # 先照著x座標排序
        for i in range(n):  # 每個棋子，分散到0..n-1
            ans += abs(i - rooks[i][0])
        
        rooks.sort(key=lambda x: x[1]) # 再照y座標排序
        for i in range(n):  # 每個棋子，在y方向，也分散0..n-1
            ans += abs(i - rooks[i][1])
        
        return ans
