# LeetCode 351. Android Unlock Patterns
# 手機解鎖 3x3 連線數字：數字不同，兩數字間，不能剛好經過「之前沒用過」的數字
# 給 m...n 對應 最少、最多 的數字數目 ex. m=1 n=1 代表只能按1個數字
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0]*10 for _ in range(10)] # 建出對照表，找到「中間」數
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5
        skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8

        visited = set()
        def helper(m, n, depth, now): # 最少、最多、目前用多少
            if depth==n-1: return 1  # 結束計算
            visited.add(now)
            if depth<m-1: ans = 0  # 深度還不夠，這層不加總
            else: ans = 1  # 這層要加總、停在這層也算1次

            for i in range(1,10):
                if i not in visited:
                    if skip[now][i]!=0 and skip[now][i] not in visited:
                        continue # 中間有壓到（未走過的）數字，就避開這輪
                    ans += helper(m, n, depth+1, i)
            visited.remove(now)
            return ans
        print(helper(m,n,0,1))
        return (helper(m,n,0,1) + helper(m,n,0,2)) * 4 + helper(m,n,0,5)
