class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1 = len(word1) + 1
        N2 = len(word2) + 1
        # table = [[0]*N2]*N1 # 這種寫法是錯的，因為變成都指到同一個
        # 下面寫法才是對的，不過這樣看起來 Python 好像也沒多簡潔...
        table = [[0 for _ in range(N2)] for _ in range(N1)]
        for i in range(N1):
            table[i][0] = i
        for j in range(N2):
            table[0][j] = j
        
        for i in range(1,N1):
            for j in range(1,N2):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    d1 = table[i-1][j] + 1
                    d2 = table[i][j-1] + 1
                    d3 = table[i-1][j-1] + 1
                    table[i][j] = min(d1,d2,d3)
        return table[N1-1][N2-1]
