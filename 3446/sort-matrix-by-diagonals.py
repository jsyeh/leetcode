# LeetCode 3446. Sort Matrix by Diagonals
# 正方形的 grid 裡，希望「下三角（含對角線」左上到右下「慢慢減少」
#「上三角」左上到右下「慢慢增加」。請你將「這些斜線」裡的元素排序好，完成任務。
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)  # 先得到「正方形」的大小
        # 左上到右下的線，對應規則是 -N < i-j < N
        table = defaultdict(list)  # 「對應斜線」的 list
        for i in range(N):  # 先針對每一個格子，將值放入「對應斜線」的 list 裡
            for j in range(N):
                table[i-j].append(grid[i][j])
        ans = [[0]*N for i in range(N)]
        # 接下來，將 table 裡的線，下三角（含對角線）、上三角 分開處理
        for ij in range(N):  # 下三角（含對角線）對應 i-j>=0 是大到小排序
            table[ij].sort(reverse=True)  # 大到小排序
            for j in range(len(table[ij])):  # 依序放回 ans[i][j] 裡
                i = ij + j  # 由i-j=ij關係，推算出 i = ij + j
                ans[i][j] = table[ij][j]  # 
        for ij in range(-1, -N, -1):  # 上三角對應 i-j<0 是小到大排序
            table[ij].sort()  # 小到大排序
            for i in range(len(table[ij])):  # 依序放回 ans[i][j] 裡
                j = i - ij  # 由i-j=ij關係，推算出 j = i - ij
                ans[i][j] = table[ij][i]
        return ans
