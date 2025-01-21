# LeetCode 2017. Grid Game
# 機器人「往右」「往下」收集 grid 2 x n 的點數，起點在「左上」、終點在「右下」
# 第1隻機器人「努力搶點數」，讓第2隻機器人「再怎麼努力，卻只能收最少」
# 第2隻機器人也很努力搶點數，問第2隻機器人會搶到多少點收？
# 第1隻機器人，有 n 個可能「往下」的位置，右上、左下「剩餘點數」是第2隻機器人能收的「目標」
# 觀察後發現，第2隻機器人「只能吃右上」or「只能吃左下」兩種可能，可用 prefix sum 技巧解題
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])  # 長度，也對應 robot 1 往下 N 種可能
        prefix, postfix = [0] * N ,[0] * N
        for i in range(N-1):  # 更新 prefix sum 和 postfix sum
            prefix[i+1] = prefix[i] + grid[1][i]  # 左下 prefix sum
            postfix[N-2-i] = postfix[N-1-i] + grid[0][N-1-i]  # 右上 postfix sum
        print(postfix)
        print(prefix)
        ans = inf  # 模擬 robot 2 可能吃到的最佳剩餘點數（持續更新、越來越少）
        for i in range(N):  # robot 1 有 N 個可「從上換到下」的位置，決定 robot 2 剩多少能吃
            now = max(prefix[i], postfix[i])  # robot 2 可以「左下、右上」，挑「大的」吃
            ans = min(ans, now)  # 因 robot 1 努力壓 robot 2 的量，所以 robot 2 能吃的會越來越少
        return ans
