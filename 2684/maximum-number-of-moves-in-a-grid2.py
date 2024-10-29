# LeetCode 2684. Maximum Number of Moves in a Grid
# 從左到右走，能挑選「上、中、下」格，數字要越來越大，最多能走幾步？
# 利用 stack 實作 backtrack 法，可解得「又快又好」(要用visited記錄走過的位置，不要重覆走)
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])  # 先得到長寬
        ans = 0
        stack = [(i,0,0) for i in range(M)]  # 先布下「種子」，從最左邊(i,0) 出發，走0步
        visited = set([(i,0) for i in range(M)])  # 走過的格子記起來，不要再走囉！
        while stack:  # 只要 stack 還有東西在裡面
            i,j,move = stack.pop()  # 現在在(i,j)的位置，走了move步
            ans = max(ans, move)  # 更新答案
            if j+1>=N: continue  # 若再往右走，會超過邊界，換下一組
            if i-1>=0 and grid[i-1][j+1]>grid[i][j] and (i-1,j+1) not in visited:  # 可往右上走
                stack.append((i-1,j+1, move+1))
                visited.add((i-1,j+1))  # 標示visited
            if grid[i][j+1]>grid[i][j] and (i,j+1) not in visited:  # 可往右走
                stack.append((i,j+1, move+1))
                visited.add((i,j+1))  # 標示visited
            if i+1<M and grid[i+1][j+1]>grid[i][j] and (i+1,j+1) not in visited:  # 可往右下走
                stack.append((i+1,j+1, move+1))
                visited.add((i+1,j+1))
        return ans
