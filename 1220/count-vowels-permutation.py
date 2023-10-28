# 題目Hard，提供aeiou母音的「組字」規則，給長度，問可能的字（排列組合）有幾個
# 看了題目，10**9+7 就表示答案很多，所以很像DP的題目。
# 在Discussion裡，有人說「其實很簡單」，我突然想通了：table[長][結尾字母] 再去更新

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0]*5 for _ in range(n+1)]
        # dp[長度][aeiou其中一個做結尾]
        MOD = 10**9+7
        dp[1] = [1]*5 # 基礎的5個字母，各使用1次
        for L in range(2,n+1):
            # 改寫一下規則，i最奇怪，後面不能放i，但可放aeou
            # 所以 a在e,i,u後  e在a,i後  i在e,o後  o在i後. u在i,o後
            dp[L][0] = (dp[L-1][1]+dp[L-1][2]+dp[L-1][4]) % MOD # e,i,u
            dp[L][1] = (dp[L-1][0]+dp[L-1][2]) % MOD # a,i
            dp[L][2] = (dp[L-1][1]+dp[L-1][3]) % MOD # e,o
            dp[L][3] = (dp[L-1][2]) # i
            dp[L][4] = (dp[L-1][2]+dp[L-1][3]) # i,o

        return sum(dp[n]) % MOD # 要記得再 MOD
# case 4/43: 5 要 output 68 但我寫成 65, 少了3個。所以規則打字打錯
