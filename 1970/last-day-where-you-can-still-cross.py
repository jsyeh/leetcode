# LeetCode 1970. Last Day Where You Can Still Cross
# row x col 的地圖裡，格子會照 cells 的座標「依序被水淹沒」(cells 座標是 1-index)
# 想能從「最上面」沿陸地走到「最下面」，請問「最晚」哪天「還能順利從top走到bottom」 
# 因格子很多，有人建議用 binary search 去猜答案（哪一天），再 queue BFS 模擬「能不能通」
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0] * col for i in range(row)] # 先把「淹沒的時間」標示在地圖上
        for day,(i1,j1) in enumerate(cells):  # 第 day 天，淹沒 (i1,j1)
            grid[i1-1][j1-1] = day  # 將 1-index 換算成 0-index，標示「格子」在哪天淹沒
        def helper(day):  # 請問第 day 天「能順利從top走到bottom嗎？」 
            queue = deque()  # 利用 queue 資料結構進行 BFS
            visited = set()  # 走過的，就不要再走
            for j in range(col):  # the top row 看有哪幾格「還沒淹水」
                if grid[0][j] >= day:  # 還沒淹水
                    queue.append((0,j))  # 可當「開始位置」
                    visited.add((0,j))  # 走過，就不要再走
            while queue:  # BFS 模擬的 queue 資料結構裡「還有地方能走」
                i,j = queue.popleft()  # 現在站在 (i,j) 座標
                for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):  # 往4個方向走
                    if ii<0 or jj<0 or ii>=row or jj>=col: continue  # 避開邊界
                    if (ii,jj) in visited or grid[ii][jj] < day: continue  # 避開走過or淹沒
                    if ii==row-1:  # 走到 the bottom row，太好了
                        return 0  # 能順利走到（成功標0、失敗標1，以便bisect_right()函式使用）
                    visited.add((ii,jj))  # 加入 set() 避開重覆走
                    queue.append((ii,jj))  # 加入 queue 資料結構
            return 1  # 不能順利走到（成功標0、失敗標1，以便bisect_left()函式使用）
        # for day in range(row*col): print(helper(day), end=' ')  # Debug 觀察 helper() 行為
        return bisect_left(range(row*col), 1, key=helper) - 1  # 「不能走」最左邊「再左一格」能走
