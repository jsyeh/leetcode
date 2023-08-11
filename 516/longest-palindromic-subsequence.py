# 這題在 Editorial 的解法，是用利用 dict 去查 (left,right) 對照的最長值
# 我之前的解法，則是「將字串s反過來」變s2後，找它們的 Longest Common Sequence
# 我決定用我熟的這個方法，改用 Python 再做一次
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        # s2 = reversed(s)不能用這種方法
        s2 = s[::-1] # 字串利用 for 迴圈反過來
        
        table = [[0]*(N+1) for _ in range(N+1)] 
        # table[i][j] 是 s[i] vs. s2[j] 的 Longest Common Sequences長

        # 因預設值為 [0] 所以不用再初始化 table[i][0] 及 table[0][j]
        for i in range(1,N+1):
            for j in range(1,N+1):
                if s[i-1] == s2[j-1]: # 真幸運，相同，可以加分
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        return table[N][N]
