# LeetCode 861. Score After Flipping Matrix
# 有一堆0和1的matrix，1個move是挑某個 row 或 col 把 0/1 交換
# 可任意次 move。每個 row 是binary表示的數，每個row加起來最大是多少？
# 因沒什麼頭緒，偷看 Editorial 的解說，解釋「從最左邊」逐項flip即可
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        for i in range(M):  # 先處理「最高位」
            if grid[i][0] == 0:  # 希望最高位都是1，所以是0時，就整個row flip
                for j in range(N):  # flipRow(i)
                    grid[i][j] = 1 - grid[i][j]
        ans = M  # 最高位，對應的bit都變成1，以剝皮法來分析，可先放1*M=M
        for j in range(1, N):  # 從「高位」往「低位」測試
            now = 0  # 整個直的col數一數有幾個1，再決定是否 flipCol(j)
            for i in range(M):
                now += grid[i][j]
            ans = ans * 2 + max(now, M - now)  # flipCol() 對應 M-now
        return ans
