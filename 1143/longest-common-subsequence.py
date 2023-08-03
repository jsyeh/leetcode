class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)
        table = [[0]*(N2+1) for _ in range(N1+1)]
        # table[i][j] 表示 text1 text2 分別使用 i j 個字母，LCS的長度

        # 其實下面的迴圈不用寫，因為宣告 table 時，裡面都已經塞[0]了
        # for i in range(N1):
        #     table[i][0] = 0 # text2 長度為0時，LCS的長度都是0
        # for j in range(N2):
        #     table[0][j] = 0 # text1 長度為0時，LCS的長度都是0
        
        for i in range(1,N1+1):
            for j in range(1,N2+1):
                if text1[i-1] == text2[j-1]: # 有幸有相同的字母
                    table[i][j] = table[i-1][j-1] + 1 # LCS +1
                else: # 不幸沒有相同，那就挑大的吧
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        return table[N1][N2] # 長度都用齊時，最好的 LCS 值

