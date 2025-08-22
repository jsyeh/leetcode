# LeetCode 3195. Find the Minimum Area to Cover All Ones I
# 2D binary 陣列裡有0、有1請找出「最小的長方形」包含全部的1
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # 其實就找「最左邊、最右邊」邊界及「最上面、最下面」邊界
        left, right = inf, -1  # 逆向思考：
        up, down = inf, -1  # 邊界先放「反過來」的極值，之後再更新
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    left = min(left, j)  # 更新「左邊界」
                    right = max(right, j)  # 更新「右邊界」
                    up = min(up, i)  # 更新「上邊界」
                    down = max(down, i)  # 更新「下邊界」
        if left==inf: return 0  # 沒有動到邊界，就沒有1，面積是0
        # 面積公式：寬 * 高，要記得「種樹問題」的邊界，所以要再+1
        return (right-left+1) * (down-up+1)
        
